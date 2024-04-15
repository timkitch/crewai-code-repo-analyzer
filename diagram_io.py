from plantweb.render import render
import re

def save_diagram(task_output):
    # Ensure the output is treated as a string
    str_content = str(task_output.raw_output)
    str_content = extract_plantuml(str_content)
    
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
    output_file = './diagram.svg'
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(decoded_string)
    file.close()
    
    print(f"Design diagram saved as {output_file}")
    
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