import BitlyModule
import os
from urllib.parse import urlparse
from dotenv import load_dotenv

#   Функцию создал, но не совсем понимаю, как ее лучше использовать, 
#   так как для expand ulr нужнен запаршенный url, 
#   ведь протоколы http/https ломают expand по api запросу
def is_bitlink(url):
    parsedUrl = urlparse(url)
    if parsedUrl.hostname == 'bit.ly':
        return True
    else:
        return False

if __name__ == '__main__':
    load_dotenv()
    user = BitlyModule.BitlyAPI(os.environ['API_KEY'])
    print("Enter your link")
    url = input()
    parsedUrl = urlparse(url)
    if parsedUrl.hostname == 'bit.ly':
        user.expandBitlink(parsedUrl.hostname+parsedUrl.path)
    else:
        user.createBitlink(url)