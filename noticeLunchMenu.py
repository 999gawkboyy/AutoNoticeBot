import requests
import json
from datetime import datetime

KEY = "04078f259fa242e19b12198cf0e3cee8"

url = f"https://open.neis.go.kr/hub/mealServiceDietInfo"

params = {
    'KEY': KEY,
    'Type': 'json',
    'pIndex': '1',
    'pSize': '100',
    "ATPT_OFCDC_SC_CODE": "B10",
    'SD_SCHUL_CODE': '7010572',
    'MLSV_YMD': ''
}

def fn(res):
    for item in res:
        if item['MLSV_YMD'] == datetime.now().strftime('%Y%m%d'):
            return [v for i, v in enumerate(item['DDISH_NM'].replace("<br/>·", " ")[1:].split(' ')) if i & 1 == 0]
    return -1
        

def findTodaysLunch():
    params['MLSV_YMD'] = datetime.now().strftime("%Y%m")
    res = requests.get(url, params=params)
    return fn(json.loads(res.text)['mealServiceDietInfo'][1]['row'])