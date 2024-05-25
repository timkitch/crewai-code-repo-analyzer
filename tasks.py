from crewai import Task
from textwrap import dedent

from tools.git_tools import GitRepoFetchTools

from crewai_tools import DirectoryReadTool, FileReadTool

from tools.plantuml_generator import PlantUMLDiagramGeneratorTool

directory_read_tool = DirectoryReadTool(directory='./plantuml_help')
file_read_tool = FileReadTool()
plantuml_generator_tool = PlantUMLDiagramGeneratorTool()


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CodeAnalyzerTasks:
        
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 bonus!"
    
    # expected_output="""A JSON array containing the name of each file in the repository, the contents of that file and
    #         the programming language used within that file. Example of the expected output:
    #         [
    #             {
    #                 "source_filename": "/home/timkitch/ai-projects/crewai-code-repo-analyzer/remote_repo/confluence_rag_app/constants.py",
    #                 "programming_language": "python",
    #                 "source_file_contents": "# Constants\nEMB_OPENAI_ADA = \"text-embedding-ada-002\"\nEMB_SBERT = None # Chroma takes care\n\nLLM = \"gpt-3.5-turbo-0125\"\n# LLM = \"gpt-3.5-turbo\"\n# LLM = \"gpt-4-turbo-preview\"\n\nDB_DIRECTORY = \".chroma_db\"\n\nDB_COLLECTION_NAME = \"confluence_qa\""
    #             }
    #         """,

    def fetch_code_task(self, agent):
        return Task(
            description='Fetch the contents of a git repository hosting Python code.',
            agent=agent,
            async_execution=True,
            expected_output="""A JSON array containing the name of each file in the repository, the contents of that file and
            the programming language used within that file. 
            """,
            # tools=[GitRepoFetchTools.fetch_repo_content],
            inputs={'repository_url': 'repository_url'}  # Make sure this key matches the kickoff input
        )
    
    def analyze_code_task(self, agent):
        return Task(
            description="""Analyze the provided source code repository to understand its purpose, technologies used, and major components.
            This is the full source code: {repo_contents}
            """,
            expected_output="A detailed analysis report covering the technologies, APIs, frameworks used, and a list of components and their interactions.",
            agent=agent
        )
        
    def document_code_task(self, agent, callback_function):
        return Task(
            description="""
                Generate a comprehensive Markdown document based on the analysis provided by the CodeAnalyzer. 
                Ensure the document follows the provided template for consistency, and includes a detailed breakdown
                of all components (e.g., classes, interfaces, functions) and their interactions.
                """,
            expected_output="""
                # Project Name

                ## Overview
                Provide a brief overview of the project's purpose and functionality.

                ## Technology Stack
                List and describe the technologies, frameworks, and libraries used in the project.

                - **Language:** [Programming Language]
                - **Frameworks:** [Frameworks Used]
                - **Libraries:** [Libraries Used]
                - **Tools:** [Tools Used]

                ## Directory Structure
                Outline the directory structure of the project with brief descriptions of each directory and file.
                Here's an example of the directory structure output:
                ├── src/
                │ ├── main.py - Entry point of the application
                │ ├── utils.py - Utility functions
                │ └── ...
                ├── tests/
                │ ├── test_main.py - Tests for main.py
                │ └── ...
                └── README.md - Project documentation
            """,
            agent=agent,
            # async_execution=False,
            callback=callback_function
        ) 
    def diagram_task(self, agent):
        # print("\n *****  Diagram Task Input:", context)
        return Task(
            description="""
            Generate PlantUML {diagram_type} diagram for the provided design description.
            The diagram should be based on the full source code: {repo_contents} and only contain names of classes, interfaces, and functions as they
            appear within the source code.
            """,
            agent=agent,
            expected_output="""PlantUML for the requested diagram that conforms to the PlantUML syntax, as per the PlantUML reference guide and examples.
            """,
            tools=[directory_read_tool, file_read_tool, plantuml_generator_tool],
            # callback=callback_function
        )
