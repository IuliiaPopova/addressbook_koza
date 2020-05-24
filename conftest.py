import pytest

from fixture.application import Application
from model.group import Group

app_fixture = None


@pytest.fixture(scope="function")
def app():
    """
    Before each test method:
     1. Create an application fixture
        - if it doesn't exist or
        - if fixture doesn't valid (no opened browser)
     2. Login
    :return: app fixture
    """
    global app_fixture
    if not app_fixture or not app_fixture.is_valid():
        app_fixture = Application()
    app_fixture.session.ensure_login(username="admin", password="secret")
    return app_fixture


@pytest.fixture
def check_group():
    if not app_fixture.group.count():
        app_fixture.group.create(Group(name="test"))
