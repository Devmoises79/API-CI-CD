import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Testa o endpoint principal"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'API Flask funcionando!'
    print(" Home endpoint OK")

def test_health_endpoint(client):
    """Testa o endpoint de health check"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    print(" Health endpoint OK")

def test_sum_endpoint(client):
    """Testa o endpoint de soma"""
    response = client.get('/api/sum/5/3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8
    print(" Sum endpoint OK")