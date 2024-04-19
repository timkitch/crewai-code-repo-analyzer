from crewai import Task
from textwrap import dedent

from tools.git_tools import GitRepoFetchTools


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
    
    def analyze_code_task(self, agent, context):
        # print("\n*****  Analyze Code Task Input:", context)
        return Task(
            description='Analyze the fetched source code to understand its functionality, technology stack, and component relationships.',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A structured summary of the code's purpose, technologies used, and an analysis of major components. List each component, its functionality, and how it interacts with other components. Components may be classes, functions or source filenames, as appropriate. 
            """
        )
        
    def document_code_task(self, agent, context, callback_function):
        # print("\n*****  Document Code Task Input:", context)
        return Task(
            description='Convert the analysis provided into a Markdown document that describes the repository comprehensively.',
            agent=agent,
            context=context,
            expected_output="""Markdown containing a detailed description of the repository.
                Example Output: 
                '## Pomodoro UI Project\n\n
                **Project Summary:
                ** A simple UI for the Pomodoro Technique.\n\n
                **Core Technologies Used:**\n\n
                - HTML, JavaScript\n\n
                **Main Components and Functionality:**\n\n
                ** The app uses a single HTML page which calls JavaScript functions to start, stop and reset the Pomodoro timer.\n\n'
            """,
            callback=callback_function
        ) 
    def diagram_task(self, agent, context, callback_function):
        # print("\n *****  Diagram Task Input:", context)
        return Task(
            description='Generate PlantUML diagram of requested type and convert to SVG.',
            agent=agent,
            context=context,
            expected_output="""PlantUML for the requested diagram.
            """,
            inputs={'diagram_type': 'diagram_type'},
            callback=callback_function
        )
