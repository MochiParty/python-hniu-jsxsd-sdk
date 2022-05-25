import logging

logger = logging.getLogger('main')
logger.setLevel(level=logging.DEBUG)

# Handler
handler = logging.FileHandler('log.log')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
