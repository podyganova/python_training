# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Test", header="Test", footer="Test"))
    app.logout()

def test_add_group2(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Test2", header="Test2", footer="Test2"))
    app.logout()
