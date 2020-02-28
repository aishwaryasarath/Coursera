import csv

with open('software.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        #print(row['name'], row['depart'])
        print(dict(row))
        #print(("{} has {} users").format(row["name"], row["users"]))



# users = [{"name":"Name1", "username" : "soln", "depart":"IT"},
#          {"name":"Name2", "username" : "nm2", "depart":"UI"},
#          {"name":"Name3", "username" : "nm3", "depart":"Dev"}]
# keys = ["name", "username", "depart"]
# with open('by_department.csv','w') as by_dept:
#     writer = csv.DictWriter(by_dept, fieldnames=keys)
#     writer.writeheader()
#     writer.writerows(users)
