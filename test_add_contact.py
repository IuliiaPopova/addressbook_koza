import pytest

from application import Application
from contact import Contact


@pytest.fixture
def app(request):
    application = Application()
    request.addfinalizer(application.tear_down)
    return application


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_cont(Contact(first_name="Olga", last_name="Kozlova"))
    app.logout()
