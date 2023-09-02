from user import User


class Twit:

    def __init__(self, id: str, body: str, author: User):
        self.id = id
        self.body = body
        self.author = author
