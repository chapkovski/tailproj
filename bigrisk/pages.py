from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class CQPage(Page):
    def js_vars(self):
        return dict(endowment=self.player.endowment)
    def is_displayed(self):
        return self.round_number == 1
    
class ShowTails(Page):
    def is_displayed(self):
        return self.round_number == 1


class BuyingTickets(Page):
    def js_vars(self):
        p=self.player
        prices=[getattr(p, f'ticket_price_{i}') for i in range(1,6)]
        probs=[{int(i.get('n')):i.get('formatted_portion')} for i in Constants.tickets]
        return dict(prices= prices,probs=probs, endowment=p.endowment,
                    negative=self.session.config.get('negative'))
    def vars_for_template(self):
        p=self.player
        form = self.get_form()
        fdata = []
       
        for i, f in enumerate(form, start=1):
            
            ticket_price=getattr(p, f'ticket_price_{i}')
            t = {'field': f,
                 'label': f'If the ticket price is <b>${ticket_price}</b>, I will purchase:',
                 }
            fdata.append(t)

        return dict(data_to_show=fdata)
    form_model = 'player'
    def before_next_page(self):
        p=self.player
        p.chosen_num_tickets = getattr(p, f'num_tickets_{p.ticket_chosen}')
    form_fields = ['num_tickets_1','num_tickets_2','num_tickets_3','num_tickets_4','num_tickets_5']
class Results(Page):
    pass
    
page_sequence = [CQPage,
    ShowTails,
                 BuyingTickets,
                 Results]
