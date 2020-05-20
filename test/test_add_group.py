import pytest

from fixture.application import Application
from model.group import Group


@pytest.fixture
def app(request):
    application = Application()
    request.addfinalizer(application.tear_down)
    return application


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    group = Group(name="dfgdfg", header="dfgdfg", footer="dfgfghgfhg")
    app.group.create(group)
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()
