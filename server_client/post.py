import urllib.request, json
import time
import random

if __name__ == '__main__':
    url = "http://localhost:1337"
    method = "POST"
    obj = {
        "smell" : "400",
        "IP" : "172.20.11.202",
        "Button" : "ButtonA",
    }
    #外部jsonファイルを読み込む場合
    f = open("data.json", 'r')
    obj = json.load(f) #JSON形式で読み込む
    json_data = json.dumps(obj).encode("utf-8")
    
    headers = {"Content-Type" : "application/json"}
    num =0

    print(obj[0]['smell'])
    while num<10:
        num+=1
        time.sleep(1)
        obj[0]['smell'] = int(random.randrange(100))
        obj[0]['count'] = int(random.randrange(10))
        json_data = json.dumps(obj).encode("utf-8")


        request = urllib.request.Request(url, data=json_data, headers=headers, method=method)
        with urllib.request.urlopen(request) as response:
            response_body = response.read().decode("utf-8")
        

        #result_objs = json.loads(response_body.split('\n')[0])
        #for result_obj in result_objs["values"]:
            #print("{0:<10}{1}".format(result_obj["view_counter"], result_obj["title"]))
