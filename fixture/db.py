import pymysql.cursors
from model.group import Group
from model.contact import Contact
import re


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password,
                                          autocommit=True)

    def get_group_list(self):
        list_gr = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list_gr.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list_gr

    def get_contact_list(self):
        list_cont = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, email3, home, work, mobile, phone2 from addressbook where deprecated= '0000-00-00 00:00:00'")
#        ("select id, firstname, lastname, address from addressbook where deprecated= '0000-00-00 00:00:00'")
            for row in cursor:
                (id, first, last, address, email, email2, email3, home, work, mobile, phone2) = row
#               row2 = (email, email2, email3)
#               row3 = (home, work, mobile, phone2)
                list_cont.append(Contact(id_cont=str(id), first=first, last=last, address=address,
                 home=home, mobile=mobile, work=work,  secondphone=phone2,
                           email=email, email2=email2, email3=email3))
#                (id, first, last, address) = row
#            list_cont.append(Contact(id_cont=str(id), first=first, last=last, address=address))
        finally:
            cursor.close()
        return list_cont

    def destroy(self):
        self.connection.close()
