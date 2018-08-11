# 13.10. Reading Configuration Files

from configparser import ConfigParser
cfg = ConfigParser()
cfg.read('config.ini')
# ['config.ini']
cfg.sections()
# ['installation', 'debug', 'server']
cfg.get('installation','library')
# '/usr/local/lib'
cfg.getboolean('debug','log_errors')

cfg.getint('server','port')
cfg.getint('server','nworkers')
print(cfg.get('server','signature'))


cfg.set('server','port','9000')
cfg.set('debug','log_errors','False')
import sys
cfg.write(sys.stdout)