import re


def arithmetic_arranger(problems):
    x = 0
    L1 = []
    Num_Match = re.search(r'[^a-zA-Z]', str(problems))
    Operator_Match = re.search("[^*/]", str(problems))

    for i in problems:
        P = problems[x].split(' ', 1)
        x += 1
        L1.append(P)
    print(L1)
    print(Num_Match)
    print(Operator_Match)

    if len(L1) > 5:
        return 'Error: Too many problems.'
    elif Num_Match:
        return 'Error: Numbers must only contain digits.'
    elif Operator_Match:
        return "Error: Operator must be '+' or '-'."
    elif len(L1) <= 5:
        return L1

    #  return arranged_problems
print(arithmetic_arranger(["32a + 698", "3801 - 2", "45 + 43", "123 + 49"]))
