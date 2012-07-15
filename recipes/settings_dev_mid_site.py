from foundry import settings as foundry_settings

from recipes.settings import *


FOUNDRY['layers'] = ('mid', 'basic',)

foundry_settings.compute_settings(sys.modules[__name__])
