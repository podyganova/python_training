from model.contact import Contact
import random
from fixture.orm import ORMFixture
from model.group import Group

ORMdb = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


def test_add_contact_in_group(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    all_contacts = db.get_contact_list()
    groups = ORMdb.get_group_list()
    contact = random.choice(all_contacts)
    group = random.choice(groups)
    list_contacts_group = app.contact.add_to_group(contact.id, group.id)
    list_contacts_db = ORMdb.get_contacts_in_group(group)
    assert sorted(list_contacts_group, key=Contact.id_or_max) == sorted(list_contacts_db, key=Contact.id_or_max)
