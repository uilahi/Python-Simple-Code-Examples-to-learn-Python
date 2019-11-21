x="hey i am umair yoo how you doing fellas"
print(x)
sent=x.split()
blank=""

f=[]

for word in sent:
    z = ""
    count = 0
    if word[0] in "aeiou":
        z=word+"yay"
        f.append(z)
    else:
        for letter in word:
            if letter not in "aeiou":
                index_of_vovel = count+1
            else:
                break
        consonants = word[:index_of_vovel]
        vovel_start = word[index_of_vovel:]
        new_word = vovel_start + consonants+"yay"
        f.append(new_word)
new_sentence=" ".join(f)
print(new_sentence)