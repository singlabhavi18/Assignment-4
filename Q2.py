import random
for i in range(10):
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    ans = num1 * num2
    print("Question", str(i+1) + ":", num1, "*", num2, "= ", end = "")
    g_ans = int(input())
    if g_ans == ans:
        print("Right!")
    else:
        print("Wrong!. The answer is", ans)
