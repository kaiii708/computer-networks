from flask import Flask
from flask import request
from flask_cors import cross_origin
import requests

app = Flask(__name__)


def get_proxy_endpoint(plan):
    if plan == "The Dalles, Oregon, North America":
        return 'socks4://34.168.83.29:8080'
    elif plan == "Changhua, Taiwan":
        return 'socks4://34.84.97.65:8080'
    else:
        return 'socks4://34.81.26.49:8080'


@app.route('/')
@cross_origin()
def hello():
    plan = request.headers.get('plan')
    print(plan)
    proxy_endpoint = get_proxy_endpoint(plan)
    print(proxy_endpoint)
    #resp = requests.get('http://google.com/')
    resp = requests.get('https://www.google.com/',
                        proxies=dict(http=proxy_endpoint,
                                     https=proxy_endpoint))

    return resp.text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
