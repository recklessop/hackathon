#!/usr/bin/env python3

import requests
import json
import time
import unicornhat as unicorn
from datetime import datetime

zaUser = "justin@jpaul.me"
zaPass = "Zertodata1!"

api_url_base = "https://analytics.api.zerto.com"
api_token = ''

unicorn.set_layout(unicorn.AUTO)
unicorn.rotation(180)
unicorn.brightness(0.2)
width,height=unicorn.get_shape()

unicorn.set_pixel(0,0,255,255,255)
unicorn.show()

def za_authorize(Username, Password):
    api_url = '{0}/v2/auth/token'.format(api_url_base)
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    creds = dict(
        username=Username,
        password=Password
    )

    response = requests.post(api_url, headers=headers, data=json.dumps(creds))

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))["token"]
    else:
        return None

def za_get_vpgs_health(api_token):
    api_url = '{0}/v2/monitoring/vpgs'.format(api_url_base)
    headers = {'accept': 'application/json', 'Authorization': 'Bearer ' + api_token}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.loads(response.content.decode('utf-8'))
    else:
        return None

def draw_vpgs(healthy, warn, error):
    total = healthy + warn + error
    unicorn.clear()
    for y in range(height):
        for x in range(width):
            if error > 0:
               unicorn.set_pixel(x,y,255,0,0)
               error -= 1
            elif warn > 0:
                unicorn.set_pixel(x,y,255,255,0)
                warn -= 1
            elif healthy > 0:
                unicorn.set_pixel(x,y,0,255,0)
                healthy -= 1
    unicorn.show()

# main loop

while True:
    api_token = za_authorize(zaUser, zaPass)
    vpgs = za_get_vpgs_health(api_token)

    healthy = vpgs["healthyVpgsCount"]
    warning = vpgs["warnedVpgsCount"]
    error = vpgs["erroneousVpgsCount"]

    print(str(datetime.now()).split('.')[0])
    print("{} Errors, {} Warnings, {} Healthy".format(error, warning, healthy))
    draw_vpgs(healthy, warning, error)

    time.sleep(30)
