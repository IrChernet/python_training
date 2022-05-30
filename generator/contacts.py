from model.contact import Contact
import random
import string
import json
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number contacts", "file"])
except getopt.GetoptError as err_gen:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_full_string(prefix, maxlen):
    sumbol = string.ascii_letters + string.digits + " "*10
    return prefix + "".join([random.choice(sumbol) for i in range(random.randrange(maxlen))])


def random_phone_string(prefix, maxlen):
    sumbol = string.digits
    s6 = "".join(random.choice(sumbol) for i in range(6))
    s3 = "".join(random.choice(sumbol) for i in range(3))
    s1 = "+7(" + s3 + ")" +s6
    return prefix + s1


def random_mail_string(prefix, maxlen):
    sumbol = string.ascii_letters + "@" + string.digits
    return prefix + "".join([random.choice(sumbol) for i in range(random.randrange(maxlen))])


testdata = [Contact(first="", last="", address="", email="", mobile="", home="")] + [
    Contact(first=random_full_string("first", 10),
            last=random_full_string("last", 15),
            address=random_full_string("address", 30),
            email=random_mail_string("email", 15),
            mobile=random_phone_string("mobile", 10),
            home=random_phone_string("home", 10))
    for i in range(n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
