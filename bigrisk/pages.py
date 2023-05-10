from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class ShowTails(Page):
    def is_displayed(self):
        return self.round_number == 1


class BuyingTickets(Page):
    form_model = 'player'
    form_fields = ['num_tickets']


page_sequence = [ShowTails,
                 BuyingTickets]
