char_no = int(input())

word = input()
alphapet = set("abcdefghijklmnopqrstuvwxyz")
word = set(word.lower())

if alphapet == word:
    print("YES")
else:
    print("NO")

