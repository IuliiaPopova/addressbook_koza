from random import randrange

from model.group import Group


def test_delete_group(app):
    """
    if don't have any group we create one group before delete
    """
    if app.group.count() == 0:#checking we have any group or no
        app.group.create(Group(name="test"))#if don't have any group we create one group before delete
    old_groups = app.group.get_groups_list()
    #randrange returns a random int from range(start, stop[, step])
    index = randrange(len(old_groups))
    app.group.delete(index)
    new_groups = app.group.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups), f"Old list '{old_groups}' != new list '{new_groups}'"
    old_groups[index:index + 1] = []
    assert old_groups == new_groups

# def test_delete_first_group(app, check_group):
#     """
#     Second method for delete group
#     """
#     old_groups = app.group.get_groups_list()
#     app.group.delete()
#     new_groups = app.group.get_groups_list()
#     assert len(old_groups) - 1 == len(new_groups), f"Len old list '{old_groups}' != len new list '{new_groups}'"
#     assert old_groups[1:] == new_groups, f"Old list '{old_groups}' != new list '{new_groups}'"
