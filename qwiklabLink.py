qwik_lab_link = input("Enter quik lab without .pem: ")
remote_ip = input("Enter remote ip: ")
student_id = input("Enter student id: ")
chmod_str = "chmod 600 ~/Downloads/"
ssh_str = "ssh -i ~/Downloads/"

print("Chmod string: {}{}.pem".format(chmod_str, qwik_lab_link))
print("ssh string: {}{}.pem {}@{}".format(ssh_str, qwik_lab_link, student_id,
                                 remote_ip))

# qwikLABS-L2400-11425744
# student-01-a8e5062efa02
# 104.197.202.189

