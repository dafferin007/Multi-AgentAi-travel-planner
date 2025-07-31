
# 🌍 Travel Itinerary Planner with Web Search

This project is a **Travel Itinerary Planner** designed to generate personalized day trip itineraries based on the city and user interests. In addition to generating itineraries, the app performs a web search for more details on the selected interests in the specified city.

## Features

- Generates a personalized day trip itinerary using advanced language models.
- Performs web searches to find relevant information about the user’s interests in a given city.
- User-friendly interface powered by **Gradio**.
- Customizable options for cities and interests, including Nature, History, Food, Art, Adventure, Relaxation, Shopping, and Nightlife.

## Installation and Setup

### 1. Clone the Repository

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/JIVTESH28/travel-itinerary-planner.git
cd travel-itinerary-planner
```

### 2. Create a Virtual Environment

It is recommended to use a virtual environment to manage your dependencies. To create and activate a virtual environment:

```bash
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```

### 3. Install Dependencies

Once your virtual environment is active, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 4. Set Up the .env File

Create a `.env` file in the project root directory to store your Groq API key. Add the following content to the file:

```plaintext
GROQ_API_KEY=your_groq_api_key_here
```

Make sure to replace `your_groq_api_key_here` with your actual Groq API key.

## Running the Application

To run the application, execute the following command:

```bash
python app.py
```

Once the application is running, open your browser and visit [http://127.0.0.1:7860](http://127.0.0.1:7860) to access the Gradio interface.

## Requirements

The project depends on the following Python libraries, which are listed in `requirements.txt`:

```plaintext
gradio
langgraph
langchain-core
langchain-groq
python-dotenv
requests
```

To install these dependencies, run:

```bash
pip install -r requirements.txt
```
## Contributing

Contributions to the project are welcome. If you'd like to contribute, feel free to fork the repository and submit a pull request. Please make sure to follow the project's coding style and include relevant tests where applicable.

