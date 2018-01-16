__author__ = 'pavelkosicin'


def test_search_master_recording(app):
    app.session.login(username="pavel.kosicin@wearevolt.com", password="abcd1234")
    app.search.enter_query(query="perfect")
    app.session.logout()
