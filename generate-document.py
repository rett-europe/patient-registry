import os
import re

# Path to the directory where your markdown files are stored
markdown_directory = './docs/'
output_file = './output_document.md'

# Generate the list of markdown files in the directory (only files with .md extension)
markdown_files = [f for f in os.listdir(markdown_directory) if f.endswith('.md')]

# Regular expression to match image references
image_pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')

def fix_image_paths(markdown_content):
    """
    Adjust image paths by prepending 'docs/' to the image URLs if they are relative.
    """
    def replace_path(match):
        alt_text = match.group(1)
        image_path = match.group(2)
        # Only adjust if the image path is relative (doesn't start with 'http', '/', 'docs/')
        if not image_path.startswith(('http', '/', 'docs/')):
            image_path = 'docs/' + image_path
        return f'![{alt_text}]({image_path})'

    return image_pattern.sub(replace_path, markdown_content)

# Function to concatenate markdown files
def concatenate_markdown_files(file_list, output_path):
    with open(output_path, 'w', encoding='utf-8') as outfile:
        for file_name in file_list:
            file_path = os.path.join(markdown_directory, file_name)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                    # Fix the image paths in the markdown content
                    content = fix_image_paths(content)
                    outfile.write(content)
                    outfile.write("\n\n")  # Add spacing between files
            else:
                print(f"File {file_name} does not exist. Skipping.")

    print(f"Combined markdown file created: {output_path}")

# Run the function to combine files
concatenate_markdown_files(markdown_files, output_file)
