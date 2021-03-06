#! /usr/bin/env python

"""Gets image name by id of existing container and start new same container"""

import click
import json
import requests
from requests.auth import HTTPBasicAuth

@click.command()
@click.argument('id')
def main(id):
    try:
        req=requests.post("http://opentsp-gateway-eureka:8761/ui/api/containers/"+id+"/scale", auth=HTTPBasicAuth('admin', 'password'))
        print(req.text)
    except Exception, e:
        print "can't schedule container {0} ".format(e)

if __name__ == '__main__':
    main()