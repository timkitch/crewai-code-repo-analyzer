# Code Repository Analyzer

This project is a code analyzer and documentation generator. It uses a variety of tools and agents to analyze code repositories, generate comprehensive documentation, and create UML diagrams.

## Features

- **Code Analysis:** The `CodeAnalyzerTasks` class in `tasks.py` provides tasks for analyzing code repositories.
- **Documentation Generation:** The `code_documentation_agent` in `agents.py` generates comprehensive Markdown documentation for the analyzed code.
- **Diagram Generation:** The `PlantUMLDiagramGeneratorTool` in `tools/plantuml_generator.py` generates UML diagrams from PlantUML text.

## Technologies Used

- **Python 3.10**
- **crewai**: for implementing various AI tools and agents
- **pydantic**: for data validation
- **load-dotenv**: for loading environment variables
- **crewai-tools**: additional tools for the CrewAI framework
- **plantweb**: for generating diagrams using PlantUML
- **langchain_community**: for community-contributed tools and utilities
- **langchain_anthropic**: for integration with Anthropic's language models

## Getting Started

To get a local copy up and running, follow these steps:

### Prerequisites

- Python 3.10 or higher
- Poetry (for dependency management)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/timkitch/crewai-code-repo-analyzer.git
    cd crewai-code-repo-analyzer-master
    ```

2. Install the required dependencies:
    ```bash
    poetry install
    ```

### Usage

The main entry point of the application is `main.py`. Run this script to start the application.

```bash
python main.py
