from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="Ivan3", middlename="Ivanovich3", lastname="Ivanov3", nickname="Van3", title="Title3", company="Company3", address="Address3", home_phone="88888888333",
                               mobile="77777777333", work_phone="55555555333", fax="999999993333", email="ivanov333", email2="ivan3333@gmail.com", email3="7638333@yandex.ru",
                               homepage="IvanIvanov333.com", byear="1933", ayear="2023", address2="Address23", phone2="Home3", notes="TestTestTest333"))
    app.session.logout()

def test_edit_contact_details(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_details(Contact(firstname="Ivan34", middlename="Ivanovich34", lastname="Ivanov34", nickname="Van34", title="Title34", company="Company34", address="Address34", home_phone="88888888333444",
                               mobile="7777777733344", work_phone="5555555533344", fax="9999999933334", email="ivanov33344", email2="ivan333344@gmail.com", email3="763833344@yandex.ru",
                               homepage="IvanIvanov33344.com", byear="1934", ayear="2034", address2="Address234", phone2="Home34", notes="TestTestTest333444"))
    app.session.logout()
