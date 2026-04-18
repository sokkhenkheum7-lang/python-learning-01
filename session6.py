ch = input("Enter a single alphabet (a,e,i,o,u): ")
if len(ch) == 1 and ch.isalpha():
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print(" It is vowel.")
    else:
        print(" It is consonant.")
