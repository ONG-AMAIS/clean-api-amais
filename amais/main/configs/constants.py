from dotenv import dotenv_values
import os

config = dotenv_values('.env')


PORT = int(config['PORT']) or 5000

SERVER_BASE_URL = config['SERVER_BASE_URL']

ALLOW_DEBUG = config['FLASK_ENV'] == 'development'

UPLOAD_FOLDER = 'uploads/certificates/'

ROOT_DIR = os.path.abspath(os.curdir)

TAMPLATE_FOLDER = '{root_dir}/{template_folder}'.format(
    root_dir=ROOT_DIR, template_folder=UPLOAD_FOLDER)


ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg'}

DATABASE = {'user': config['DB_USER'],
            'password': config['DB_PASSWORD'],
            'host': config['DB_HOST'],
            'port': config['DB_PORT'],
            'db_name': 'db_amais'}
