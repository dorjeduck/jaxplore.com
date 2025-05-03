import os
from datetime import datetime


def generate_paper_info():
    # Output directory specified in the script
    output_dir = "../content/resources/papers/"

    # Ask for user input step by step
    title = input("Enter the title of the paper: ")
    date_str = input("Enter the date (YYYYMMDD): ")
    
    # Validate the date format
    try:
        date_obj = datetime.strptime(date_str, '%Y%m%d')
        date_formatted = date_obj.strftime('%Y-%m-%d')  # Format it as YYYY-MM-DD
        weight = int(date_str)  # Directly use the input as weight
    except ValueError:
        print("Invalid date format. Please use YYYYMMDD.")
        return
    
    web = input("Enter the web link (e.g., https://arxiv.org/abs/1511.05952): ")
    
    authors = input("Enter the authors (comma-separated if more than one): ")
    # Handle case for only one author
    if ',' in authors:
        author_line = f"author = \"{authors}\""
    else:
        author_line = f"author = \"{authors}\""
    
    # Ask for the full abstract (multi-line input)
    print("Enter the abstract (finish with Ctrl+D or Ctrl+Z):")
    
    # Capture multi-line input for abstract
    abstract = ""
    try:
        while True:
            line = input()  # Capture input line by line
            abstract += line + "\n"
    except EOFError:
        # When the user finishes input (Ctrl+D or Ctrl+Z)
        pass

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Prepare the template content
    # Use a string with escaped quotes for the abstract
    template = f"""
+++
title = "{title}"
date = "{date_formatted}"
weight = {weight}

template="resources/paper.html"

[extra]
web = "{web}"

{author_line}

abstract = \"\"\"{abstract}\"\"\"
+++
"""
    
    # Specify the file path for saving
    output_file = os.path.join(output_dir, f"{title.replace(' ', '_').lower()}.md")
    
    # Write to file
    with open(output_file, 'w') as file:
        file.write(template)
    
    print(f"File has been generated: {output_file}")

# Call the function to generate the paper info
generate_paper_info()