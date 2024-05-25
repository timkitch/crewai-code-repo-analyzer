from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI

from langchain_anthropic import ChatAnthropic

from dotenv import load_dotenv
load_dotenv()

from tools.git_tools import GitRepoFetchTools


class CodeAnalyzerAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.2)
        
        self.OpenAIGPT4o = ChatOpenAI(model_name="gpt-4o", temperature=0.2)
        
        self.ClaudeHaiku = ChatAnthropic(
            model="claude-3-haiku-20240307"
        )
        self.ClaudeSonnet = ChatAnthropic(
            model="claude-3-sonnet-20240229"
        )

    def code_analysis_agent(self):
        return Agent(
            role='Code Analyzer',
            goal="""
            Thoroughly analyze the provided source code. Identify and document the following:
            - The overall purpose of the project.
            - The technologies, APIs, and frameworks used.
            - All major components (e.g., classes, interfaces, functions, methods).
            - The interactions between these components.
            - The architectural patterns and design principles applied.
            """,
            backstory="""With a critical eye and a knack for distilling complex information, you provide insightful analyses of the source code. 
            Your mission is to deeply understand the structure and technologies used in the project and to describe the core components and their interactions.""",
            verbose=True,
            max_iter=5,
            allow_delegation=False,
            llm=self.OpenAIGPT4o,
            memory=True,
        )
    def code_documentation_agent(self):
        return Agent(
        role='Code Documentor',
        goal="""
        Use the analysis provided by the Code Analyzer to generate a comprehensive Markdown document describing the source code. 
        """,
        backstory="""With a knack for distilling complex information into clear and concise documentation, your task is to create a 
        comprehensive and well-structured Markdown document that accurately represents the analyzed source code.""",
        verbose=True,
        max_iter=5,
        allow_delegation=False,
        llm=self.OpenAIGPT4o,
        memory=True
    )
    def code_diagramming_agent(self):
        return Agent(
            role='Component Diagrammer',
            goal="""
            Generate PlantUML diagram reflecting the design based on the contents of a given source code repository. 
            """,
            backstory="""As an expert in software design and PlantUML, your role is to create precise and accurate diagrams that visualize the 
            component design of the source code. Your diagrams should be clear, accurate, and true to the source.""",
            verbose=True,
            max_iter=5,
            allow_delegation=False,
            llm=self.OpenAIGPT4o,
            memory=True
        )