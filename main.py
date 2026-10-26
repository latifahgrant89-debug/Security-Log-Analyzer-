filename = "Sample_login_attempts.txt"

successful_logins = 0
failed_logins = 0
failed_ips = {}

#opens the file
file = open(filename, "r")
failed_file = open("failed_attempts.txt", "w")

#reads through each login attempt record

for line in file:
    if "LOGIN_SUCCESSFUL" in line:
        successful_logins = seccessful_logins + 1
    elif "LOGIN_FAILED" in line:
        failed_logins = failed_logins + 1

        #saves all the failed login records
        failed_file.write(line)

        #singles out the IP address
        parts = line.split()
        ip = parts[4].replace("ip=","")

        #counts all the failed attempts for the each IP address
        if ip in failed_ips:
            failed_ips[ip] = failed_ips[ip] + 1
        else:
            failed_ips[ip] = 1
#closes all the files
file.close()
failed_file.close()

#shows all the security reports
print("SECURITY LOG ANALYZER")
print("---------------------")
print("Successful logins:", successful_logins)
print("Failed logins:", failed_logins)

print("\nFailed login attempts by IP:")

for ip in failed_ips:
    print(ip, "-", failed_ips[ip], "failed attempts")

print("\nSuspicious IP addresses:")

found_suspicious = False

for ip in failed_ips:
    if failed_ips[ip] >= 3:
        print(ip, "-", failed_ips[ip], "failed attempts")
        found_suspicious = True

if found_suspicious == False:
    print("No IP addresses met the alert threshold.")

print("\nFailed login events saved to failed_attempts.txt")
