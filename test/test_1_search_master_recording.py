__author__ = 'pavelkosicin'


def test_search_master_recording(app):
    app.search.enter_query(query="perfect")
