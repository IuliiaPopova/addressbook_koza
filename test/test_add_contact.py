import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    application = Application()
    request.addfinalizer(application.tear_down)
    return application


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Olga", last_name="Kozlova"))
    app.session.logout()
