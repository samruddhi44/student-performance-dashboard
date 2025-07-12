
import pandas as pd
import matplotlib.pyplot as plt

# Load student data
df = pd.read_csv("students.csv")

# Calculate total, average, and result
df["Total"] = df["Maths"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3
df["Result"] = df["Average"].apply(lambda x: "Pass" if x >= 40 else "Fail")

# Assign grade
def assign_grade(avg):
    if avg >= 85:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "D"
df["Grade"] = df["Average"].apply(assign_grade)

# Show topper
topper = df.loc[df["Total"].idxmax()]
print("Topper:", topper["Name"], "- Total:", topper["Total"])

# Show full data
print("\nFull Student Performance:\n")
print(df)

# Plotting: Marks of each student
df.plot(x="Name", y=["Maths", "Science", "English"], kind="bar")
plt.title("Subject-wise Marks")
plt.ylabel("Marks")
plt.tight_layout()
plt.show()

# Pie chart: Pass vs Fail
pass_count = df["Result"].value_counts()
pass_count.plot(kind="pie", autopct="%1.1f%%", colors=["green", "red"])
plt.title("Pass vs Fail")
plt.ylabel("")
plt.show()
