from crewai import Task

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

    def analyze_code_task(self, agent):
        return Task(
            description="""
            Analyze the provided source code repository to understand its purpose, technologies used, and major components.
            This is the full source code: {repo_contents}.
            Identify and document the following:
            - The overall purpose of the project.
            - The technologies, APIs, and frameworks used.
            - All major components (e.g., classes, interfaces, functions, methods).
            - The interactions between these components.
            - The architectural patterns and design principles applied.
            """,
            expected_output="""
            A detailed analysis report covering the purpose of the project, the technologies, APIs, frameworks used, a list of components and their interactions, 
            and architectural patterns and design principles applied.
            """,
            agent=agent
        )
        
    def document_code_task(self, agent, context):
        return Task(
            description="""
                Generate a comprehensive Markdown document based on the analysis provided by the previous task. 
                Ensure the document follows the provided template for consistency, and includes a detailed breakdown
                of all components (e.g., classes, interfaces, functions) and their interactions.
                """,
            expected_output="""
                A comprehensive Markdown document describing the source code. The document should include the following sections:
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
            context=context,
            async_execution=False,
            output_file="design.md",
            agent=agent,
        ) 
    def diagram_task(self, agent):
        return Task(
            description="""
            Generate PlantUML {diagram_type} diagram for the provided design description.
            The diagram should be based on the full source code: {repo_contents} and only contain names of classes, interfaces, and functions as they
            appear within the source code.
            Ensure all names (e.g., classes, interfaces, functions) in the diagram exactly match those used in the source code.
            Do not make up any names when generating a diagram. All names must appear within the provided source code.
            The type of diagram (sequence, class, component) will be provided.
            Use the tools provided to you to find information to help you ensure you generate correct PlantUML syntax.
            """,
            agent=agent,
            expected_output="""PlantUML for the requested diagram that conforms to the PlantUML syntax, as per the PlantUML reference guide and examples.
            """,
            tools=[directory_read_tool, file_read_tool, plantuml_generator_tool],
            # callback=callback_function
        )
