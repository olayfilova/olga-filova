class MyDict:
    def __init__(self):
        self.data = {}

    def add(self, key, value):
        self.data[key] = value

    def find(self, key):
        return self.data.get(key, None)

    def update(self, key, value):
        if key in self.data:
            self.data[key] = value

    def print_dict(self):
        for key, value in self.data.items():
            print(f"{key}: {value}")

