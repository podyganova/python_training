from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="Test3", header="Test3", footer="Test3"))
    app.session.logout()
