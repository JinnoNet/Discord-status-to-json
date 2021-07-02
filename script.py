import json
import time
import requests
import datetime
import git

def task():
    api_json = "api.json"
    api_data = open(api_json, 'r')
    api_url = json.load(api_data)
    url = (api_url["url"])
    status_json = "status-json.json"
    before_data = open(status_json, 'r')
    json_before_data = json.load(before_data)
    status_before_data = (json_before_data["status"])
    long_data = (json_before_data["duration"])

    session = requests.Session()
    file_data = session.get(url)
    json_data = json.loads(file_data.text)
    status_data = (json_data["members"])

    dt_now = datetime.datetime.now()
    dt_now_text = dt_now.strftime('%Y年%m月,%d %H:%M:%S 更新')

    if status_data:
        status = "Online"
        if status_before_data == "Online":
            duration = long_data + 1
        else:
            duration = 0
    else:
        status = "Offline"
        if status_before_data == "Offline":
            duration = long_data + 1
        else:
            duration = 1

    str_json = {
        "status": status,
        "duration": duration,
        "date": {
            "y": dt_now.strftime('%Y'),
            "m": dt_now.strftime('%m'),
            "d": dt_now.strftime('%d'),
            "H": dt_now.strftime('%H'),
            "M": dt_now.strftime('%M'),
            "S": dt_now.strftime('%S')
        }
    }
    with open(status_json, 'w') as f:
        json.dump(str_json, f)
    f.close

    repo = git.Repo("")
    repo.git.add(status_json)
    repo.index.commit("update")
    origin = repo.remote(name='origin')
    origin.push()

    print("出力しました。" + status + "、" + str(duration) + "時間前、" + dt_now_text)

while True:
    task()
    time.sleep(3600)

