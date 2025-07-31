🌍 Description
This Travel Itinerary Planner with Web Search is an AI-powered project I built using LangGraph, LangChain, Gradio, and Groq’s LLaMA 3.3 70B model. It allows users to generate a personalized day trip itinerary for any city by selecting their interests from a predefined list like Nature, Food, History, Art, and more.

The unique part of this project is that it not only uses an LLM to generate tailored travel plans but also integrates a web search mechanism to fetch real-time information related to the user’s interests. This enhances the accuracy and relevance of the itinerary by grounding it in live context.

The app is designed to be simple, fast, and user-friendly—making travel planning smarter with AI.

⚙️ How It Works
User Input
The user provides the name of a city they plan to visit and selects one or more interests (like Adventure, Nightlife, Relaxation, etc.).

Web Search Integration
A basic web search is performed using the DuckDuckGo HTML endpoint to find real-time information about the selected interests in the chosen city. This simulates live data integration and adds relevance to the itinerary.

Itinerary Generation with LLM
The user's city and interests are passed through a custom prompt to Groq’s LLaMA 3.3 70B model, which generates a personalized, bullet-pointed day plan that includes activities, places to visit, and suggestions based on preferences.

Gradio Interface
The results (both itinerary and web search summary) are displayed in a clean Gradio UI. The interface allows users to interact with the app easily—no code or technical steps required.

Installation and Setup
1. Clone the Repository
Start by cloning the repository to your local machine:

git clone https://github.com/JIVTESH28/travel-itinerary-planner.git
cd travel-itinerary-planner
2. Create a Virtual Environment
It is recommended to use a virtual environment to manage your dependencies. To create and activate a virtual environment:

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
3. Install Dependencies
Once your virtual environment is active, install the necessary dependencies:

pip install -r requirements.txt
4. Set Up the .env File
Create a .env file in the project root directory to store your Groq API key. Add the following content to the file:

GROQ_API_KEY=your_groq_api_key_here
Make sure to replace your_groq_api_key_here with your actual Groq API key.

Running the Application
To run the application, execute the following command:

python app.py
Once the application is running, open your browser and visit http://127.0.0.1:7860 to access the Gradio interface.

Requirements
The project depends on the following Python libraries, which are listed in requirements.txt:

gradio
langgraph
langchain-core
langchain-groq
python-dotenv
requests
To install these dependencies, run:

pip install -r requirements.txt
