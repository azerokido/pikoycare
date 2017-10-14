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
    nume = parameters.get("number")

    if num >= 0 and num <= 100:
    speech = "The fee for the amount of" , num , "is PHP 2.00"
    elif num >= 101 and num <= 300:
    speech = "The fee for the amount of",  num , "is PHP 3.00"
    elif num >= 301 and num <= 500:
    speech ="The fee for the amount of",  num , "is PHP 8.00"
    elif num >= 501 and num <= 700:
    speech = "The fee for the amount of",  num , "is PHP 10.00","\n","Discount is 1.00"
    else:
    speech = num

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        # "contextOut": [],
        "source": "webhook sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=True, port=port, host='0.0.0.0')
