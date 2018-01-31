__author__ = 'pavelkosicin'


def test_search_query(app):
    app.search.enter_query(query="18002738255")
    app.navigation.choose_songs_tab()
    app.search.check_response_title(expected_result_title="1-800-273-8255", error_message='Nothing found on request')
    app.search.check_response_person(expected_result_person="Logic, Alessia Cara", error_message='Wrong name of songwriter')
