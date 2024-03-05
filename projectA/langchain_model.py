import os
import openai
from langchain.llms import OpenAI
from langchain.prompts  import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secretkey import openapi_key 

os.environ['OPENAI_API_KEY'] = openapi_key


def get_sentiment(text):
    """Perform sentiment analysis on the given text."""
    response = OpenAI.Completion.create(
        model="content-analysis",
        prompt=text,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def get_topics(text):
    """Identify key topics in the given text."""
    response = OpenAI.Completion.create(
        model="content-analysis",
        prompt=text,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def get_entities(text):
    """Extract relevant entities from the given text."""
    response = OpenAI.Completion.create(
        model="content-analysis",
        prompt=text,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def analyze_data(text):
    """Analyze the given text for sentiment, topics, and entities."""
    sentiment = get_sentiment(text)
    topics = get_topics(text)
    entities = get_entities(text)
    return {
        "sentiment": sentiment,
        "topics": topics,
        "entities": entities
    }
