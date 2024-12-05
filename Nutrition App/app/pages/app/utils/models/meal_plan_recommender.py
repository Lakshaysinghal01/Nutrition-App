def recommend_meal_plan(calories=None, vegetarian=False, low_carb=False, fiber_rich=False, high_protein=False, workout_intense=False):
    # Example meal plans
    meal_plans = [
        {"name": "Grilled Chicken Salad", "calories": 350},
        {"name": "Quinoa Bowl with Vegetables", "calories": 400},
    ]

    if vegetarian:
        meal_plans = [meal for meal in meal_plans if "Chicken" not in meal["name"]]

    return meal_plans
