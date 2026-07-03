from tinydb import TinyDB, Query
from tinydb.table import Document


class DB:
    def __init__(self, path="data/resume_data.json"):
        self.db = TinyDB(path)

        self.personal = self.db.table("personal")
        self.education = self.db.table("education")
        self.projects = self.db.table("projects")
        self.experience = self.db.table("experience")
        self.tech_stack = self.db.table("tech_stack")

    def update_personal(self, doc_id, data):
        self.personal.upsert(Document(data, doc_id=doc_id))
