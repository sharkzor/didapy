### improve list:
# functie maken voor connectie object naar swis met username/ww
# functies aanpassen dat ze geen userid/ww pakken maar swis object

import requests
from orionsdk import SwisClient
from datetime import datetime, timedelta

requests.packages.urllib3.disable_warnings()

def suspress_node(hostname, username, password, nodename, begin, end):

    swis = SwisClient(hostname, username, password)
    results = swis.query('SELECT Uri, Caption FROM Orion.Nodes WHERE Caption = @caption', caption=nodename)
    if results['results']:
        Uri = results['results'][0]['Uri']
        caption = results['results'][0]['Caption']
        swis.invoke('Orion.AlertSuppression', 'SuppressAlerts', [Uri], begin, end)
        print('Done...' + nodename + 'will be silenced until ' + end.strftime("%d/%m/%Y, %H:%M:%S") )
    else:
        print("Device doesn't Exist")

def unmute(hostname, username, password, nodename):

    swis = SwisClient(hostname, username, password)
    results = swis.query('SELECT Uri, Caption FROM Orion.Nodes WHERE Caption = @caption', caption=nodename)
    if results['results']:
        Uri = results['results'][0]['Uri']
        caption = results['results'][0]['Caption']
        swis.invoke('Orion.AlertSuppression', 'ResumeAlerts', [Uri])       

        print('Done... device' + nodename + ' is unmuted')
    else:
        print("Device doesn't Exist")

def sms_status_node(hostname, username, password, nodename, sms):
    swis = SwisClient(hostname, username, password)
    results = swis.query('SELECT Uri, Caption FROM Orion.Nodes WHERE Caption = @caption', caption=nodename)
    uri = results['results'][0]['Uri']
    print(uri)
    swis.update(uri + '/CustomProperties', no_sms=sms)
    obj = swis.read(uri + '/CustomProperties')
    print (obj)

def sms_status_if(hostname, username, password, interface, sms, nodename="empty"):
    swis = SwisClient(hostname, username, password)
    if nodename == "empty":
       results = swis.query('SELECT Uri AS Uri FROM Orion.NPM.Interfaces WHERE Caption Like @caption', caption=interface)
    else:
       results = swis.query('SELECT i.Uri AS Uri FROM Orion.Nodes n JOIN Orion.NPM.Interfaces i ON n.NodeID = i.NodeID WHERE i.Caption = @icaption AND n.Caption = @ncaption', icaption=interface, ncaption=nodename)
    
    uri = results['results'][0]['Uri']
    print(uri)
    swis.update(uri + '/CustomProperties', no_sms_interface=sms)
    obj = swis.read(uri + '/CustomProperties')
    print (obj)
    
def set_nosms_ifall(hostname, username, password):
    swis = SwisClient(hostname, username, password)
    results = swis.query('SELECT Uri FROM Orion.NPM.Interfaces WHERE Caption LIKE \'%#NOSMS%\' ')
    urilijst = []
    for x in results['results']:
        swis.update(x['Uri'] + '/CustomProperties', no_sms_interface=1)
        obj = swis.read(x['Uri'] + '/CustomProperties')
        print(obj)

def connect_sw(hostname, username, password):
     requests.packages.urllib3.disable_warnings()
     swis = SwisClient(hostname, username, password)
     return swis

#requests.packages.urllib3.disable_warnings()

def main():
    hostname = 'monitor.vlkintern.nl'
    username = 'solarapi'
    password = 'SOtl#TjWJe8inqG'
    node = 'mst-mrb-01'
    interface = 'ether1'
    sms = "1"
    begin = datetime.utcnow()
    end = begin + timedelta(days=1)
    #suspress_node(hostname, username, password, node, begin, end)
    #unmute(hostname, username, password, node)
    #sms_status(hostname, username, password, node, sms)
    #swiss = connect_sw(hostname, username, password)
    #sms_status_if(hostname, username, password, interface, sms, node)
    set_nosms_ifall(hostname, username, password)

if __name__ == '__main__':
    main()
