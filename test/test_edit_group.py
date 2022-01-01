from model.group import Group


def test_edit_group(app):
    app.group.edit(Group(name="Test3", header="Test3", footer="Test3"))
