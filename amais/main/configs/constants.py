from dotenv import dotenv_values

config = dotenv_values('.env')


DATABASE = {'user': config['DB_USER'],
            'password': config['DB_PASSWORD'],
            'host': config['DB_HOST'],
            'port': config['DB_PORT'],
            'db_name': 'db_amais'}
