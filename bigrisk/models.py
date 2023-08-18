from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import csv
from pprint import pprint
import random

author = "Philipp Chapkovski, UBonn"

doc = """
Tail, no median lottery project
"""


class Constants(BaseConstants):
    name_in_url = "bigrisk"
    players_per_group = None
    num_rounds = 2
    POSITIVE_ENDOWMENT = 10
    NEGATIVE_ENDOWMENT = 200
    price_ranges = ((0.01, 0.50), (0.50, 1.50), (1.50, 2.75), (2.75, 5), (5, 10))
    # READ THE DATA
    path_to_data = "./data/"

    with open(f"{path_to_data}lotteries.csv", "r") as f:
        reader = csv.DictReader(f)
        lotteries = [i.get("header") for i in reader]

    with open(f"{path_to_data}tickets.csv", "r") as f:
        reader = csv.DictReader(f)
        tickets = list(reader)
        tickets = [
            {**i, "formatted_portion": f"{float(i.get('portion')):.2%}"}
            for i in tickets
        ]
    with open(f"{path_to_data}heavytail.csv", "r") as f:
        tails = [float(line.strip()) for line in f.readlines()]


class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            for p in self.session.get_participants():
                p.vars['chosen_round']=random.randint(1,Constants.num_rounds)
        neg = self.session.config.get("negative")
        tail = self.session.config.get("tail")
        endowment = (
            Constants.NEGATIVE_ENDOWMENT if neg else Constants.POSITIVE_ENDOWMENT
        )
        if tail:
            lotteries = Constants.lotteries.copy()
        else:
            lotteries = Constants.lotteries.copy()[:4]
        for p in self.get_players():
            p.chosen_round=p.participant.vars['chosen_round']
            p.endowment = endowment
            p.tail = tail
            p.participant.vars["lotteries"] = lotteries
            for i in range(1, 6):
                prange = Constants.price_ranges[i - 1]
                price = round(random.uniform(*prange), 2)
                setattr(p, f"ticket_price_{i}", price)
            p.ticket_chosen = random.randint(1, 5)
            p.price_chosen = getattr(p, f"ticket_price_{p.ticket_chosen}")
            p.personal_outcome = random.choice(Constants.tails)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    def set_final_payoff(self):
        self.payoff = self.in_round(self.chosen_round).intermediary_payoff

    def get_proportion(self):
        t = self.chosen_num_tickets
        prop = t / (t + 1)
        return round(prop, 2)

    def consent_error_message(self, value):
        if not value:
            return 'bạn phải chọn "đồng ý" để tiếp tục'

    consent = models.BooleanField(
        label="",
        choices=[
            (True, "CÓ, TÔI ĐỒNG Ý tham gia nghiên cứu này."),
            (False, "KHÔNG, TÔI KHÔNG ĐỒNG Ý tham gia nghiên cứu này."),
        ],
        widget=widgets.RadioSelect,
    )
    chosen_round = models.IntegerField()
    num_tickets_1 = models.IntegerField(min=0, max=20)
    num_tickets_2 = models.IntegerField(min=0, max=20)
    num_tickets_3 = models.IntegerField(min=0, max=20)
    num_tickets_4 = models.IntegerField(min=0, max=20)
    num_tickets_5 = models.IntegerField(min=0, max=20)
    ticket_price_1 = models.FloatField()
    ticket_price_2 = models.FloatField()
    ticket_price_3 = models.FloatField()
    ticket_price_4 = models.FloatField()
    ticket_price_5 = models.FloatField()
    ticket_chosen = models.IntegerField()
    price_chosen = models.FloatField()
    endowment = models.IntegerField()
    chosen_num_tickets = models.IntegerField()
    tail = models.BooleanField()
    personal_outcome = models.FloatField()
    intermediary_payoff = models.CurrencyField()

    # comprehension questions block

    # END OF comprehension questions block
