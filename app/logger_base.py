from flask import *
import logging as log

log.basicConfig(
    level=log.DEBUG,
    format='%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s',
    datefmt='%I:%M:%S %p',
    handlers=[
        # log.FileHandler(url_for('static', filname='utils/data.log')),
        log.FileHandler('./app/static/utils/data.log'),
        log.StreamHandler()
    ]
)

if __name__ == '__main__':
    log.debug('Mensaje nivel DEBUG')
    log.info('Mensaje nivel INFO')
    log.warning('Mensaje nivel WARNING')
    log.error('Mensaje nivel ERROR')
    log.critical('Mensaje nivel CRITICAL')