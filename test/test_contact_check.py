import re
from model.contact import Contact


def test_contact_check(app, db):
    contact_home = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contact_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contact_home)):
        assert contact_home[i].firstname == contact_db[i].firstname
        assert contact_home[i].lastname == contact_db[i].lastname
        assert contact_home[i].address == contact_db[i].address
        assert contact_home[i].all_emails == merge_emails(contact_db[i])
        assert contact_home[i].all_phones == merge_phone(contact_db[i])


def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails(contact):
    return "\n".join(filter(lambda x: x !="",
                               (filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


def merge_phone(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home_phone, contact.mobile, contact.work_phone,
                                                                 contact.phone2]))))