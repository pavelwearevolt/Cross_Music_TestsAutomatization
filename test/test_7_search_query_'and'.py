__author__ = 'pavelkosicin'


def test_search_query(app):
    app.search.enter_query(query="and")
    app.navigation.choose_songs_tab()
    app.search.check_response_title(expected_result_title="Him & I", error_message='Nothing found on request')
    app.search.check_response_person(expected_result_person="G-Eazy, Halsey", error_message='Wrong name of songwriter')
