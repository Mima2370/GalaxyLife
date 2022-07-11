import os
from flask import Flask

from api.api import routes

app = Flask(__name__)

app.register_blueprint(routes, url_prefix='/star')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    print(port)
    app.run(port=port, host='0.0.0.0', debug=True)
