from fastapi.testclient import TestClient

from app import app


client = TestClient(app)


def test_main_page():
    response = client.get('/')
    assert response.status_code == 200


def test_success_search_fragment():
    response = client.post('/', json={'phrase': 'сказал'})

    assert response.status_code == 200
    assert 'fragment_text' in response.json()
    assert 'author' in response.json()
    assert 'book_title' in response.json()


def test_fragment_not_found():
    response = client.post('/', json={'phrase': 'сказал, что отрывек не найден...'})

    assert response.status_code == 404
    assert response.json() == {"detail": "Отрывок не найден..."}
