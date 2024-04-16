from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

from tools.git_tools import GitRepoFetchTools


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CodeAnalyzerAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)
        self.OpenAIGPT4 = ChatOpenAI(model_name="gpt-4-turbo", temperature=0.2)

    def code_fetching_agent(self):
        return Agent(
            role='CodeFetcher',
            goal='Fetch the contents of a git repository hosting Python code.',
            backstory="""As an expert on GitHub, you understand how to extract the contents of a GitHub repository at {repository_url}. """,
            allow_delegation=True,
            verbose=True,
            max_iter=5,
            tools=[GitRepoFetchTools()],
            llm=self.OpenAIGPT4
        )
    def code_analysis_agent(self):
        return Agent(
            role='CodeAnalyzer',
            goal="""
            Analyze the provided source code and describe the technologies used and the functionality and core classes, functions and how they interact.
            """,
            backstory="""With a critical eye and a knack for distilling complex information on source codee, you provide insightful
            analyses of the source code of an entire github repository and describe the technologies used, as well as the functionality and the core classes, functions and how they interact.""",
            verbose=True,
            max_iter=5,
            allow_delegation=True,
            llm=self.OpenAIGPT4
        )
    def code_documentation_agent(self):
        return Agent(
            role='CodeDocumentor',
            goal='Generate a Markdown description of the repository, covering its purpose, technology stack, and component relationships',
            backstory="""As the final architect of the code design documentation, you meticulously arrange and format the content,
            ensuring a coherent and visually appealing presentation that clearly communicates the design of the app represented by the source code. Make sure to follow
            markdown format guidelines and maintain consistency throughout.""",
            verbose=True,
            max_iter=5,
            allow_delegation=False,
            llm=self.OpenAIGPT35
        )
    def code_diagramming_agent(self):
        return Agent(
            role='ComponentDiagrammer',
            goal='Generate PlantUML diagram of type {diagram_type} reflecting the design of the repository',
            backstory="""As an expert in both software design and PlantUML, you are able to use a description of a software design to
            generate PlantUML that can be used to visualize the component design of the app represented by the source code.""",
            verbose=True,
            max_iter=5,
            allow_delegation=False,
            llm=self.OpenAIGPT4
        )