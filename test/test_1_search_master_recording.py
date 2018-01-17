__author__ = 'pavelkosicin'


def test_search_master_recording(app):
    app.search.enter_query(query="perfect")
    app.navigation.choose_recording_tab()
    app.search.check_search_result(expected_result="Perfect")
