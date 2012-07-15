from foundry import settings as foundry_settings

from recipes.settings_qa_base import *


FOUNDRY['layers'] = ('smart', 'mid', 'basic',)

foundry_settings.compute_settings(sys.modules[__name__])
