from model.contact import Contact
import random
from model.group import Group


def test_add_contact_in_group(app, db, ORMdb):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(ORMdb.get_group_list())
    contacts_not_in_group = ORMdb.get_contacts_not_in_group(group)
    if len(contacts_not_in_group) == 0:
        app.contact.create(Contact(firstname="test"))
        contacts_not_in_group = ORMdb.get_contacts_not_in_group(group)
    contact = random.choice(contacts_not_in_group)
    app.contact.add_to_group(contact.id, group.id)
    list_contacts_db = ORMdb.get_contacts_in_group(group)
    assert contact in list_contacts_db