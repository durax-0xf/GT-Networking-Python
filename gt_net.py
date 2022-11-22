import requests
import time

def get_info(ip=False, port=False):
    '''
    SERVER IP AND PORT
    ~~~~~~~~~~~~~~~~~~
    >>> get_info(ip=True)
    '213.179.209.168'     <- String
    >>> get_info(port=True)
    '17197'           <- String
    >>> get_info(ip=True, port=True)
    ('213.179.209.168', '17195')  <- Tuple


    Works by using the UbiServices User-Agent for headers
    "https://www.growtopia2.com/growtopia/server_data.php"
    'User-Agent': 'UbiServices_SDK_2019.Release.27_PC64_unicode_static'

    '''
    url = "https://www.growtopia2.com/growtopia/server_data.php"
    headers = {
    'User-Agent': 'UbiServices_SDK_2019.Release.27_PC64_unicode_static'
    }
    response = requests.get(url, headers=headers)
    if(ip==True and port==True):
        return str(response.content)[9:24], str(response.content)[33:38]
    elif(ip == True):
        return str(response.content)[9:24]
    elif(port == True):
        return str(response.content)[33:38]
    
    

def usr_count():
    '''
    ONLINE USER COUNT
    ~~~~~~~~~~~~~
    Returns online players for growtopia
    will return incorrect value if player count goes over 100k
    '''
    url = "https://growtopiagame.com/detail"
    response = requests.get(url)
    #this is beyond stupid btw and i cba to fix it
    return int(str(response.content)[18:23])


def server_status(monitoring = False):
    '''
    ~~~~~~~~~~~~~~~~
    Returns False If server is down
    Returns True If server is up

    Auto monitors server every 10 seconds if monitoring is True

    Server is considered to be down if playercount is lower than 130, due to devs
    (and server monitors?) showing up as online players
    '''
    while(monitoring == True):
        #usually there are some devs working on the game at any point when server is 'down'
        if(usr_count()<130): 
            return False
        else:
            return True
        time.sleep(10)
    else:
        if(usr_count()<130):
            return False
        else:
            return True
    
 
