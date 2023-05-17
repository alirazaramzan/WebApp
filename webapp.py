import streamlit as st

def calculate_bmi(weight, height):
    # Convert height from cm to meters
    height /= 100

    # Calculate BMI
    bmi = weight / (height * height)
    return bmi

def generate_diet_timetable(weight, height):
    bmi = calculate_bmi(weight, height)

    # Generate diet timetable based on BMI
    if bmi < 18.5:
        timetable = "You are underweight. Here's a sample diet plan:\n\n- Breakfast: Oatmeal with fruits\n- Snack: Greek yogurt with nuts\n- Lunch: Grilled chicken with vegetables\n- Snack: Protein shake\n- Dinner: Baked fish with quinoa\n- Snack: Mixed berries"
    elif 18.5 <= bmi < 24.9:
        timetable = "You have a normal weight. Here's a sample diet plan:\n\n- Breakfast: Whole grain toast with avocado\n- Snack: Apple with peanut butter\n- Lunch: Salad with grilled tofu\n- Snack: Hummus with carrots\n- Dinner: Quinoa with roasted vegetables\n- Snack: Dark chocolate"
    elif 24.9 <= bmi < 29.9:
        timetable = "You are overweight. Here's a sample diet plan:\n\n- Breakfast: Scrambled eggs with vegetables\n- Snack: Almonds\n- Lunch: Brown rice with lean meat\n- Snack: Greek yogurt with honey\n- Dinner: Grilled salmon with steamed broccoli\n- Snack: Edamame beans"
    else:
        timetable = "You are obese. Here's a sample diet plan:\n\n- Breakfast: Green smoothie with spinach and banana\n- Snack: Rice cakes with almond butter\n- Lunch: Quinoa salad with chickpeas\n- Snack: Mixed nuts\n- Dinner: Grilled chicken with sweet potato\n- Snack: Sliced watermelon"

    return timetable

# Streamlit app code
def main():
    st.title("Nutrition Diet Timetable Generator")
    st.write("Enter your weight and height to generate a diet timetable.")

    weight = st.number_input("Weight (in kg)")
    height = st.number_input("Height (in cm)")

    if weight <= 0 or height <= 0:
        st.warning("Please enter valid weight and height.")
    else:
        if st.button("Generate Timetable"):
            timetable = generate_diet_timetable(weight, height)
            st.subheader("Your Diet Timetable:")
            st.write(timetable)

if __name__ == "__main__":
    main()
