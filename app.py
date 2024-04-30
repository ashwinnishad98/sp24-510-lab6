import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

prompt_template = """
You are an expert event planner in birthdays, gatherings, and other special occasions. 

Please provide comprehensive and accurate information to plan the perfect event for your client. This includes locations of venues/activities and their booking information, etc.

<event planning requirements to consider>
- Individual roles and responsibilities 
- Budget 
- Date and time of the event 
- Event master plan 
- Event location 
- Day-of processes
- Last-miute details and extras
</event planning requirements to consider>

Please include the following details:
- Type of event
- Date and Time
- The location or city
- Number of guests
- Budget
- Catering needs
- Contact information
- Short text and email to send the invitees

Use the following step-by-step instructions to respond to user inputs:
Step 1 - The user will provide you with an overall description of the event they want to plan. Try to fill in the details as much as possible.
Step 2 - The response should start with the overall plan for the event prefixed with "High Level Plan". Then display various aspects of the events.

The user's request is:
{prompt}
"""


def add_custom_css():
    """
    Adds custom CSS styles to the application.

    This function generates a CSS string and applies it to the application using Streamlit's `markdown` function.

    Returns:
        None
    """
    css = """
    <style>
        header {visibility: hidden;}
        .css-1d391kg {text-align: center;}
        .stButton>button {width: 100%;}
        textarea {
            font-size: 30px;
        }
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)


add_custom_css()


def local_css(file_name):
    """
    Applies local CSS styles to the Streamlit app.

    Parameters:
    file_name (str): The path to the CSS file.

    Returns:
    None
    """
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def generate_prompt_response(prompt):
    """
    Generates a response based on the given prompt.

    Args:
        prompt (str): The prompt to generate a response for.

    Returns:
        str: The generated response.
    """
    response = model.generate_content(prompt_template.format(prompt=prompt))
    return response.text


st.title("Event Planner 💒🥳")

local_css("style.css")

event_needs = st.text_area(
    "Please provide the details of the event you want to plan. Include the type of event, date and time, location, number of guests, budget, catering needs, and contact information and any other relevant information."
)

if st.button("Plan my Event! 🎉"):
    response = generate_prompt_response(event_needs)
    st.divider()
    st.write(response)