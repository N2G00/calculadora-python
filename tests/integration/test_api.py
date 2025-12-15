import pytest
from src.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_api_divide(client):
    response = client.post('/calculate', json={
        'operation': 'divide',
        'a': 20,
        'b': 2
    })
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 10