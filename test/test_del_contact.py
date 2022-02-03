import time
import random
from model.contact import Contact


def test_del_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_some_id(contact.id)
    time.sleep(5)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)


def test_del_all_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Van", title="Title",
                company="Company", address="Address", home_phone="88888888",
                mobile="77777777", work_phone="55555555", fax="99999999", email="ivanov", email2="ivan@gmail.com",
                email3="7638@yandex.ru",
                homepage="IvanIvanov.com", byear="1990", ayear="2021", address2="Address2", phone2="Home",
                notes="TestTestTest"))
    app.contact.delete_all()
    time.sleep(5)
    old_contacts = db.get_contact_list()
    assert len(old_contacts) == 0


def test_del_edit(app, db, check_ui): # Удаление через форму редактирования
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Van", title="Title",
                company="Company", address="Address", home_phone="88888888",
                mobile="77777777", work_phone="55555555", fax="99999999", email="ivanov", email2="ivan@gmail.com",
                email3="7638@yandex.ru",
                homepage="IvanIvanov.com", byear="1990", ayear="2021", address2="Address2", phone2="Home",
                notes="TestTestTest"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_edit_id(contact.id)
    time.sleep(5)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_group_list(), key=Contact.id_or_max)

