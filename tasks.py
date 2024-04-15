from crewai import Task
from textwrap import dedent

from tools.git_tools import GitRepoFetchTools


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CodeAnalyzerTasks:
        
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 bonus!"

    def fetch_code_task(self, agent):
        return Task(
            description='Fetch the contents of a git repository hosting Python code.',
            agent=agent,
            async_execution=True,
            expected_output="""A string containing the contents of the repository.
            """,
            # tools=[GitRepoFetchTools.fetch_repo_content],
            inputs={'repository_url': 'repository_url'}  # Make sure this key matches the kickoff input
        )

    def analyze_code_task(self, agent, context):
        return Task(
            description='Analyze the fetched source code to understand its functionality, technology stack, and component relationships.',
            agent=agent,
            async_execution=True,
            context=context,
            expected_output="""A structured summary of the code's purpose, technologies used, and an analysis of major components.
            """
        )
        
    def document_code_task(self, agent, context, callback_function):
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
        return Task(
            description='Generate PlantUML diagram of requested type and convert to SVG.',
            agent=agent,
            context=context,
            expected_output="""SVG file containing the diagram.
            """,
            inputs={'diagram_type': 'diagram_type'},
            callback=callback_function
        )
