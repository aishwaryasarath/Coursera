import csv
# f = open("csv_file.txt")
# csv_f = csv.reader(f)
# for row in csv_f:
#     name, phone, role = row
#     print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
# f.close()

hosts = [["workstation.local", "121.111.111.111"], ["webserver.cloud",
                                                    "344.555.666"]]
with open('hosts.csv', 'w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)

# cat hosts.csv
