def calculate_calories(current_weight, goal_weight, activity_level):
    base_calories = 2000
    calorie_deficit = 500 if activity_level == "Moderate" else 700
    return base_calories - calorie_deficit
