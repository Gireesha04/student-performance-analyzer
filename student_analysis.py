import pandas as pd
import matplotlib.pyplot as plt

# Read student data
data = pd.read_csv("data/students.csv")

# Calculate total and average marks
data["Total"] = data[["Python", "SQL", "Electronics"]].sum(axis=1)
data["Average"] = data[["Python", "SQL", "Electronics"]].mean(axis=1)

# Display student performance
print("\nStudent Performance Report")
print(data)

# Find the highest-performing student
top_student = data.loc[data["Average"].idxmax()]

print("\nTop Performing Student:")
print("Name:", top_student["Name"])
print("Average Marks:", round(top_student["Average"], 2))

# Create a bar chart
plt.bar(data["Name"], data["Average"])
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance Analysis")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
