from backend_api import app
import pytest 

def test_dummy_wrong_route(): 
    with app.test_client() as client:
        response = client.get('/wrong_route')
        assert response.status_code == 404


def test_dummy_correct_route():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

with app.test_client() as client:
    response = client.get('/recipes')
    assert response.status_code == 200

with app.test_client() as client:
    response = client.get('/recipes/1')
    assert response.status_code == 200

with app.test_client() as client:
    response = client.post('/recipes', json={'name': 'soup', 'ingredients': 'water', 'instructions': 'boil', 'favorite': False, 'rating': 4})
    assert response.status_code == 200

with app.test_client() as client:
    response = client.put('/recipes/1', json={'name': 'soup', 'ingredients': 'water', 'instructions': 'boil', 'favorite': False, 'rating': 4})
    assert response.status_code == 200

