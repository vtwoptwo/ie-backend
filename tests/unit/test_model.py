from backend_api.models import Recipe
import pytest

def test_create_account():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, instructions, favorite, and rating are defined correctly
    """
    recipe = Recipe('soup', 'water', 'boil', False, 4)
    assert recipe.name == 'soup'
    assert recipe.ingredients == 'water'
    assert recipe.instructions == 'boil'
    assert recipe.favorite == False
    assert recipe.rating == 4

