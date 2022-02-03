from model.group import Group
import random


def test_edit_id_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    index = old_groups.index(random.choice(old_groups))
    group_new = Group(name="Test3", header="Test3", footer="Test3")
    group_new.id = old_groups[index].id
    app.group.edit_by_id(group_new)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group_new
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
