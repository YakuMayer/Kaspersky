import math
text = input()
key = input()
alph = "qwertyuiopasdfghjklzxcvbnm_{}1234567890"
key = key * math.ceil(len(text)/len(key))
ans = ""
for i in range(len(text)):
    ans += alph[((alph.find(text[i]) + 1) + (alph.find(key[i]) + 1)) % len(alph) - 1]
print(ans)
