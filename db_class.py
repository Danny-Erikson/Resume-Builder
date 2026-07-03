from tinydb import TinyDB, Query


class DB:
    def __init__(self, path="resume_data.json"):
        self.db = TinyDB(path)

        self.personal = self.db.table("personal")
        self.education = self.db.table("education")
        self.projects = self.db.table("projects")
        self.experience = self.db.table("experience")
        self.tech_stack = self.db.table("tech_stack")
