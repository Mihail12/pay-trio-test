import hashlib
import requests
import json


def get_sign(request, keys_required):
    secret = "RWg3gZmgHQnGNUN9wlDUaIIFOdgos4jkv"

    string_to_sign = ":".join(str(request[k]).encode("utf8") for k in keys_required) + secret

    sign = hashlib.md5(string_to_sign).hexdigest()

    return sign

def tip(data):
    request = {
        "shop_id":"305268",
        "amount": data.amount,
        "payway": "payeer_usd",
        "currency": data.currency,
        "shop_invoice_id":'100dfs0d0fsd0g0sdf0sdfs01',
        "description":data.description,
        }
    keys_sorted = ("amount", "currency", "shop_id",  "shop_invoice_id")
    return (request, get_sign(request, keys_sorted))

def post_invoice_API(data):
    request = {
        "shop_id":constants.shop_id,
        "amount": data.amount,
        "payway": "payeer_eur",
        "currency": data.currency,
        "shop_invoice_id":'101',
        "description":data.description,
        }
    keys_sorted = ('amount', 'currency', 'payway', 'shop_id', 'shop_invoice_id')

    sign = get_sign(request, keys_sorted)
    request['sign']=sign
    url = 'https://central.pay-trio.com/invoice'
    headers = {'content-type': "application/json"}
    r = requests.post(
        url,
        data=json.dumps(request),
        headers=headers ,
        verify=False)
    
    return json.loads(r.text)
