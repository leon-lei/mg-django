from tutorial.settings.base import *

# Override base.py settings here

try:
    from tutorial.settings.local import *
except:
    # Can tell user to create local.py
    pass