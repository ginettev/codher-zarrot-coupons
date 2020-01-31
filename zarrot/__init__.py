from flask import Flask
from zarrot.main.controllers import main
from zarrot.coupons.controllers import coupons

app = Flask(__name__, static_folder='resources')

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(coupons, url_prefix='/coupons')
