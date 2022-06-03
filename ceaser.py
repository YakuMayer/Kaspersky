text = input()
alph_up = "".join(chr(i) for i in range(ord("A"), ord("Z") + 1))
alph_low = "".join(chr(i) for i in range(ord("a"), ord("z") + 1))
questions = []
text0 = text.split("?")
dot = 0
dots = []
for a in text0:
    q = a.split(".")
    questions.append(q[-1])
    a = a.replace(q[len(q)-1], "")
for b in range(len(text)):
    if text[b] == ".":
        dot = b
    if text[b] == "?":
        dots.append(dot)
dots.append(len(text))
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
            if i+1  <  len(dots):
                for z in text[dots[i]:dots[i+1]]:
                    if z in alph_up:
                        ans += alph_up[(alph_up.index(z) - x)%26]
                    elif z in alph_low:
                        ans += alph_low[(alph_low.index(z) - x)%26]
                    else:
                        ans += z
            answer += ans
            break
print(answer)
