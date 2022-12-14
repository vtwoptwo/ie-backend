from backend_api import app
import pytest 

def test_dummy_wrong_route(): 
    with app.test_client() as client:
        response = client.get('/wrong_route')
        assert response.status_code == 404


