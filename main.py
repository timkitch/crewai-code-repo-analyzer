from crewai import Crew, Process

from agents import CodeAnalyzerAgents
from tasks import CodeAnalyzerTasks

agents = CodeAnalyzerAgents()
tasks = CodeAnalyzerTasks()

from callbacks.file_io import save_design_doc
from callbacks.diagram_io import save_diagram

from utils.git_util import clone_repo, load_repo

# Instantiate the agents
code_analyzer = agents.code_analysis_agent()
code_documentor = agents.code_documentation_agent()
code_diagrammer = agents.code_diagramming_agent()

# Instantiate the tasks
analyze_code_task = tasks.analyze_code_task(code_analyzer)
document_code_task = tasks.document_code_task(
    code_documentor, [analyze_code_task]
)
diagram_task = tasks.diagram_task(code_diagrammer)

# Form the crew
crew = Crew(
    agents=[code_analyzer, code_documentor,code_diagrammer],
    tasks=[analyze_code_task, document_code_task, diagram_task],
    process=Process.sequential,
    # memory=True, # get "max tokens 8192 when enable memory here - enabled in agents instead"
    verbose=2,
    
)

# Kickoff the crew process with input from the user
repository_url = input("Please enter the GitHub repository URL: ")
local_repo = clone_repo(repository_url)
repo_contents = load_repo(local_repo)

# TODO: for sequence diagram support, may need input from user to select one or more sequences (e.g. Task human_input=True)
# diagram_options = ["component", "class", "sequence"]

diagram_options = ["component", "class"]
print("Please select a diagram type to generate:")
for i, option in enumerate(diagram_options, start=1):
    print(f"{i}. {option}")
selection = int(input("Enter the number of your selection: "))
diagram_type = diagram_options[selection - 1]


results = crew.kickoff(
    inputs={
        "repo_contents": repo_contents,
        "diagram_type": diagram_type,
    }
)

# Print the results
print(f"Crew Usage Metrics: {crew.usage_metrics}")
print(results)
