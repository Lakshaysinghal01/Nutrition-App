import streamlit as st
from app.utils.data_processing import calculate_calories
from models.meal_plan_recommender import recommend_meal_plan

def run():
    st.title("Weight Loss Journey")
    st.write("Personalized dietary recommendations for your weight loss goals.")

    # User inputs
    age = st.number_input("Age", 18, 100)
    weight = st.number_input("Current Weight (kg)", 30, 200)
    goal_weight = st.number_input("Goal Weight (kg)", 30, 200)
    activity_level = st.selectbox("Activity Level", ["Low", "Moderate", "High"])
    vegetarian = st.checkbox("Vegetarian")

    if st.button("Get Meal Plan"):
        calorie_target = calculate_calories(weight, goal_weight, activity_level)
        meal_plan = recommend_meal_plan(calorie_target, vegetarian)
        st.write("### Recommended Meal Plan")
        for meal in meal_plan:
            st.write(f"- {meal['name']} ({meal['calories']} kcal)")
