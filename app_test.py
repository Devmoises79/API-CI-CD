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
    assert data['status'] == 'success'
    assert 'API Flask funcionando!' in data['message']
    print(" Teste home endpoint passou!")

def test_health_endpoint(client):
    """Testa o endpoint de health check"""
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'
    print(" Teste health endpoint passou!")

def test_get_user(client):
    """Testa o endpoint de usuário"""
    response = client.get('/api/users/123')
    assert response.status_code == 200
    data = response.get_json()
    assert data['id'] == 123
    assert 'Usuário' in data['name']
    print(" Teste get_user passou!")

def test_sum_endpoint(client):
    """Testa o endpoint de soma"""
    response = client.get('/api/sum/5/3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8
    print(" Teste sum endpoint passou!")

if __name__ == '__main__':
    print(" Executando testes...")
    pytest.main([__file__, '-v'])