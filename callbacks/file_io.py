
def save_design_doc(task_output):
    # Ensure the output is treated as a string
    str_content = str(task_output.raw_output)
    
    output_file = "./design.md"

    # Write the task output to the markdown file
    with open(output_file, "w") as file:
        file.write(str_content)
    file.close()
    
    print(f"Design description saved as {output_file}")
