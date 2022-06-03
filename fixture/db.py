import pymysql.cursors
from model.group import Group
from model.contact import Contact


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
            cursor.execute("select id, firstname, lastname, mobile from addressbook")
            for row in cursor:
                (id, first, last, mobile) = row
                list_cont.append(Contact(id_cont=str(id), first=first, last=last, mobile=mobile))
        finally:
            cursor.close()
        return list_cont

    def destroy(self):
        self.connection.close()
