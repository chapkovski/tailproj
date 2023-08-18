from otree.api import Currency as c, currency_range
from ._builtin import Page as oTreePage, WaitPage
from .models import Constants


class Page(oTreePage):
    instructions_path = "bigrisk/includes/instructions.html"
    instructions = False

    def get_context_data(self, **context):
        r = super().get_context_data(**context)
        r["instructions_google_doc"] = self.session.config.get("instructions_path")
        r["maxpages"] = self.participant._max_page_index
        r["page_index"] = self._index_in_pages
        r[
            "progress"
        ] = f"{int(self._index_in_pages / self.participant._max_page_index * 100):d}"
        r["instructions"] = self.instructions

        return r


class ConsentPage(Page):
    def is_displayed(self):
        return self.round_number == 1

    form_model = "player"
    form_fields = ["consent"]

    def vars_for_template(self):
        return dict(consent_form_path=self.session.config.get("consent_form_path"))


class CQPage(Page):
    instructions = True

    def js_vars(self):
        return dict(
            endowment=self.player.endowment,
            num_rounds=Constants.num_rounds,
            negative=self.session.config.get("negative"),
        )

    def is_displayed(self):
        return self.round_number == 1


class ShowTails(Page):
    instructions = True

    def is_displayed(self):
        return self.round_number == 1


class BuyingTickets(Page):
    instructions = True

    def js_vars(self):
        p = self.player
        prices = [getattr(p, f"ticket_price_{i}") for i in range(1, 6)]
        probs = [
            {int(i.get("n")): i.get("formatted_portion")} for i in Constants.tickets
        ]
        return dict(
            prices=prices,
            probs=probs,
            endowment=p.endowment,
            negative=self.session.config.get("negative"),
        )

    def vars_for_template(self):
        p = self.player
        form = self.get_form()
        fdata = []

        for i, f in enumerate(form, start=1):
            ticket_price = getattr(p, f"ticket_price_{i}")
            t = {
                "field": f,
                "label": f"If the ticket price is <b>${ticket_price}</b>, I will purchase:",
            }
            fdata.append(t)

        return dict(data_to_show=fdata)

    form_model = "player"

    def before_next_page(self):
        p = self.player
        p.chosen_num_tickets = getattr(p, f"num_tickets_{p.ticket_chosen}")
        perssign=-1 if self.session.config.get("negative") else +1
        p.intermediary_payoff= p.endowment- p.chosen_num_tickets * p.price_chosen + perssign*p.personal_outcome*p.get_proportion()
    form_fields = [
        "num_tickets_1",
        "num_tickets_2",
        "num_tickets_3",
        "num_tickets_4",
        "num_tickets_5",
    ]


class Results(Page):
    instructions = True

    def vars_for_template(self):
        negative=self.session.config.get("negative")
        perssign = "-" if negative else "+"
        return dict(negative=negative, perssign=perssign)


page_sequence = [
    # ConsentPage, CQPage, ShowTails,
    BuyingTickets,
    Results,
]
