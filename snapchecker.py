import requests
import threading
import thread
class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    HEADER = '\033[95m'


def maino():
    face = """""
      ____          _          _   ____        
     / ___|___   __| | ___  __| | | __ ) _   _ 
    | |   / _ \ / _` |/ _ \/ _` | |  _ \| | | |
    | |__| (_) | (_| |  __/ (_| | | |_) | |_| |
     \____\___/ \__,_|\___|\__,_| |____/ \__, |
                                         |___/ 
     ____                       _              _   _____ 
    |  _ \ _ __ ___   __ _ _ __| | ____      _| |_|___ / 
    | | | | '_ ` _ \ / _` | '__| |/ /\ \ /\ / / __| |_ \ 
    | |_| | | | | | | (_| | |  |   <  \ V  V /| |_ ___) |
    |____/|_| |_| |_|\__,_|_|  |_|\_\  \_/\_/  \__|____/ 
    
    ================ SnapChatChecker =====================
    
        """
    print(bcolors.HEADER + face)
    ask = raw_input(bcolors.OKBLUE + "Enter UserList: ")
    lopi = open(ask, "r")


    headers = {
    "User-Agent": "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Referer": "https://accounts.snapchat.com/",
    "Cookie": "xsrf_token=a-mMpU6dwym43afgEibJnw; web_client_id=12966659-1ddb-4d0b-8c4c-e39610ddf0f8; _sca={%22cid%22:%2235552e94-28cd-46fc-bf26-b220994ae1d7%22%2C%22token%22:%22v1.key.2018-05-23_8lt9BOpW.iv.ykqLG02DA/OtGORO.j0/QFbsqE82bUtb8Qa0jO6//zEXiS4ZQT4tYissWzZ42fsdCsi8fl7Hy2bEHDm3hs1Li8jciZDbraK3xOUQoTk21tiPgsPcMQvecgafXovbGZOKh%22}; _scid=f2fd66fb-9e11-44d8-a36f-75d807b8d061; sc_at=v2|H4sIAAAAAAAAADNITjFJNjcz100zNjTVNTE2M9RNtDAz1k1NtjAzMU01TElKSqoxNDKwMjQ1NQZKA0VrkJgGAGh4Yl9AAAAA; _sctr=1|1553400000000; oauth_client_id=scan",
    "Connection": "close",
    "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
    }
    url = "https://accounts.snapchat.com/accounts/get_username_suggestions"
    for rew in lopi:
        data = "requested_username="+rew+"&xsrf_token=a-mMpU6dwym43afgEibJnw"
        url = "https://accounts.snapchat.com/accounts/get_username_suggestions"

        request = requests.post(url, headers=headers, data=data)
        po = request.content
        if "OK" in po:
            print( bcolors.OKGREEN + "Available -----> "+rew)
        elif "TAKEN" in po:
            print(bcolors.FAIL + "Taken -----> "+rew)
        else:
            print("unknown error for user -----> " + rew)

t1 = threading.Thread(target=maino())
t1.start()
