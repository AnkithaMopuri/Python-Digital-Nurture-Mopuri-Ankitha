import json

class Gradebook:
    def __init__(self):
        self.students = {}

    def add_grade(self, name, grade):
        if not (0 <= grade <= 100):
            print("Invalid grade")
            return

        if name not in self.students:
            self.students[name] = []

        self.students[name].append(grade)

    def calculate_gpa(self, grades):
        return sum(grades) / len(grades) if grades else 0

    def class_average(self):
        all_grades = [g for grades in self.students.values() for g in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def save(self, file="grades.json"):
        with open(file, "w") as f:
            json.dump(self.students, f)

    def load(self, file="grades.json"):
        try:
            with open(file, "r") as f:
                self.students = json.load(f)
        except FileNotFoundError:
            print("No saved data found")


# Example usage
g = Gradebook()

g.add_grade("Anki", 85)
g.add_grade("Anki", 90)
g.add_grade("John", 70)

print("Anki GPA:", g.calculate_gpa(g.students["Anki"]))
print("Class Average:", g.class_average())

g.save()