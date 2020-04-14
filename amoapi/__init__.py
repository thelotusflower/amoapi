import sys
import logging

from .settings import settings as amo_settings
from .api import *
from .apimodels import *
from . import fields

__all__ = [
    'BaseCompany', 'BaseContact', 'BaseLead', 'amo_settings', 'AmoApi', 'ContactNote', 'ContactTask',
    'LeadNote', 'LeadTask', 'fields',
]

logger = logging.getLogger('amoapi')

if not logger.handlers:
    formatter = logging.Formatter(
        '%(asctime)s.%(msecs)d %(levelname)s: %(message)s', '%Y-%m-%d %H:%M:%S'
    )
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(formatter)
    handler.setLevel(logging.DEBUG)
    logger.addHandler(handler)
