from amais.main.application import app
from amais.main.configs.constants import DATABASE
from flask_sqlalchemy import SQLAlchemy


connection_string = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}'.format(
    user=DATABASE['user'], password=DATABASE['password'], host=DATABASE['host'], port=DATABASE['port'], db_name=DATABASE['db_name'])

app.config['SQLALCHEMY_DATABASE_URI'] = connection_string
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
