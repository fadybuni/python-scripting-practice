error_count = 0

with open("log.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    if "ERROR" in line:
        error_count += 1

with open("report.txt", "w") as report:
    report.write(f"Total lines: {len(lines)}\n")
    report.write(f"Error lines: {error_count} \n")
print("Report Generated")