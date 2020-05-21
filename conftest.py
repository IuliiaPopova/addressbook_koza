import pytest

from fixture.application import Application


@pytest.fixture(scope="session")
def app(request):
    application = Application()
    request.addfinalizer(application.tear_down)
    return application