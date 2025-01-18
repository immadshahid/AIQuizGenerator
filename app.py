import openai
import streamlit as st

# Azure OpenAI Configuration
openai.api_type = "azure"
openai.api_base = "https://mansai.openai.azure.com/"
openai.api_version = "2023-06-01-preview"
openai.api_key = "OPENAPIKEY"

# Streamlit Interface
st.title("Personalized Learning Assistant")

# User Inputs
topic = st.text_input("Enter Topic", "")
difficulty = st.selectbox("Select Difficulty", ["Easy", "Medium", "Hard"])
question_count = st.number_input("Number of Questions", min_value=1, max_value=20, step=1)

# Quiz Generation Button
if st.button("Generate Quiz"):
    try:
        # Generate prompt
        prompt = (
            f"Generate a quiz with {question_count} questions on the topic '{topic}'. "
            f"The difficulty level should be {difficulty}. Include multiple-choice answers and mark the correct one."
        )

        # Call Azure OpenAI
        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo",  # Replace with your deployment name
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000,
            temperature=0.7,
        )

        # Extract response text
        quiz = response.choices[0].message["content"].strip()

        st.success("Quiz Generated Successfully!")
        st.text_area("Generated Quiz", quiz, height=400)

    except openai.error.OpenAIError as e:
        st.error(f"OpenAI API error: {str(e)}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")

