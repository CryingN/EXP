import requests

def get(url, get_data=""):
    
    if "http" in url:
        data = requests.get(url + "?" + get_data)
    else:
        try:
            data = requests.get("https://" + url + "?" + get_data)
        except:
            data = requests.get("http://" + url + "?" + get_data)
    
    return data.text

def post(url, post_data="", get_data=""):
    payload = {}
    for i in post_data.split("&"):
        a, b = i.split("=")
        payload[a] = b
    if "http" in url:
        data = requests.post(url + "?" + get_data, data=payload)
    else:
        try:
            data = requests.post("https://" + url + "?" + get_data, data=payload)
        except:
            data = requests.post("http://" + url + "?" + get_data, data=payload)
    return data.text


