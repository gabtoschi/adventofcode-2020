import modules.aoc as AOC

input = AOC.readDayInput('18')

def getPostfixNotation(expression, precedence):
    tokens = list(expression.replace(' ', ''))
    postfix = []
    operators = []

    for token in tokens:
        if token.isnumeric():
            postfix.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                postfix.append(operators.pop())

            operators.pop()
        else: # operator
            while operators and operators[-1] != '(' and precedence[token] <= precedence[operators[-1]]:
                postfix.append(operators.pop())

            operators.append(token)

    while operators:
        postfix.append(operators.pop())

    return postfix

def evaluateExpression(expression, precedence):
    postfix = getPostfixNotation(expression, precedence)
    operands = []

    for token in postfix:
        if token.isnumeric():
            operands.append(int(token))
        else:
            val2 = operands.pop()
            val1 = operands.pop()
            operands.append(eval(str(val1) + token + str(val2)))

    return operands[0]

## FIRST STAR
precedence = { '+': 1, '*': 1 }
result = sum([ evaluateExpression(exp, precedence) for exp in input ])
AOC.printDayAnswer(1, result)

## SECOND STAR
precedence = { '+': 2, '*': 1 }
result = sum([ evaluateExpression(exp, precedence) for exp in input ])
AOC.printDayAnswer(2, result)