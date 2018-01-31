__author__ = 'pavelkosicin'


def test_search_query(app):
    app.search.enter_query(query="thats")
    app.navigation.choose_songs_tab()
    app.search.check_response_title(expected_result_title="That's What I Like", error_message='Nothing found on request')
    app.search.check_response_person(expected_result_person="Bruno Mars", error_message='Wrong name of songwriter')
