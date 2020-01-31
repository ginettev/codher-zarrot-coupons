from flask import Blueprint
from flask import render_template
from flask import jsonify, Response
from flask import current_app as app
import json
import os


coupons = Blueprint('coupons', __name__)


@coupons.route('/')
def index():
    # with open('zarrot/resources/coupons.json') as json_file:
    #     data = json.load(json_file)
    #     print(rodata)
    # return "CouponController"
    filename = os.path.join(app.static_folder, '', 'coupons.json')
    print(filename)
    with open(filename) as coupons_file:
        data = json.load(coupons_file)
        print(data)
    return jsonify(data), 200, {'Content-Type': 'application/json; charset=utf-8'}
