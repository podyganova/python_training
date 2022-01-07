# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Van", title="Title", company="Company", address="Address", home_phone="88888888",
                               mobile="77777777", work_phone="55555555", fax="99999999", email="ivanov", email2="ivan@gmail.com", email3="7638@yandex.ru",
                               homepage="IvanIvanov.com", byear="1990", ayear="2021", address2="Address2", phone2="Home", notes="TestTestTest")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    contact2 = Contact(firstname="Select ("+contact.firstname+" "+contact.lastname+")") #для сравнения
    old_contacts.append(contact2)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact2(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan2", middlename="Ivanovich2", lastname="Ivanov2", nickname="Van2", title="Title2", company="Company2", address="Address2", home_phone="8888888228",
                               mobile="777777772", work_phone="555555552", fax="999999992", email="ivanov2", email2="ivan@gmail.com2", email3="7638@yandex.ru2",
                               homepage="IvanIvanov2.com", byear="1992", ayear="2022", address2="Address22", phone2="Home2", notes="TestTestTest222")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    contact2 = Contact(firstname="Select ("+contact.firstname+" "+contact.lastname+")") #для сравнения
    old_contacts.append(contact2)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)