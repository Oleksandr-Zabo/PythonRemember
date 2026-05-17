class BackpackCaller:
    def __init__(self, matches, salt):
        self.matches = matches
        self.salt = salt

    def __call__(self, action='no_act', count=1):
        if action == 'fire':
            self.matches -= count

        if action == 'salute':
            self.salt -= count

        return self

    def __str__(self):
        return f"Matches left: {self.matches}, Salute Salt left : {self.salt}"