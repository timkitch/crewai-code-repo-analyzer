from plantweb.render import render
import re


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
    match = re.search(r'@startuml.*?@enduml', raw_output, re.DOTALL)
    if match:
        plantuml_script = match.group(0)
    else:
        # raise exception
        raise Exception('PlantUML script not found in raw output')
    
    return plantuml_script

def main():
    extract_plantuml("```plantuml@startuml\nAlice -> Bob: Hello\n@endumlgarbagh= yadhhndfkm 12$#")

if __name__ == "__main__":
    main()

    