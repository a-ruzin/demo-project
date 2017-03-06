import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename='example.log', level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.debug('Yahoo, we are here')
logging.info('Something happens')
logging.warning('Something suspicios happens')
logging.error('Error occurs')
logging.critical('AHHH!!! Is everything broken?')
