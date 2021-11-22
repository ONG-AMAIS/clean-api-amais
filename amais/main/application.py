from flask import Flask
from amais.main.configs.constants import TAMPLATE_FOLDER

app = Flask(__name__, template_folder=TAMPLATE_FOLDER)
