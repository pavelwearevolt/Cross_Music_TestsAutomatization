__author__ = 'pavelkosicin'

import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_first_test(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.search.enter_query(query="perfect")
    app.session.logout()

