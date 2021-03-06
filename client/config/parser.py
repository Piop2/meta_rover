from configparser import ConfigParser

PATH = 'config.ini'

parser = ConfigParser()
with open(PATH, 'r') as f:
    parser.read_file(f)

server_ip = parser['SERVER']['ip']
server_port = int(parser['SERVER']['port'])
