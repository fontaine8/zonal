# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams():
    word= input("Enter first word:")
    anagram= input("Enter second word:")
    a=word.replace(' ','')
    b=anagram.replace(' ','')
    
    if len(a) != len(b): return False
    for char in word:
        if char not in anagram:
            return False
    return True
       

i = "yes"
while i == "yes":
    print(find_anagrams())
    i= input("Do you want to continue(yes/no:) :")

    

