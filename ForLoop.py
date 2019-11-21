d={
    1:["abc","abd","bcd"],
    2:["sde","asqs","cfvrv"],
    3:["caq","cdcw","aqa"],
    4:["ccc","caca","jhjja"],
}
output=[]
for i in d:
    ls =d[i]
    for j in ls:
        for k in j:
            if k == "a":
                if j not in output:
                     output.append(j)

print(output)
print(len(output))







