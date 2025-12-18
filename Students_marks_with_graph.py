import pandas as pd
import matplotlib.pyplot as plt
#read csv file
data = pd.read_csv("students_marks.csv")

data["Maths"].fillna(data["Maths"].mean(), inplace=True)
data["Science"].fillna(data["Science"].mean(), inplace=True)
data["English"].fillna(data["English"].mean(), inplace=True)

#take average
data["Total"] = data["Maths"] + data["Science"] + data["English"]
data["Average"] = data["Total"] / 3

# Pass / Fail logic
result = []
for avg in data["Average"]:
    if avg >= 50:
        result.append("Pass")
    else:
        result.append("Fail")

data["Result"] = result

# Bar Graph
plt.figure()
plt.bar(data["Name"], data["Average"])
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")
plt.savefig("students_average_marks.png")
plt.show()

# Clean data save
data.to_csv("clean_students_marks.csv", index=False)

print("Project successfully run ")