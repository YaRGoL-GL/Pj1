
'''
logging.basicConfig(level=logging.DEBUG)
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('computer - ded 💀')
logging.debug2('debug2')
logging.info2('info2')
'''
''' Время по секундам
import logging
logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='a', format='Logging messages:%(asctime)s:%(levelname)s - (name)s')
logging.debug('debug')
logging.info('info')
logging.debug('debug2 - warning')
logging.info('info2 - critical error')
'''
'''
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='logs.log',
                    filemode='a',
                    format='Logging messages:%(asctime)s:'
                           '%(levelname)s - (name)s')
try:
    print(10/0)
    print('lst_ *3 - ', lst_ *3)
except Exception:
    logging.exception('Exception')
'''
'''
y = 5 * 5 + 10
print(y == 25)
if 5 * 5 + 10 ==35:
    print('True')
assert 5 * 5 + 10 == 36, 'warning_warning'
'''
