import logging
# from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import time

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# roll over after 2KB, and keep backup logs app.log.1, app.log.2, etc.
# handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# s, m, h, d, midnight, w0(stands for Monday)
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello, world!')
    time.sleep(5)
