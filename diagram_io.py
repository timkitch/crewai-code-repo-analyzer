from plantweb.render import render
import re

class TaskOutput:
        def __init__(self, raw_output):
            self.raw_output = raw_output

def save_diagram(task_output):
    # Ensure the output is treated as a string
    str_content = str(task_output.raw_output)
    
    raw_task_output_file = './raw_task_output.txt'
    with open(raw_task_output_file, 'w', encoding='utf-8') as file:
        file.write(str_content)
    file.close()
    
    str_content = extract_plantuml(str_content)
    plantuml_output_file = './diagram.puml'
    with open(plantuml_output_file, 'w', encoding='utf-8') as file:
        file.write(str_content)
    file.close()
    
    output = render(
        str_content,
        engine='plantuml',
        format='svg',
        cacheopts={
            'use_cache': False
        }
    )
    
    byte_string = output[0]

    # Step 2: Decode the byte string from 'us-ascii' to a Python string
    decoded_string = byte_string.decode('us-ascii')
    svg_output_file = './diagram.svg'
    
    with open(svg_output_file, 'w', encoding='utf-8') as file:
        file.write(decoded_string)
    file.close()
    
    print(f"Design diagram saved as {svg_output_file}")
    
def extract_plantuml(raw_output):
    match = re.search('```plantuml\n(.+?)\n```', raw_output, re.DOTALL)
    if match:
        plantuml_script = match.group(1)
    
    return plantuml_script
        
    # # Regular expression to find the required part
    # match = re.search(r'(@startuml.*?@enduml)', raw_output, re.DOTALL)

    # # Extract the matched part and handle newlines/quotes
    # if match:
    #     extracted_text = match.group(1)
    #     # Replace any problematic characters if necessary (example shown for double quotes)
    #     extracted_text = extracted_text.replace('"', '\\"')
    #     return extracted_text
    # else:
    #     raise ValueError("No match found for PlantUML start and end annotations.")
    
# str_content = '```plantuml\n@startuml\npackage "Confluence Q&A Application" {\n    [Streamlit UI] as Streamlit\n    [Environment Variables] as Dotenv\n    [ConfluenceQA] as ConfluenceQA\n    [Vector Database Operations] as VectorDB\n    [Document Retrieval and Ranking] as DocRetrieval\n    [Language Model Interaction] as LangModel\n\n    Streamlit ..> ConfluenceQA : uses\n    Streamlit ..> Dotenv : uses\n    ConfluenceQA ..> VectorDB : uses\n    ConfluenceQA ..> DocRetrieval : uses\n    ConfluenceQA ..> LangModel : uses\n}\n@enduml\n```\nThis PlantUML script represents the component design of the Confluence Q&A Application. Each component and their interactions are clearly depicted, reflecting the software\'s architecture based on the provided description.'

# # Create an instance of TaskOutput
# task_output = TaskOutput(str_content)

# save_diagram(task_output)
    
    