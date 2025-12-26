count = {}
amount = int(input("Please enter how many of the most common words you want to see: "))

with open("wordlist.txt", 'r') as file:
    for line in file:
        for word in line.split():
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
    

with open("result.txt", "w") as result:
    print(f"Here are the top {amount} most common words and how many times they occur: \n")
    top_five = sorted(count.items(), key=lambda x:x[1], reverse =True) [:amount]
    for word, freq in top_five:
        result.write(f"{word}:{freq}\n")
print("Done. ")