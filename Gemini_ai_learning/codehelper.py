import google.generativeai as genai

class CodeHelper:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')
    def explain_code(self, code):
        """Explain what code does"""
        prompt = f"""
        Explain this Python code in simple terms:
        ```python
        {code}
        ```
        Include:
        1. What the code does
        2. How it works step by step
        3. Any important concepts used
        """
        response = self.model.generate_content(prompt)
        return response.text
    def fix_code(self, code, error_message=""):
        """Help fix broken code"""
        prompt = f"""
        This Python code has an issue:
        ```python
        {code}
        ```
        Error message: {error_message}
27
        Please:
        1. Identify the problem
        2. Explain why it's wrong
        3. Provide corrected code
        4. Explain the fix
        """
        response = self.model.generate_content(prompt)
        return response.text
    def generate_code(self, description):
        """Generate code from description"""
        prompt = f"""
        Write Python code for: {description}
        Include:
        - Well-commented code
        - Error handling
        - Example usage
        """
        response = self.model.generate_content(prompt)
        return response.text


# Usage
from config import GEMINI_API_KEY
helper = CodeHelper(GEMINI_API_KEY)




# Example 1: Explain code
code = """
students = [
    {"name": "Alice", "age": 20, "grades": [85, 90, 88]},
    {"name": "Bob", "age": 22, "grades": [78, 82, 75]},
    {"name": "Charlie", "age": 21, "grades": [92, 95, 90]},
    {"name": "Diana", "age": 20, "grades": [88, 85, 90]}
]


# Part A: Calculate and add average grade for each student
print("\n--- Part A: Calculate Averages ---")
for student in students:
    avg = sum(student["grades"]) / len(student["grades"])
    student["average"] = avg

print("\nStudents with average data print")
for student in students:
    print(f"{student['name']}: {round(student['average'],2)}")



# Part B: Filter Top Students
print("\n--- Part B: Top Students (Average > 85) ---")
top_students = [s["name"] for s in students if s["average"] > 85]
print("Top students:", top_students)


# Part C: All Grades Analysis
print("\n--- Part C: All Grades Analysis ---")
all_grades = [grade for s in students for grade in s["grades"]]
print("All grades:", all_grades)

class_avg = sum(all_grades) / len(all_grades)
print(f"Class average: {round(class_avg,2)}")


# Part D: Rankings
print("\n--- Part D: Rankings ---")
sorted_students = sorted(students, key=lambda s: s["average"], reverse=True)
print("Rankings:")
for i, s in enumerate(sorted_students, 1):
    print(f"{i}. {s['name']}: {round(s['average'],2)}")


# Part E: Grade Distribution
print("\n--- Part E: Grade Distribution ---")
def get_letter_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

grade_distribution = {}
for student in students:
    letter = get_letter_grade(student["average"])
    if letter not in grade_distribution:
        grade_distribution[letter] = 0
    grade_distribution[letter] += 1


print("Grade Distribution:")
grade_ranges = {
    'A': '(90+)',
    'B': '(80-89)',
    'C': '(70-79)',
    'D': '(60-69)',
    'F': '(<60)'
}
for grade in ['A', 'B', 'C', 'D', 'F']:
    count = grade_distribution.get(grade, 0)
    print(f"{grade} {grade_ranges[grade]}: {count} students")
"""




# explanation = helper.explain_code(code)
# print(explanation)

# Example 3: generate code
description = "A Python function that takes a list of numbers and returns the list sorted in ascending order."
generated_code = helper.generate_code(description)
print(generated_code)