import json

class Collection:
    def __init__(self):
        try:
            with open("collection.json", "r") as f:
                self.collections = json.load(f)
        except FileNotFoundError:
            self.collections = []

    def all(self):
        return self.collections

    def get(self, id):
        return self.collections[id]

    def get_api(self, id):
        movie = [movie for movie in self.all() if movie['id'] == id]
        if movie:
            return movie[0]
        return []

    def create(self, data):
        data.pop('csrf_token')
        self.collections.append(data)

    def create_api(self, data):
        self.collections.append(data)
        self.save_col()

    def save_col(self):
        with open("collection.json", "w") as f:
            json.dump(self.collections, f)
    
    def update(self, id, data):
        data.pop('csrf_token')
        self.collections[id] = data
        self.save_col()

    def update_api(self, id, data):
        movie = self.get(id)
        if movie:
            index = self.collections.index(movie)
            self.collections[index] = data
            self.save_col()
            return True
        return False

    def delete(self, id):
        movie = self.get(id)
        if movie:
            self.collections.remove(movie)
            self.save_col()
            return True
        return False



collection = Collection()