import re

def extract_plantuml(raw_output):
    # Regular expression to find the required part
    match = re.search(r'(@startuml.*?@enduml)', raw_output, re.DOTALL)

    # Extract the matched part and handle newlines/quotes
    if match:
        extracted_text = match.group(1)
        # Replace any problematic characters if necessary (example shown for double quotes)
        extracted_text = extracted_text.replace('"', '\\"')
        return extracted_text
    else:
        print("No match found.")
        

test = """
'```plantuml\n@startuml\npackage "Confluence Q&A Application" {\n    [Streamlit UI] as Streamlit\n    [Environment Variables] as Dotenv\n    [ConfluenceQA] as ConfluenceQA\n    [Vector Database Operations] as VectorDB\n    [Document Retrieval and Ranking] as DocRetrieval\n    [Language Model Interaction] as LangModel\n\n    Streamlit ..> ConfluenceQA : uses\n    Streamlit ..> Dotenv : uses\n    ConfluenceQA ..> VectorDB : uses\n    ConfluenceQA ..> DocRetrieval : uses\n    ConfluenceQA ..> LangModel : uses\n}\n@enduml\n```\nThis PlantUML script represents the component design of the Confluence Q&A Application. Each component and their interactions are clearly depicted, reflecting the software\'s architecture based on the provided description.'
"""

print(test + "\n\n")
print(extract_plantuml(test))


import re

s = '```plantuml\n@startuml\npackage "Confluence Q&A Application" {\n    [Streamlit UI] as Streamlit\n    [Environment Variables] as Dotenv\n    [ConfluenceQA] as ConfluenceQA\n    [Vector Database Operations] as VectorDB\n    [Document Retrieval and Ranking] as DocRetrieval\n    [Language Model Interaction] as LangModel\n\n    Streamlit ..> ConfluenceQA : uses\n    Streamlit ..> Dotenv : uses\n    ConfluenceQA ..> VectorDB : uses\n    ConfluenceQA ..> DocRetrieval : uses\n    ConfluenceQA ..> LangModel : uses\n}\n@enduml\n```\nThis PlantUML script represents the component design of the Confluence Q&A Application. Each component and their interactions are clearly depicted, reflecting the software\'s architecture based on the provided description.'

match = re.search('```plantuml\n(.+?)\n```', s, re.DOTALL)
if match:
    plantuml_script = match.group(1)
    print(plantuml_script)