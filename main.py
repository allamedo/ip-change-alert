import public_ip as ip
from tinydb import TinyDB, Query
import telegram
import time, os

db = TinyDB('/tmp/ip_database.json')

def get_public_ip():
    return ip.get()

def get_last_ip_address():
    Ip = Query()
    result = db.search(Ip.ip_address.exists())
    if result:
        result.sort(key=lambda x: x['timestamp'], reverse=True)
        return result[0]['ip_address']
    else:
        return None

def add_ip_to_database(ip_address):
    timestamp = int(time.time())
    Ip = Query()
    existing_ip = db.get(Ip.ip_address == ip_address)
    last_ip_address = get_last_ip_address()
    if existing_ip:
        db.update({'timestamp': timestamp}, Ip.ip_address == ip_address)
        return False
    else:
        db.insert({'ip_address': ip_address, 'timestamp': timestamp})
        if ip_address != last_ip_address:
            telegram.send_message(f"{os.uname()[1]} {ip_address}","") 
        return ip_address != last_ip_address

def main():
    ip_address = get_public_ip()
    add_ip_to_database(ip_address)
    print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {os.uname()[1]} Current IP -> {ip_address}") 

if __name__ == "__main__":

    while(True):
        main()
        time.sleep(60*30)