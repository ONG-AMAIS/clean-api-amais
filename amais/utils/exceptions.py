class Error(Exception):
    title: str

    def __init__(self, title: str):
        self.title = title
