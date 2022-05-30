from model.contact import Contact
#import pytest
import random
import string


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


testdata = [
    Contact(first=first, last=last, address=address, email=email, mobile=mobile, home=home)
    for first in ["", random_full_string("first", 10)]
    for last in ["", random_full_string("last", 15)]
    for address in ["", random_full_string("address", 30)]
    for email in ["", random_mail_string("email", 15)]
    for mobile in ["", random_phone_string("mobile", 10)]
    for home in ["", random_phone_string("home", 10)]
]
