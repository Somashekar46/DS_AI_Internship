import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
print("Original Grades:")
print(grades)
print("\nMissing Values (True indicates missing):")
print(grades.isnull())
filled_grades = grades.fillna(0)
print("\nGrades After Filling Missing Values with 0:")
print(filled_grades)
filtered_scores = filled_grades[filled_grades > 60]
print("\nScores Greater Than 60:")
print(filtered_scores)
