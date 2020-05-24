from model.group import Group


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test1", header="kpggdtaka", footer="tnlhtdt"))
    old_groups = app.group.get_groups_list()
    group = Group(name="koza", header="kaka", footer="tt")
    group.id = old_groups[0].id
    app.group.modify(group)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test1"))
#     old_groups = app.group.get_groups_list()
#     app.group.modify(Group(name="kaka"))
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"
