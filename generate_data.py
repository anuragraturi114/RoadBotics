import csv
import random

# Generate random road assessment data
data = []
for road_id in range(1, 11):
    road_name = f"Road {road_id}"
    assessment = random.randint(50, 100)
    data.append((road_name, assessment))

# Write data to CSV file
with open('data/road_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Road', 'Assessment'])
    csvwriter.writerows(data)
