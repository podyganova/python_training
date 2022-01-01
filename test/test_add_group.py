# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Test", header="Test", footer="Test"))


def test_add_group2(app):
    app.group.create(Group(name="Test2", header="Test2", footer="Test2"))
