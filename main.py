# Import required urllib and bs4 modules along with module ssl
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def follow_url(url, count, position, context):
    for i in range(count):
        html = urllib.request.urlopen(url, context=context).read()
        soup = BeautifulSoup(html, 'html.parser')
        print("Retrieving: " + url)
        tags = soup('a')
        url = tags[position - 1].get("href", None)


url = input('Enter URL: ')
position = int(input("Enter position: "))
count = int(input("Enter count: ")) + 1
follow_url(url, count, position, ctx)
