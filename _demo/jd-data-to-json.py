import time
import json
import urllib3
http = urllib3.PoolManager()
import uuid


BASE_URL = '//api.m.jd.com/client.action'


def getData():
    r = http.request('POST', BASE_URL, fields={
        'functionId': 'qryCompositeMaterials',
        'body': json.dumps({
            'activityId': 'Conf.activityId',
            'pageId': 'Conf.pageId',
            't': time.time(),
            'qryParam': json.dumps([]),
            'previewTime': '',
            'geo': {
                'lng': '',
                'lat': ''
            }
        }),
        'clientVersion': '1.0.0',
        'client': 'wh5',
        'uuid': uuid.uuid1(),
        'area': ''
    })
    
    print(r.status, r.data)


getData()
