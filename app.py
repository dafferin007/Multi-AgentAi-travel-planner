import gradio as gr
from typing import TypedDict, Annotated, List
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import requests
from dotenv import load_dotenv
import os


load_dotenv()

class PlannerState(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], "The messages in the conversation"]
    city: str
    interests: List[str]
    itinerary: str
    web_search_results: str


groq_api_key = os.getenv("GROQ_API_KEY")


llm = ChatGroq(
    temperature=0,
    groq_api_key=groq_api_key,  
    model_name="llama-3.3-70b-versatile"
)


search_llm = ChatGroq(
    temperature=0,
    groq_api_key=groq_api_key,  
    model_name="llama-3.3-70b-versatile"
)


itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel assistant. Create a day trip itinerary for {city} based on the user's interests: {interests}. Provide a brief, bulleted itinerary."),
    ("human", "Create an itinerary for my day trip."),
])


web_search_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Search the web for details on {interests} in {city}."),
    ("human", "Find the best resources, landmarks, and activities related to {interests} in {city}. Provide a summary."),
])

#web search function
def search_web(interests: str, city: str) -> str:
    search_query = f"{interests} in {city}"
    search_url = f"https://duckduckgo.com/html/?q={search_query}"
    response = requests.get(search_url)
    
    # This part processes the DuckDuckGo HTML response. Ideally, use APIs like SerpAPI for structured data.
    if response.status_code == 200:
        return "Results found. Please check the web for more details."
    else:
        return "Sorry, no results found."


def input_city(city: str, state: PlannerState) -> PlannerState:
    return {
        **state,
        "city": city,
        "messages": state['messages'] + [HumanMessage(content=city)],
    }

def input_interests(interests: List[str], state: PlannerState) -> PlannerState:
    return {
        **state,
        "interests": interests,
        "messages": state['messages'] + [HumanMessage(content=", ".join(interests))],
    }

def create_itinerary(state: PlannerState) -> str:
    response = llm.invoke(itinerary_prompt.format_messages(city=state['city'], interests=", ".join(state['interests'])))
    state["itinerary"] = response.content
    state["messages"] += [AIMessage(content=response.content)]
    return response.content

def perform_web_search(state: PlannerState) -> str:
    search_results = search_web(", ".join(state["interests"]), state["city"])
    state["web_search_results"] = search_results
    state["messages"] += [AIMessage(content=search_results)]
    return search_results


def travel_planner(city: str, interests: List[str]):

    state = {
        "messages": [],
        "city": "",
        "interests": [],
        "itinerary": "",
        "web_search_results": "",
    }


    state = input_city(city, state)
    state = input_interests(interests, state)

    # Perform web search
    web_search_results = perform_web_search(state)
    
    # Generate the itinerary
    itinerary = create_itinerary(state)

    # Return the combined output
    return f"Itinerary:\n\n{itinerary}\n\nWeb Search Results:\n{web_search_results}"


interface = gr.Interface(
    fn=travel_planner,
    theme=gr.themes.Citrus(),  
    inputs=[
        gr.Textbox(label="Enter the city for your day trip"),
        gr.CheckboxGroup(
            choices=["Nature", "History", "Food", "Art", "Adventure", "Relaxation", "Shopping", "Nightlife"],
            label="Select Your Interests"
        ),
    ],
    outputs=gr.Textbox(label="Generated Itinerary & Web Search Results", lines=15, interactive=False),
    title="🌍Travel Itinerary Planner with Web Search",
    description="Enter a city and select your interests to generate a personalized itinerary and perform a web search for more details."
)


interface.launch()
