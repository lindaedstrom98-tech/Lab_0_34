from src.api import app

def test_hello_route():
    client = app.test_client()
    response = client.get('/hello')
    
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello World!"}