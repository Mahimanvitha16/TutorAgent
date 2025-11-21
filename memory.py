import json

class MemoryStore:
    def _init_(self, filename="student_memory.json"):
        self.filename = filename
        self.data = {}

        try:
            with open(self.filename, "r") as file:
                self.data = json.load(file)
        except:
            self.data = {}

    def save(self, topic, result):
        self.data[topic] = result
        with open(self.filename, "w") as file:
            json.dump(self.data, file, indent=4)

    def load(self, topic):
        return self.data.get(topic, None)
