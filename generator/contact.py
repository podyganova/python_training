import jsonpickle
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data\\contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                    home_phone="", mobile="", work_phone="", fax="", email="", email2="", email3="", homepage="", byear="",
                    ayear="", address2="", phone2="", notes="")] + [
            Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                    lastname=random_string("lastname", 10), nickname=random_string("nickname", 10),
                    title=random_string("title", 10), company=random_string("company", 10),
                    address=random_string("address", 10), home_phone=random_string("8", 10),
                    mobile=random_string("9", 10), work_phone=random_string("78",10), fax=random_string("7", 10),
                    email=random_string("email", 10), email2=random_string("email2", 10), email3=random_string("email3", 10),
                    homepage=random_string("homepage", 10), byear=random_string("18", 2), ayear=random_string("20", 2),
                    address2=random_string("address2", 10), phone2=random_string("28", 10), notes=random_string("notes", 10))
            for i in range(5)]

file = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), f)


with open(file, "w") as out:
    out.write(jsonpickle.encode(testdata, indent=2))
