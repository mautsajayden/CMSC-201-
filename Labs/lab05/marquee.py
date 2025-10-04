import time



word = input("What text do you want to scroll? ")

num = len(word)
for i in range(num):
    time.sleep(0.25)
    print(word[i:] + word[:i])


#part 1

text = input("Enter a string: ")

text = text.strip()

parts = text.split()

joined = "".join(parts)

result = joined.lower()

print(result)


#part 2 

text = input("Enter a string: ")


text = text.strip()

parts = text.split()

word = "".join(parts)

word = word.lower()

for i in range(len(word)):
    print(word[i], sep=", ")
