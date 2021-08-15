import requests
import time
from datetime import datetime
from config import USERNAME, PASSWORD, HOSTNAME


def get_IPV6():
    url = 'http://v6.ipv6-test.com/api/myip.php'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return False
    

def log_ip(response):
    date = datetime.today().strftime('%Y-%m-%d-%H:%M:%S')
    
    with open('IP_LOG.txt', 'a') as f:
        f.write("\n")
        f.write("{} / {}".format(date, response.strip()))
        


def request_update(ipv6):
    url = 'http://{}:{}@dynupdate.no-ip.com/nic/update?hostname={}&myipv6={}'.format(USERNAME, PASSWORD, HOSTNAME, ipv6)
    response = requests.get(url)
    if "good" in response.text:
        print(response.text)
        log_ip(response.text)


def main():
    while True:
        print("Atualizando...")
        IPV6 = get_IPV6()
        if IPV6:
            request_update(IPV6)
        time.sleep(600)


if __name__ == '__main__':
    main()