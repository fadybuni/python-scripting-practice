
success_count = 0
failed_count = 0
with open("auth.log","r") as log:
    lines = log.readlines()
for line in lines:
    if "SUCCESS" in line:
        success_count += 1
    if "FAILED" in line:
        failed_count += 1
with open("analyzed.txt","w") as result:
    result.write(f"Success Lines: {success_count}\n")
    result.write(f"Failed Lines: {failed_count}\n")
    result.write(f"Total Lines: {len(lines)}\n")
print("Log file has been analyzed")