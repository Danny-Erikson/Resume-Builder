from pathlib import Path

import json

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

# * Main route


with open('HardData.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


def build(extra_args: list):
    print("Build resume")
    render_resume(data)

# *Helper Functions


def render_resume(data):
    template_folder = Path("./templates")
    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    env = Environment(loader=FileSystemLoader(template_folder))
    template = env.get_template("highlight.html")

    html_content = template.render(data)

    html_path = output_folder / "resume.html"
    pdf_path = output_folder / "resume.pdf"

    html_path.write_text(html_content, encoding="utf-8")

    HTML(
        string=html_content,
        base_url=Path(".").resolve()
    ).write_pdf(pdf_path)

    print(f"Created: {pdf_path}")
