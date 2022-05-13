from sys import maxsize

class Contact:
    def __init__(self, first=None, middle=None, last=None, nick=None, title=None, address=None, mobile=None, email=None, id=None):
        self.email = email
        self.first = first
        self.middle = middle
        self.last = last
        self.nick = nick
        self.title = title
        self.address = address
        self.mobile = mobile
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.first)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first == other.first

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
