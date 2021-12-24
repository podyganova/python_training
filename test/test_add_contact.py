# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact

@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_untitled_test_case(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="Van", title="Title", company="Company", address="Address", home_phone="88888888",
                               mobile="77777777", work_phone="55555555", fax="99999999", email="ivanov", email2="ivan@gmail.com", email3="7638@yandex.ru",
                               homepage="IvanIvanov.com", byear="1990", ayear="2021", address2="Address2", phone2="Home", notes="TestTestTest"))
    app.session.logout()

