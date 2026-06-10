from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


# NOTE: We will use tinyDB, this is just to get the template set up
# Icons from devicon
resume_data = {
    "name": "Daniel Erikson",
    "email": "derikson413@gmail.com",
    "phone": "555-555-5555",
    "address": "123 Main Street, Anytown, NY 12345",
    "location": "Los Angeles",
    "languages": [
        {
            "name": "Python",
            "logo": "assets/logos/python.svg",
            "highlight": 1
        },
        {
            "name": "Java",
            "logo": "assets/logos/java.svg",
            "highlight": 0
        },
        {
            "name": "JavaScript",
            "logo": "assets/logos/javascript.svg",
            "highlight": 0
        },
        {
            "name": "HTML",
            "logo": "assets/logos/html.svg",
            "highlight": 0
        },
        {
            "name": "CSS",
            "logo": "assets/logos/css.svg",
            "highlight": 0
        },
        {
            "name": "C",
            "logo": "assets/logos/c.svg",
            "highlight": 0
        },
        {
            "name": "C++",
            "logo": "assets/logos/c++.svg",
            "highlight": 0
        },
        {
            "name": "Go",
            "logo": "assets/logos/go.svg",
            "highlight": 0
        }
    ],
    "frameworks": [
        {
            "name": "React",
            "logo": "assets/logos/react.svg",
            "highlight": 0
        },
        {
            "name": "Node.js",
            "logo": "assets/logos/node.svg",
            "highlight": 0
        },
    ],
    "database": [
        {
            "name": "PostgreSQL",
            "logo": "assets/logos/postgre.svg",
            "highlight": 1
        },
        {
            "name": "MySQL",
            "logo": "assets/logos/mysql.svg",
            "highlight": 0
        },
        {
            "name": "SQLite",
            "logo": "assets/logos/sqlite.svg",
            "highlight": 0
        },
    ],
    "tools": [
        {
            "name": "Git",
            "logo": "assets/logos/git.svg",
            "highlight": 1
        }
    ],

    "projects": [
        {
            "name": "Service Logger",
            "tech": "Python, SQLite, Tkinter",
            "bullets": [
                "Built a desktop app to track vehicle mileage, services, and fuel logs.",
                "Used SQLite relationships to connect cars, mileage entries, and fuel data.",
                "Generated reports with mileage and cost-per-mile calculations."
            ]
        },
        {
            "name": "Resume Builder",
            "tech": "Python, Jinja2, WeasyPrint",
            "bullets": [
                "Created a template-based resume generator.",
                "Rendered resume data into HTML and exported it as a PDF."
            ]
        }
    ],

    "experience": [
        {
            "title": "Full Stack Developer",
            "company": "Personal Projects",
            "dates": "2025 - Present",
            "bullets": [
                "Built web and desktop applications using Python, React, and SQL.",
                "Designed database schemas and user interfaces for project-based tools."
            ]
        }
    ],

    "education": [
        {
            "type": "Associate in Science",
            "title": "Full Stack Web Development",
            "school": "Pasadena City College",
            "date": "2025",
            "description": "Completed coursework in full stack web development, covering client-side and server-side programming, secure web application development, database management, testing, deployment, and maintenance. Built foundational skills in HTML, CSS, JavaScript, React, Node.js, SQL, Python, and responsive web design."
        }
    ]
}


def render_resume(data):
    template_folder = Path(".")
    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    env = Environment(loader=FileSystemLoader(template_folder))
    template = env.get_template("template.html")

    html_content = template.render(data)

    html_path = output_folder / "resume.html"
    pdf_path = output_folder / "resume.pdf"

    html_path.write_text(html_content, encoding="utf-8")

    HTML(
        string=html_content,
        base_url=Path(".").resolve()
    ).write_pdf(pdf_path)

    print(f"Created: {pdf_path}")


if __name__ == "__main__":
    render_resume(resume_data)
