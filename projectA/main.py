import streamlit as st
import langchain_model
# 
import os
import openai
from langchain.llms import OpenAI
from langchain.prompts  import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from secretkey import openapi_key 

os.environ['OPENAI_API_KEY'] = openapi_key
# 

def main():
    st.title("Competitor Analysis Tool")
    st.write("Enter the target sector and competitor name to get insights:")

    sector = st.text_input("Target Sector", "e.g., Technology, Retail, Finance")
    competitor_name = st.text_input("Competitor Name", "e.g., Apple, Amazon, Google")

    if st.button("Get Competitor Insights"):
        # Placeholder for calling Langchain model
        # Replace this with actual code to call Langchain model
        insights = generate_insights(sector, competitor_name)
        display_insights(insights)

def generate_insights(sector, competitor_name):
    # Placeholder function to generate insights
    return {
        "summary": f"Summary of {competitor_name}'s SWOT analysis...",
        "detailed_reports": {
            "sentiment_analysis": "Sentiment analysis results...",
            "key_topics": "Key topics...",
            "identified_entities": "Identified entities..."
        }
    }

def display_insights(insights):
    st.write("### Summary:")
    st.write(insights["summary"])

    st.write("### Detailed Reports:")
    st.write("#### Sentiment Analysis:")
    st.write(insights["detailed_reports"]["sentiment_analysis"])

    st.write("#### Key Topics:")
    st.write(insights["detailed_reports"]["key_topics"])

    st.write("#### Identified Entities:")
    st.write(insights["detailed_reports"]["identified_entities"])


# 
# 
# 

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
# 
# 
# 

if __name__ == "__main__":
    main()
