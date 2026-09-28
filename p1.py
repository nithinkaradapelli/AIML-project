import csv
APP="Instagram"
min_spent = []

with open("digital_behaviour.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        min_spent.append(int(row["Instagram_Minutes"]))
minutes=min_spent[0:7]
total=sum(minutes)
average=total//len(minutes)
highest=max(minutes)
lowest=min(minutes)
count=0
for i in range(len(minutes)):
    if minutes[i]>average:
        count+=1
print(f"Count: {count}")
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")