from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1",header="kpggdtaka", footer="tnlhtdt"))
    old_groups = app.group.get_groups_list()
    app.group.modify(Group(name="koza", header="kaka", footer="tt"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"



def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1"))
    old_groups = app.group.get_groups_list()
    app.group.modify(Group(name="kaka"))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"


