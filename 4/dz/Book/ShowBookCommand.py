from ..CommandInterface import CommandInterface

class ShowBookCommand(CommandInterface):
    def __init__(self, repository):
        self.repo = repository

    def execute(self, data):
        title = data[0]
        book = self.repo.read(title)
        if book:
            print(book)
        else:
            print(f"Book '{title}' not found.")