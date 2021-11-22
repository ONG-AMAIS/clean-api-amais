from amais.main.server import app
from amais.main.configs.constants import ALLOW_DEBUG, PORT

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=ALLOW_DEBUG)
