class CommentsRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "comment": "hello world", "category": True}
        ]

    def get_all(self):
        return self.comments

    def append(self, comment):
        if "id" not in comment or not comment["id"]:
            comment["id"] = self.get_next_id()
        self.comments.append(comment)
        return self.comments

    def get_next_id(self):
        return len(self.comments) + 1
