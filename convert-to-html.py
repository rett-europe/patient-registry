import markdown2

# Path to your concatenated markdown file
input_markdown_file = 'output_document.md'
output_html_file = 'output_document.html'
css_file = 'style.css'  # External CSS file

# Read the markdown file
with open(input_markdown_file, 'r', encoding='utf-8') as f:
    markdown_content = f.read()

# Convert markdown to HTML
html_content = markdown2.markdown(markdown_content, extras=["tables", "fenced-code-blocks", "footnotes"])

# Add the link to the external CSS and HTML header/footer
html_output = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Markdown Document</title>
    <link rel="stylesheet" type="text/css" href="{css_file}">
</head>
<body>
    {html_content}
</body>
</html>
"""

# Save the HTML to a file
with open(output_html_file, 'w', encoding='utf-8') as f:
    f.write(html_output)

print(f'HTML file saved as {output_html_file}')
