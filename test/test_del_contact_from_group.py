from model.contact import Contact
import random
from model.group import Group


def test_del_contact_from_group(app, db, ORMdb):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    group = random.choice(ORMdb.get_group_list())
    if len(ORMdb.get_contacts_in_group(group)) == 0:
        app.contact.add_to_group(random.choice(db.get_contact_list()).id, group.id)
    contacts_group = app.contact.get_contact_list_group(group)
    contact = random.choice(contacts_group)
    app.contact.del_from_group(contact.id, group)
    list_contacts_db = ORMdb.get_contacts_in_group(group)
    assert contact not in list_contacts_db
