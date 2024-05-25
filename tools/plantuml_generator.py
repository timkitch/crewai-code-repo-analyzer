from crewai_tools import BaseTool

from plantweb.render import render
import re

class PlantUMLDiagramGeneratorTool(BaseTool):
    name: str ="PlantUML Diagram Generator Tool"
    description: str = ("Accepts text that represents a diagram in PlantUML format "
         "and generates a SVG file from it.")
    
    def _run(self, text: str) -> str:
        try:
            output = render(
                text,
                engine='plantuml',
                format='svg',
                cacheopts={
                    'use_cache': False
                }
            )
        except Exception as e:
            raise ValueError(f"The provided text is not valid PlantUML: {e}")
        
        byte_string = output[0]

        # Step 2: Decode the byte string from 'us-ascii' to a Python string
        decoded_string = byte_string.decode('us-ascii')
        svg_output_file = './diagram.svg'
        
        with open(svg_output_file, 'w', encoding='utf-8') as file:
            file.write(decoded_string)
        file.close()
        
        print(f"Design diagram saved as {svg_output_file}")