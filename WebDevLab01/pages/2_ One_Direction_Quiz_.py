import streamlit as st
import random
st.title("Which One Direction Member Are You?") # title and description
st.markdown("""
This quiz will help you find out which One Direction member you are most like. 
Answer the questions below and let’s see who you are most compatible with!
""") # quiz description 

# Question 1: Personality type (Multiple choice)
st.subheader("What is your personality like?") # question title
personality = st.radio( # multiple choice question 
    "Choose your personality type:",
    ["Outgoing", "Funny", "Shy", "Creative", "Adventurous"]  # NEW
)

# Question 2: Style (Multi-select)
st.subheader("Which of the following would describe your style?") # question title
style = st.multiselect( # drop down, allows you to slect multiple 
    "Pick all that apply:",
    ["Casual", "Glam", "Sporty", "Rock Star", "Trendy"]  # NEW 
)

# Question 3: Music taste (Number input)
st.subheader("On a scale of 1-10, how much do you love pop music?") # question title 
music_love = st.slider(
    "How much do you love pop music?", 
    1, 10, 5  # NEW 
)

# Question 4: Dream vacation (Selectbox)
st.subheader("Where would you love to go for a vacation?")
vacation = st.selectbox(
    "Choose your dream vacation destination:",
    ["Paris", "Hawaii", "London", "New York", "Tokyo"]  # NEW 
)

# 5. Question 5: Favorite trait (Multiple choice)
st.subheader("What is your most attractive trait?")
favorite_trait = st.radio(
    "Choose one that best represents you:",
    ["Sense of Humor", "Creativity", "Kindness", "Confidence"]
)

# Display images of One Direction members
st.image("Images/Harry.jpg", caption="Harry Styles", width=250)  # NEW 
st.image("Images/Liam_Payne.webp", caption="Liam Payne", width=250)  # NEW 
st.image("Images/zayn.jpeg", caption="Zayn Malik", width=250)  # NEW 

# 6. Show results based on answers
if st.button("Submit"):
    # Logic to calculate results
    if personality == "Outgoing":
        result = "Harry Styles"
    elif personality == "Funny":
        result = "Liam Payne"
    elif personality == "Shy":
        result = "Zayn Malik"
    elif personality == "Creative":
        result = "Louis Tomlinson"
    else:
        result = "Niall Horan"

    st.markdown(f"**You are most like {result}!**")
    st.balloons()  # NEW 
