import json
import time
import requests
import datetime
import git
from requests.packages.urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter


def task():
    api_json = "api.json"
    api_data = open(api_json, 'r')
    api_url = json.load(api_data)
    url = (api_url["url"])
    status_json = "status-json.json"
    before_data = open(status_json, 'r')
    json_before_data = json.load(before_data)
    status_before_data = (json_before_data["status"])
    before_datetime_y = json_before_data["changeDateTime"]["y"]
    before_datetime_m = json_before_data["changeDateTime"]["m"]
    before_datetime_d = json_before_data["changeDateTime"]["d"]
    before_datetime_H = json_before_data["changeDateTime"]["H"]
    before_datetime_M = json_before_data["changeDateTime"]["M"]
    before_datetime_S = json_before_data["changeDateTime"]["S"]

    retries = Retry(total=10000,
                backoff_factor=10,
                status_forcelist=[ 500, 502, 503, 504 ])

    s = requests.Session()
    s.mount('https://', HTTPAdapter(max_retries=retries))
    file_data = s.get(url)
    json_data = json.loads(file_data.text)
    status_data = (json_data["members"])

    dt_now = datetime.datetime.now()
    dt_now_ = dt_now.replace(microsecond = 0)
    dt_now_text = dt_now.strftime('%Y年%m月,%d %H:%M:%S 更新')

    if status_data:
        status = "Online"
        if status_before_data == "Online":
            timelag = dt_now_  - datetime.datetime(year=before_datetime_y, month=before_datetime_m, day=before_datetime_d, hour=before_datetime_H, minute=before_datetime_M, second=before_datetime_S)
            y = before_datetime_y
            m = before_datetime_m
            d = before_datetime_d
            H = before_datetime_H
            M = before_datetime_M
            S = before_datetime_S
        else:
            timelag = 0
            y = dt_now.year
            m = dt_now.month
            d = dt_now.day
            H = dt_now.hour
            M = dt_now.minute
            S = dt_now.second
    else:
        status = "Offline"
        if status_before_data == "Offline":
            timelag = dt_now_  - datetime.datetime(year=before_datetime_y, month=before_datetime_m, day=before_datetime_d, hour=before_datetime_H, minute=before_datetime_M, second=before_datetime_S)
            y = before_datetime_y
            m = before_datetime_m
            d = before_datetime_d
            H = before_datetime_H
            M = before_datetime_M
            S = before_datetime_S
        else:
            timelag = 0
            y = dt_now.year
            m = dt_now.month
            d = dt_now.day
            H = dt_now.hour
            M = dt_now.minute
            S = dt_now.second
    str_json = {
        "status": status,
        "changeDateTime": {
            "y": y,
            "m": m,
            "d": d,
            "H": H,
            "M": M,
            "S": S
        },
        "timeLag": timelag,
        "upDateTime": {
            "y": dt_now.strftime('%Y'),
            "m": dt_now.strftime('%m'),
            "d": dt_now.strftime('%d'),
            "H": dt_now.strftime('%H'),
            "M": dt_now.strftime('%M'),
            "S": dt_now.strftime('%S')
        }
    }
    with open(status_json, 'w') as f:
        str_ = json.dumps(str_json, default=str)
        f.write(str_)

    repo = git.Repo("")
    repo.git.add(status_json)
    repo.index.commit("update")
    origin = repo.remote(name='origin')
    origin.push()

    print("出力しました。" + status + "、" + dt_now_text)


while True:
    task()
    time.sleep(60)
