import pytest
from models.meal_plan_recommender import recommend_meal_plan

def test_recommend_meal_plan():
    result = recommend_meal_plan(vegetarian=True)
    assert all("Chicken" not in meal["name"] for meal in result)
