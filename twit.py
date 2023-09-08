from user import User


class Twit:

    def __init__(self, _id: str, body: str, author: User):
        self._id = _id
        self.body = body
        self.author = author