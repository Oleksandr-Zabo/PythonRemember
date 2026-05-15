class RepositoryInterface:
    def create(self, data):
        raise NotImplementedError("Method create() not implemented")

    def read_all(self):
        raise NotImplementedError("Method readAll() not implemented")

    def read(self, id):
        raise NotImplementedError("Method read() not implemented")

    def update(self, id, data):
        raise NotImplementedError("Method update() not implemented")

    def delete(self, id):
        raise NotImplementedError("Мethod delete() not implemented")