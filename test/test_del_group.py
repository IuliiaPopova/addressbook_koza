from model.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_groups_list()
    app.group.delete()
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"


def test_delete_first_group(app, check_group):
    """
    Second method for delete group
    """
    old_groups = app.group.get_groups_list()
    app.group.delete()
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups), f"Len old list '{old_groups}' != len new list '{new_groups}'"
    assert old_groups[1:] == new_groups, f"Old list '{old_groups}' != new list '{new_groups}'"
