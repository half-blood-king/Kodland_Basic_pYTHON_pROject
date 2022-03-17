line=int(input("How many lines will there be ?"))
poem=str()
for i in range(0,line):
    lines=input()
    poem=poem+lines+'\n'

vowel=['a','e','i','o','u','A','E','I','O','U']
noise=['!','`','$','%',',','^','&amp;','*','(',')','.',';',':','|']
vowel_len=0
consonants=0
for i in poem:
    if i in vowel:
        vowel_len=vowel_len+1
    elif i==' ' or i=='\n' or i in noise:
        continue
    else:
        consonants=consonants+1
print("Number of vowels :",vowel_len)
print("Number of consonants :",consonants)