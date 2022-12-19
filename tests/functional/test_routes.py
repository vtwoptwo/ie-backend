from backend_api import app
import pytest

def test_get_recipes(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is requested (GET)
    THEN check that the response is valid
    """
 
    response = testing_client.get('/recipes')
    assert response.status_code == 200

def test_dummy_wrong_route(): 
    """
    GIVEN a Flask application
    WHEN the '/wrong_route' page is requested (GET)
    THEN check that the response is valid
    """

    with app.test_client() as client:
        response = client.get('/wrong_route')
        assert response.status_code == 404

def test_create_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes' page is requested (POST)
    THEN check that the response is valid
    """
    response = testing_client.post('/recipes', json={ 'name': 'ketchup', 'ingredients': 'water', 'instructions': 'boil', 'favorite': False, 'rating': 4})
    assert response.json['name'] == 'ketchup'
    assert response.json['ingredients'] == 'water'
    assert response.json['instructions'] == 'boil'
    assert response.json['favorite'] == False
    assert response.json['rating'] == 4
    assert response.status_code == 200

def test_edit_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes/<recipe_id>' page is requested (PUT)
    THEN check that the response is valid
    """
    response = testing_client.put('/recipes/1', json={ 'name': 'soup', 'ingredients': 'water', 'instructions': 'boil', 'favorite': False, 'rating': 4})
    assert response.json['name'] == 'soup'
    assert response.json['ingredients'] == 'water'
    assert response.json['instructions'] == 'boil'
    assert response.json['favorite'] == False
    assert response.json['rating'] == 4
    assert response.status_code == 200

def test_delete_recipe(testing_client):
    """
    GIVEN a Flask application
    WHEN the '/recipes/<recipe_id>' page is requested (DELETE)
    THEN check that the response is valid
    """
    response = testing_client.delete('/recipes/1')
    assert response.status_code == 200
    