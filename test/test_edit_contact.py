from model.contact import Contact
import random


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = old_contacts.index(random.choice(old_contacts))
    contact = Contact(firstname="Ivan3", middlename="Ivanovich3", lastname="Ivanov3", nickname="Van3", title="Title3", company="Company3", address="Address3", home_phone="88888888333",
                               mobile="77777777333", work_phone="55555555333", fax="999999993333", email="ivanov333", email2="ivan3333@gmail.com", email3="7638333@yandex.ru",
                               homepage="IvanIvanov333.com", byear="1933", ayear="2023", address2="Address23", phone2="Home3", notes="TestTestTest333")
    contact.id = old_contacts[index].id
    app.contact.edit_by_id(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)


def test_edit_contact_details(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    index = old_contacts.index(random.choice(old_contacts))
    contact = Contact(firstname="Ivan34", middlename="Ivanovich34", lastname="Ivanov34", nickname="Van34", title="Title34", company="Company34", address="Address34", home_phone="88888888333444",
                               mobile="7777777733344", work_phone="5555555533344", fax="9999999933334", email="ivanov33344", email2="ivan333344@gmail.com", email3="763833344@yandex.ru",
                               homepage="IvanIvanov33344.com", byear="1934", ayear="2034", address2="Address234", phone2="Home34", notes="TestTestTest333444")
    contact.id = old_contacts[index].id
    app.contact.edit_details_id(contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
