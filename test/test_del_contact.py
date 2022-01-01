from model.contact import Contact

def test_del_contact(app):
    app.contact.delete_first()


def test_del_all_contact(app):
    app.contact.delete_all()
    # Добавление нового контакта, после общего удаления, для возможности выполнения следующих тестов
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Van", title="Title",
                company="Company", address="Address", home_phone="88888888",
                mobile="77777777", work_phone="55555555", fax="99999999", email="ivanov", email2="ivan@gmail.com",
                email3="7638@yandex.ru",
                homepage="IvanIvanov.com", byear="1990", ayear="2021", address2="Address2", phone2="Home",
                notes="TestTestTest"))


def test_del_edit(app): # Удаление через форму редактирования
    app.contact.delete_edit()
    # Добавление нового контакта,для возможности выполнения следующих тестов
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Van", title="Title",
                company="Company", address="Address", home_phone="88888888",
                mobile="77777777", work_phone="55555555", fax="99999999", email="ivanov", email2="ivan@gmail.com",
                email3="7638@yandex.ru",
                homepage="IvanIvanov.com", byear="1990", ayear="2021", address2="Address2", phone2="Home",
                notes="TestTestTest"))


