import glob
import os
from jinja2 import Template

content_files = glob.glob("content/*.html")

pages = []

def page_list():
    for html_file in content_files:
        file_name = os.path.basename(html_file)
        name_only, extension = os.path.splitext(file_name)

        pages.append({
        "filename": "content/" + file_name,
        "title": name_only,
        "output": "docs/" + file_name,
        })
    
    print(pages)
    return pages


def open_content():
    return open(pages[0]['filename']).read()

    
def apply_content():
    index_html = open(pages[0]['filename']).read()
    base_template = open("templates/base.html").read()
    template = Template(base_template)
     
    
def write_output():
    for page in pages:
        file_path = pages[0]['filename']
        page_html = template.render(
            title = pages[0]['title'],
            content = index_html,
            pages = pages,
            selected = pages[0]['output']
        )
    open(page['output'], "w+").write(page_html)	
    
