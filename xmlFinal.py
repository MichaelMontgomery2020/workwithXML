import urllib.request
import urllib.parse
import urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# TEST: http://py4e-data.dr-chuck.net/comments_42.xml
# REAL: http://py4e-data.dr-chuck.net/comments_1096789.xml

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    url = address
    print("Retrieving", url)
    uh = urllib.request.urlopen(url)

    data = uh.read()
    print("Retrieved", len(data), "characters")
    # print(data.decode())

    tree = ET.fromstring(data)
    mylist = tree.findall("comments/comment")
    print("Count:", len(mylist))

    num = 0

    for item in mylist:
        x = int(item.find("count").text)
        num += x

    print("Sum:", num)
