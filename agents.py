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

    def code_fetching_agent(self):
        return Agent(
            role='CodeFetcher',
            goal='Fetch the contents of a git repository hosting Python code.',
            backstory="""As an expert on GitHub, you understand how to extract the contents of a GitHub repository at {repository_url}. """,
            allow_delegation=True,
            verbose=True,
            max_iter=5,
            tools=[GitRepoFetchTools()],
            llm=self.ClaudeHaiku,
            memory=True
        )
    def code_analysis_agent(self):
        return Agent(
            role='CodeAnalyzer',
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
        role='CodeDocumentor',
        goal="""
        Use the analysis provided by the CodeAnalyzer to generate a comprehensive Markdown document. 
        This document should include:
        - An introduction to the project, outlining its purpose.
        - A detailed description of the technology stack used.
        - A list of all major components (e.g., classes, functions, files).
        - Detailed documentation of each component, including its functionality and interactions with other components.
        - Ensure the document is well-structured and follows Markdown formatting guidelines.
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
            role='ComponentDiagrammer',
            goal="""
            Generate PlantUML diagram of type {diagram_type} reflecting the design of the repository. 
            Ensure all names (e.g., classes, interfaces, functions) in the diagram exactly match those used in the source code.
            Do not make up any names when generating a diagram. All names must appear within the provided source code.
            The type of diagram (e.g., sequence, class, component) will be provided.
            """,
            backstory="""As an expert in software design and PlantUML, your role is to create precise and accurate diagrams that visualize the 
            component design of the source code. Your diagrams should be clear, accurate, and true to the source.""",
            verbose=True,
            max_iter=5,
            allow_delegation=False,
            llm=self.OpenAIGPT4o,
            memory=True
        )