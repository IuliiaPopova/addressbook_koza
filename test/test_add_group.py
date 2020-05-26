from model.group import Group


def test_add_group(app):
    """
    1.Get all groups from the screen
    2.Create a new group
    Verification:
    3.Checking count of groups +1 group(you created groups yourself) must equal count all groups on the screen
    4.Get all groups from the screen after added new group.
    5.Add a new group to old_group_list
    6.6.Compare updated old list and new list. Because id generates in JS we cannot add it manually.
    We use key=Group.id_or_max wich returns to us a very big number for added group from step 5.
    """
    #1. Get all groups from the screen
    old_group_list = app.group.get_groups_list()
    group = Group(name="dfgdfg", header="dfgdfg", footer="dfgfghgfhg")
    #2.Create a new group
    app.group.create(group)
    #3.Checking count of groups +1 group(you created groups yourself) must equal count all groups on the screen after add group
    assert len(old_group_list) + 1 == app.group.count()
    #4.Get all groups from the screen after added new group.
    new_group_list = app.group.get_groups_list()
    #5.Add a new group to old_group_list
    old_group_list.append(group)
    #6.Compare updated old list and new list.
    assert sorted(old_group_list, key=Group.id_or_max) == sorted(new_group_list, key=Group.id_or_max)

# def test_add_empty_group(app):
#     old_groups = app.group.get_groups_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     assert len(old_groups) + 1 == app.group.count()# count is hash function
#     new_groups = app.group.get_groups_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
