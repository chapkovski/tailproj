from os import environ
app_seq=['bigrisk','q']
SESSION_CONFIGS = [
    dict(
        name='median_pos',
        display_name="Median, positive",
        num_demo_participants=3,
        tail=False,
        negative=False,
        app_sequence=app_seq
    ),
    dict(
        name='median_neg',
         display_name="Median, negative",
        num_demo_participants=3,
        tail=False,
        negative=True,
        app_sequence=app_seq
    ),
    dict(
        name='tail_pos',
         display_name="Tail, positive",
        num_demo_participants=3,
        tail=True,
        negative=False,
        app_sequence=app_seq),
    dict(
        name='tail_neg',
         display_name="Tail, negative",
        num_demo_participants=3,
        tail=True,
        negative=True,
        app_sequence=app_seq
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
    consent_form_path='https://docs.google.com/document/d/e/2PACX-1vSvOVXHrwpn7EDQ0Rc4QuiP-wR3fqLjyPCReoXh0Sg1YDi9sXsFo3dX-bxmIbesDQ/pub',
    instructions_path='https://docs.google.com/document/d/e/2PACX-1vRDBR-WRDvhZ_SCzAh7VbdyTPpw7r_8aF7Ey3O6GQvKwBrzIhzDIz7kglABfXa16bKMuQJI72RT-a29/pub',
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)
ROOMS=[{"name": "room1", "display_name": "Experiment room 1",
          "participant_label_file":'_rooms/tail.txt',},
       {"name": "room2", "display_name": "Experiment room 2",
          "participant_label_file":'_rooms/tail.txt',}]
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
