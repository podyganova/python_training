from model.group import Group


def test_modify_group_name(app):
    app.group.modify_first(Group(name="Test123"))


def test_modify_group_header(app):
    app.group.modify_first(Group(header="Test123"))


def test_modify_group_footer(app):
    app.group.modify_first(Group(footer="Test123"))

