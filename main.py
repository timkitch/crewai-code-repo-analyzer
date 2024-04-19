from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI

from agents import CodeAnalyzerAgents
from tasks import CodeAnalyzerTasks

agents = CodeAnalyzerAgents()
tasks = CodeAnalyzerTasks()

from callbacks.file_io import save_design_doc
from callbacks.diagram_io import save_diagram

# Instantiate the agents
code_fetcher = agents.code_fetching_agent()
code_analyzer = agents.code_analysis_agent()
code_documentor = agents.code_documentation_agent()
code_diagrammer = agents.code_diagramming_agent()

# Instantiate the tasks
fetch_code_task = tasks.fetch_code_task(code_fetcher)
analyze_code_task = tasks.analyze_code_task(code_analyzer, [fetch_code_task])
document_code_task = tasks.document_code_task(
    code_documentor, [analyze_code_task], save_design_doc
)
diagram_task = tasks.diagram_task(code_diagrammer, [document_code_task], save_diagram)

# Form the crew
crew = Crew(
    agents=[code_fetcher, code_analyzer, code_documentor, code_diagrammer],
    tasks=[fetch_code_task, analyze_code_task, document_code_task, diagram_task],
    process=Process.sequential,
    memory=True,
    verbose=True,
)

# Kickoff the crew process with input from the user
repository_url = input("Please enter the GitHub repository URL: ")
diagram_type = input(
    "Please enter a diagram type to generate (e.g. one of component, class, sequence, etc.): "
)
results = crew.kickoff(
    inputs={
        "repository_url": repository_url,
        "diagram_type": diagram_type,
    }
)

# Print the results
print(f"Crew Usage Metrics: {crew.usage_metrics}")
print(results)
