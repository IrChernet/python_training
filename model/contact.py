from sys import maxsize

class Contact:
    def __init__(self, id_cont=None, first=None, middle=None, last=None, nick=None, title=None, address=None,
                 all_phones=None, fax=None, home=None, work=None, mobile=None, secondphone=None, all_mails=None,
                 email=None, email2=None, email3=None, address2=None):
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_mails = all_mails
        self.first = first
        self.middle = middle
        self.last = last
        self.nick = nick
        self.title = title
        self.address = address
        self.home = home
        self.work = work
        self.mobile = mobile
        self.secondphone = secondphone
        self.all_phones = all_phones
        self.fax = fax
        self.address2 = address2
        self.id_cont = id_cont

    def __repr__(self):
        return "%s:%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s" % (self.id_cont, self.first, self.last,
                                   self.home, self.work, self.mobile, self.secondphone,
                                   self.email, self.email2, self.email3,
                                    self.all_phones, self.all_mails)

    def __eq__(self, other):
        return (self.id_cont is None or other.id_cont is None or self.id_cont == other.id_cont) and self.first == other.first

    def id_or_max(self):
        if self.id_cont:
            return int(self.id_cont)
        else:
            return maxsize
