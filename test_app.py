from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_index():
    response = client.get('/')
    assert response.status_code == 200


def test_register():
    user = {
        'firstName': 'Serhii',
        'lastName': 'Khara',
        'birthday': '17.07.2005',
        'email': 'test@gmail.com',
        'password': 'TestPassword',
    }
    response = client.post('/user/', json=user)

    assert response.status_code == 401


def test_login():
    user = {'email': 'test@gmail.com', 'password': 'TestPassword'}
    response = client.post('/auth/login', json=user)
    assert response.status_code == 400


def test_fetching_items():
    response = client.get('/items/')
    assert response.status_code == 200
