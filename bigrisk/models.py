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

import random
author = 'Philipp Chapkovski, UBonn'

doc = """
Tail, no median lottery project
"""


class Constants(BaseConstants):
    name_in_url = 'bigrisk'
    players_per_group = None
    num_rounds = 10
    POSITIVE_ENDOWMENT = 10
    NEGATIVE_ENDOWMENT = 200
    price_ranges = ((0.01, 0.50), (0.50, 1.50),
                    (1.50, 2.75), (2.75, 5), (5, 10))
    # READ THE DATA
    path_to_data = './data/'

    with open(f'{path_to_data}lotteries.csv', 'r') as f:
        reader = csv.DictReader(f)
        lotteries = [i.get('header') for i in reader]

    with open(f'{path_to_data}tickets.csv', 'r') as f:
        reader = csv.DictReader(f)
        tickets = list(reader)
        print(tickets)


class Subsession(BaseSubsession):
    def creating_session(self):
        neg = self.session.config.get('negative')
        tail = self.session.config.get('tail')
        endowment = Constants.NEGATIVE_ENDOWMENT if neg else Constants.POSITIVE_ENDOWMENT
        if tail:
            lotteries = Constants.lotteries.copy()
        else:
            lotteries = Constants.lotteries.copy()[:4]
        for p in self.get_players():
            p.endowment = endowment
            p.tail = tail
            p.participant.vars['lotteries'] = lotteries
            for i  in range(1,6):
                prange=Constants.price_ranges[i-1]
                price=round(random.uniform(*prange),2)
                setattr(p, f'ticket_price_{i}', price)
            p.ticket_chosen=random.randint(1,5)
            p.price_chosen=getattr(p, f'ticket_price_{p.ticket_chosen}')


class Group(BaseGroup):
    pass


class Player(BasePlayer):
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
