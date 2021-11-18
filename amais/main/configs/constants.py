from dotenv import dotenv_values

config = dotenv_values('.env')

PORT = int(config['PORT']) or 5000

ALLOW_DEBUG = config['FLASK_ENV'] == 'development'

DATABASE = {'user': config['DB_USER'],
            'password': config['DB_PASSWORD'],
            'host': config['DB_HOST'],
            'port': config['DB_PORT'],
            'db_name': 'db_amais'}
