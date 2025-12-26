word = input("Please input what word you would like to scan for: ")

count = 0
total_words = 0 

with open("notes.txt","r") as file:
    for line in file:
        split_words = line.split()
        total_words += len(split_words)
        for words in split_words:
            if words.lower() == word.lower():
                count += 1
with open("scanned.txt","w") as report:
    report.write(
        f"'{word}' was mentioned {count} times out of a total of {words} words."
    )
if count > 0:
    print("Keywords have been detected")
else:
    print("No keywords have been detected")
        