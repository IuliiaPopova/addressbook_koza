import pytest

from application import Application
from group import Group


@pytest.fixture
def app(request):
    application = Application()
    request.addfinalizer(application.tear_down)
    return application


def test_add_group(app):
    app.login(username="admin", password="secret")
    group = Group(name="dfgdfg", header="dfgdfg", footer="dfgfghgfhg")
    app.create_group(group)
    app.logout()


def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
