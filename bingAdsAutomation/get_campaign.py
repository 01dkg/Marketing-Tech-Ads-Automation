import logging
import time
from googleads import adwords

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)


PAGE_SIZE = 100
