import requests, time, os, public_ip

import secret

read_url = "https://api.thingspeak.com/channels/2569331/feeds.json?api_key=" + secret.read_key + "&results=1"


while "stop" not in os.listdir():
    record = requests.get(read_url).json()['feeds'][0]
    # print(requests.get(read_url).json())
    data = {
        "req_res_flag" : int(record['field1'])
    }
    # print(data)
    if data["req_res_flag"] == 0:
        # print("Got no requests")
        time.sleep(20)
    elif data["req_res_flag"] == 2:
        time.sleep(20)
        ip_fields = "".join([f"&field{x + 2}={y}" for x,y in enumerate(public_ip.get().split('.'))])
        # ip_fields = "".join([f"&field{x + 2}={y}" for x,y in enumerate("192.168.0.12".split('.'))])
        write_url = "https://api.thingspeak.com/update?api_key=" + secret.write_key + "&field1=0" + ip_fields
        
        while not(int(requests.get(write_url).json()) != 0):
            time.sleep(1)
    else:
        time.sleep(20)

