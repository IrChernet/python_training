from model.group import Group


testdata = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

#def random_string(prefix, maxlen):
#    sumbol = string.ascii_letters + string.punctuation + string.digits + " "*10
#    return prefix + "".join([random.choice(sumbol) for i in range(random.randrange(maxlen))])


#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name", 10)]
#    for header in ["", random_string("header", 15)]
#    for footer in ["", random_string("footer", 15)]
#    ]
