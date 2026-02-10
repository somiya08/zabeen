sentence=input("enter a string")
vowels="aeiouAEIOU"
for ch in sentence:
    if ch in vowels:
        print(ch,end=" ")