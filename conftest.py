import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
    # create fixture
        fixture = Application()
        fixture.session.login(username="admin", passw='secret')
    else:
        if not fixture.is_valid:
            fixture = Application()
            fixture.session.login(username="admin", passw='secret')
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture
