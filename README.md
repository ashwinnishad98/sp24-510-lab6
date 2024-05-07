# Lab 6
## Event Planner using Gemini with Improved Prompting Techniques

## What it does
This app is an event planner that helps users plan various types of events, such as birthdays, gatherings, and special occasions. It uses Google's Gemini LLM to generate responses based on the user's input. The app prompts the user to provide comprehensive details about the event, including the type of event, date and time, location, number of guests, budget, catering needs, contact information, and more. Once the user submits the event details, the app generates a response using the AI model and displays it to the user.

### How to Run
Open your terminal (if in VS Code, press ```ctrl + ` ```).

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### What's Included
- app.py: Entry point to the application, where a prompt from the user regarding details about the event are sent to Google's Gemini LLM to plan an event.

## Problems when developing the last app
- It seemed to provide random suggestions for venues, not taking into consideration the type of event
- Always provided an email template, even for informal events such as birthdays with a few friends

## Changes made to code
- Added delimeters to indicate what parts of the event planning to consider.
- Added step by step instructions to be followed when designing the event.
- Added clearer and in-depth instructions for the LLM to follow.

## Improvements
- A lot better at providing exact information required for the event, in terms of venue and budget needs.
- Better email/text templates based on the context of the event.
- Brief overview of the event.