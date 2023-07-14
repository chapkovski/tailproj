from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import json
import logging

PRODUCER = "P"
INTERPRETER = "I"


class Q(Page):
    form_model = "player"
    form_fields = [
        "age",
        "gender",
        "marital",
        "employment",
        "income",
      
    ]

 


page_sequence = [
    Q,
  
    ]
