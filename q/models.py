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

from . import choices
author = 'Tên của bạn'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'q'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
        # DEMOGRAPHICS
    
    age = models.StringField(label='Tuổi của bạn là?', choices=choices.AGE_CHOICES, widget=widgets.RadioSelect)
    education = models.StringField(
        label="bằng cấp (học vấn) cao nhất mà bạn đã từng học?",
        choices=choices.EDUCATION_CHOICES, widget=widgets.RadioSelect)
    gender = models.StringField(label='Giới tính của bạn?',
                                 choices=choices.GENDER_CHOICES, widget=widgets.RadioSelect)
    marital = models.StringField(label='Tình trạng hôn nhân của bạn?',
                                  choices=choices.MARITAL_CHOICES, widget=widgets.RadioSelect)
    employment = models.StringField(label='Tình trạng việc làm hiện tại của bạn?',
                                     choices=choices.EMPLOYMENT_CHOICES, widget=widgets.RadioSelect)
    income = models.StringField(
        label="Thu nhập hàng năm của gia đình bạn là?",
        choices=choices.INCOME_CHOICES,
        widget=widgets.RadioSelect()
    )
 
    