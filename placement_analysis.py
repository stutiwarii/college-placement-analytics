import pandas as pd

df = pd.read_csv("data/placement_data.csv")

placement_rate = df['Placed'].value_counts(normalize=True) * 100
avg_package = df[df['Placed'] == 'Yes']['Package_LPA'].mean()

dept_summary = df.groupby('Department')['Placed'].value_counts().unstack()

print("Placement Rate (%)")
print(placement_rate)

print("\nAverage Package (LPA):", round(avg_package, 2))
print("\nDepartment-wise Placement Summary")
print(dept_summary)
