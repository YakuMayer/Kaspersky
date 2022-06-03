text = input()
alph_up = "".join(chr(i) for i in range(ord("A"), ord("Z") + 1))
alph_low = "".join(chr(i) for i in range(ord("a"), ord("z") + 1))
questions = []
text0 = text.split("?")
text = []
for a in text0:
    q = a.split(".")
    questions.append(q[len(q)-1])
    a = a.replace(q[len(q)-1], "")
    text.append(a)
text.pop(0)
text.append("")
print(text)
answer = ""
for i in range(len(questions)):
    for x in range(27):
        ans = ""
        for j in questions[i]:
            if j in alph_up:
                ans += alph_up[(alph_up.index(j) - x)%26]
            elif j in alph_low:
                ans += alph_low[(alph_low.index(j) - x)%26]
            else:
                ans += j
        print(ans)
        print("Текст осмысленный? y/n")
        result = input()
        if result == "y":
            ans = ""
            print(i)
            for z in text[i]:
                if z in alph_up:
                    ans += alph_up[(alph_up.index(z) - x)%26]
                elif z in alph_low:
                    ans += alph_low[(alph_low.index(z) - x)%26]
                else:
                    ans += z
            answer += ans + "?"
            break
print(answer)
