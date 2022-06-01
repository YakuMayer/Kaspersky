text = input()
text = text[11:]
text = text[:-1]
text = text.split("|")
alph = "".join(chr(i) for i in range(ord("A"), ord("Z") + 1))
ans = "yourflagis{"
for i in text:
    ans += alph[int(i) - 1]
print(ans + "}")
