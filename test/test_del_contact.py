import time
from random import randrange
from model.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_some(index)
    time.sleep(5)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


def test_del_all_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Van", title="Title",
                company="Company", address="Address", home_phone="88888888",
                mobile="77777777", work_phone="55555555", fax="99999999", email="ivanov", email2="ivan@gmail.com",
                email3="7638@yandex.ru",
                homepage="IvanIvanov.com", byear="1990", ayear="2021", address2="Address2", phone2="Home",
                notes="TestTestTest"))
    app.contact.delete_all()
    time.sleep(5)
    old_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == 0


def test_del_edit(app): # Удаление через форму редактирования
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Van", title="Title",
                company="Company", address="Address", home_phone="88888888",
                mobile="77777777", work_phone="55555555", fax="99999999", email="ivanov", email2="ivan@gmail.com",
                email3="7638@yandex.ru",
                homepage="IvanIvanov.com", byear="1990", ayear="2021", address2="Address2", phone2="Home",
                notes="TestTestTest"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_edit_some(index)
    time.sleep(5)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts


