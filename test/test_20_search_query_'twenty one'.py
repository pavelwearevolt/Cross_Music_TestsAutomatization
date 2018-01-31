__author__ = 'pavelkosicin'


def test_search_query(app):
    app.search.enter_query(query="twenty one")
    app.navigation.choose_songs_tab()
    app.search.check_response_title(expected_result_title="Bank Account", error_message='Nothing found on request')
    app.search.check_response_person(expected_result_person="21 Savage", error_message='Wrong name of songwriter')
