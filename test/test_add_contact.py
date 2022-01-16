# -*- coding: utf-8 -*-
from model.contact import Contact
import time
import random
import string
import pytest


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10
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


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    time.sleep(5)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)