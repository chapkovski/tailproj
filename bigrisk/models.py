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


author = 'Philipp Chapkovski, UBonn'

doc = """
Tail, no median lottery project
"""


class Constants(BaseConstants):
    name_in_url = 'bigrisk'
    players_per_group = None
    num_rounds = 10
    POSITIVE_ENDOWMENT=10
    NEGATIVE_ENDOWMENT=200

    # READ THE DATA
    path_to_data='./data/' 

    with open(f'{path_to_data}lotteries.csv', 'r') as f:
        reader = csv.DictReader(f)
        lotteries=[i.get('header') for i in reader]

    with open(f'{path_to_data}tickets.csv', 'r') as f:
        reader = csv.DictReader(f)
        tickets=list(reader)
        print(tickets)
class Subsession(BaseSubsession):
    def creating_session(self):
        neg=self.session.config.get('negative')
        tail=self.session.config.get('tail')
        endowment=Constants.NEGATIVE_ENDOWMENT if neg else Constants.POSITIVE_ENDOWMENT
        if tail:
            lotteries=Constants.lotteries.copy()
        else:
            lotteries=Constants.lotteries.copy()[:4]
        for p in self.get_players():
            p.endowment=endowment
            p.tail=tail
            p.participant.vars['lotteries']=lotteries

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_tickets=models.IntegerField(label='How many tickets you would like to buy?',
                                    min=0, max=20)
    endowment=models.IntegerField()
    tail=models.BooleanField()