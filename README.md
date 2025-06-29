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

