#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):
    if req.get("result").get("action") != "sample.fee":
        return {}
    result = req.get("result")
    parameters = result.get("parameters")
    zone = parameters.get("number")

    cost = {'Europe':100, 'North America':200, 'South America':300, 'Asia':400, 'Africa':500}

    speech = "show me the remittance fee of 1000"
    
    num = 600
    if num >= 0 and num <= 100:
    print("The fee for the amount of",  num , "is PHP 2.00")
    elif num >= 101 and num <= 300:
    print("The fee for the amount of",  num , "is PHP 3.00")
    elif num >= 301 and num <= 500:
    print("The fee for the amount of",  num , "is PHP 8.00")
    elif num >= 501 and num <= 700:
    print("The fee for the amount of",  num , "is PHP 10.00","\n","Discount is 1.00")
    else:
    print(num)

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "apiai-onlinestore-shipping"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
