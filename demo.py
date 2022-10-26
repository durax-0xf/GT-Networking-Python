import requests

def get_info():
    url = "https://www.growtopia2.com/growtopia/server_data.php"
    headers = {
    'User-Agent': 'UbiServices_SDK_2019.Release.27_PC64_unicode_static'
    }
    response = requests.get(url, headers=headers)
    out_ip = str(response.content)[9:24]
    out_port = str(response.content)[33:38]
    return(out_ip, out_port)


