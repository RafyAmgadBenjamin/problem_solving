n = int(input())
sentence = ""
for item in range(n):
    if item == 0:
        sentence += "I hate"
    elif item % 2 == 0:
        sentence += " that I hate"
    elif item % 2 != 0:
        sentence += " that I love"
sentence += " it"
print(sentence)
