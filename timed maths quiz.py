import random
import time

OPERATOR = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND =  15
TOTAL_PROBLEM = 5


def generate_problem():

    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATOR)

    expression = str(left) + " " + operator + " " + str(right)
    answer = eval(expression)
    return expression, answer

wrong =  0
start = input("press enter to start!")
print("------------------------------------")
start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expression, answer = generate_problem()
    while True:
        guess = input("problem #" + str(i + 1) + ": " + expression + "= ")
        if guess == str(answer):
            break
        wrong += 1
end_time = time.time()
total_time = round(end_time - start_time, 2)

print("---------------------------------------")
print("nice work! you finsied in ", total_time, "seconds")
