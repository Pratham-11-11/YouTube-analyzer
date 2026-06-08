from textwrap import dedent
import streamlit as st

from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.youtube import YouTubeTools


def build_youtube_agent():

    groq_key = st.secrets["GROQ_API_KEY"]

    return Agent(
        name="YouTube Agent",

        model=Groq(
            id="qwen/qwen3-32b",
            api_key=groq_key
        ),

        tools=[YouTubeTools()],

        instructions=dedent("""
        You are an expert YouTube video analyst.

        Analyze the video and provide:
        - Video overview
        - Important topics
        - Timestamps
        - Key insights
        - Final summary

        Use markdown formatting.
        """),

        markdown=True,
    )
