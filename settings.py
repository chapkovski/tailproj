from os import environ

SESSION_CONFIGS = [
    dict(
        name='median_pos',
        display_name="Median, positive",
        num_demo_participants=3,
        tail=False,
        negative=False,
        app_sequence=['bigrisk']
    ),
    dict(
        name='median_neg',
         display_name="Median, negative",
        num_demo_participants=3,
        tail=False,
        negative=True,
        app_sequence=['bigrisk']
    ),
    dict(
        name='tail_pos',
         display_name="Tail, positive",
        num_demo_participants=3,
        tail=True,
        negative=False,
        app_sequence=['bigrisk']
    ),
    dict(
        name='tail_neg',
         display_name="Tail, negative",
        num_demo_participants=3,
        tail=True,
        negative=True,
        app_sequence=['bigrisk']
    ),
        dict(
        name='post_q',
         display_name="Post-experimental questionnaire",
        num_demo_participants=1,
        
        app_sequence=['q']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = False

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'zx$4no)b1ddh-$tzmb5%ubzccw3^d$v#un%b(-gw6+^u-j@v+0'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
