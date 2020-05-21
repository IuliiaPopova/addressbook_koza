from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    group = Group(name="dfgdfg", header="dfgdfg", footer="dfgfghgfhg")
    app.group.create(group)
    app.session.logout()


# def test_add_empty_group(app):
#     app.session.login(username="admin", password="secret")
#     app.group.create(Group(name="", header="", footer=""))
#     app.session.logout()
