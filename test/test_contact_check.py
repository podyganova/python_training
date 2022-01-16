import re


def test_contact_check(app):
    contact_home = app.contact.get_contact_list()[0]
    contact_edit = app.contact.get_contact_edit(0)
    assert contact_home.firstname == clear(contact_edit.firstname)
    assert contact_home.lastname == clear(contact_edit.lastname)
    assert contact_home.address == clear(contact_edit.address)
    assert contact_home.all_emails == merge_emails(contact_edit)
    assert contact_home.all_phones == merge_phone(contact_edit)

 
def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3]))))


def merge_phone(contact):
    return "\n".join(filter(lambda x: x !="",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None, [contact.home_phone, contact.mobile, contact.work_phone,
                                                                 contact.phone2]))))