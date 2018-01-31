__author__ = 'pavelkosicin'


def test_search_query(app):
    app.search.enter_query(query="perfecd")
    app.navigation.choose_songs_tab()
    app.search.check_response_title(expected_result_title="Perfect", error_message='Nothing found on request')
    app.search.check_response_person(expected_result_person="Ed Sheeran, Beyonce",
                                     error_message='Wrong name of songwriter')
