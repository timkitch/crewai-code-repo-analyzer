## TextRank Web Application

**Project Summary:**
This repository houses a Python-based web application that processes and ranks text data. The application utilizes Streamlit to create an interactive web interface where users can input questions and receive answers based on content extracted from a Confluence page.

**Core Technologies Used:**

- Python
- Streamlit
- dotenv
- langchain

**Main Components and Functionality:**

### app.py
- **Purpose**: The main entry point of the web application responsible for user interactions, session state management, and integration of processing modules.
- **Key Components**:
    - `ConfluenceQA`: Handles embeddings, models, and QA logic.
    - `load_confluence(config)`: Ingests and vectorizes Confluence documents.
    - Streamlit functions for UI components.
- **Interactions**:
    - Utilizes `ConfluenceQA` for backend QA processing.
    - Manages user inputs and configurations.
    - Calls `load_confluence` to process Confluence data.

### utils.py
- **Purpose**: Provides utility functions to support the main application.
- **Key Components**:
    - `pretty_print_docs(docs)`: Formats and prints document content.
- **Interactions**:
    - Supports formatting output for user presentation.

### rerank.py
- **Purpose**: Contains logic for advanced text processing and document ranking.
- **Key Components**:
    - Components from the `langchain` library for prompts and document embeddings.
    - Functions and classes for document retrieval and compression.
- **Interactions**:
    - Enhances QA responses by processing and ranking text data.

**Summary:**
The application is structured around `app.py` for user interactions and result display, utilizing `rerank.py` for text processing and ranking. `utils.py` provides document formatting support. Streamlit integration enhances the user experience, making complex text processing accessible.