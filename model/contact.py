from sys import maxsize

class Contact:
    def __init__(self, first=None, middle=None, last=None, nick=None, title=None, address=None, mobile=None,
                 home=None, work=None, fax=None,
                 email=None, id_cont=None):
        self.email = email
        self.first = first
        self.middle = middle
        self.last = last
        self.nick = nick
        self.title = title
        self.address = address
        self.mobile = mobile
        self.home = home
        self.work = work
        self.fax = fax
        self.id_cont = id_cont

    def __repr__(self):
        return "%s:%s" % (self.id_cont, self.first)

    def __eq__(self, other):
        return (self.id_cont is None or other.id is None or self.id_cont == other.id) and self.first == other.first

    def id_or_max(self):
        if self.id_cont:
            return int(self.id_cont)
        else:
            return maxsize
