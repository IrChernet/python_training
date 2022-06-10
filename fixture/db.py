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
            cursor.execute("select id, firstname, lastname, address from addressbook where deprecated= '0000-00-00 00:00:00'")
            for row in cursor:
                (id, first, last, address) = row
#                  email, email2, email3, home, mobile, phone2) = row
                list_cont.append(Contact(id_cont=str(id), first=first, last=last, address=address))
#                list_cont.append(Contact(id_cont=str(id), first=first, last=last, address=address,
#                all_mail=all_mail, all_phones=all_phone))
        finally:
            cursor.close()
        return list_cont

    def destroy(self):
        self.connection.close()
