def arithmetic_arranger():
    print("Welcome to the Arithmetic Arranger!")
    print("Please enter up to 5 arithmetic problems, separated by commas.")
    print("Each problem should be in the format 'a + b' or 'a - b'.")
    print("For example: '3 + 5, 2 - 4, 10 + 2' ***Include spaces too***")
    print("Note: Each number should be no more than 4 digits long.")

    problems = input("Enter your problems: ").split(', ')

    if len(problems) > 5:
        return "Error: Too many problems."

    display_answers = input("Do you want to display the answers? (yes/no): ")
    if display_answers.lower()!= 'yes' and display_answers.lower()!= 'no':
        return "Error: Invalid input. Please enter 'yes' or 'no'."

    display_answers = display_answers.lower() == 'yes'

    first_operands = []
    second_operands = []
    operators = []
    results = []

    for problem in problems:
        if '+' in problem:
            operands = problem.split(' + ')
            operator = '+'
        elif '-' in problem:
            operands = problem.split(' - ')
            operator = '-'
        else:
            return "Error: Operator must be '+' or '-'."

        if len(operands)!= 2:
            return "Error: Invalid problem format. Please use 'a + b' or 'a - b'."

        first_operand = operands[0].strip()
        second_operand = operands[1].strip()
        
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        first_operands.append(first_operand)
        second_operands.append(second_operand)
        operators.append(operator)
        
        if operator == '+':
            result = str(int(first_operand) + int(second_operand))
        else:
            result = str(int(first_operand) - int(second_operand))
        results.append(result)
    
    first_line = []
    second_line = []
    dashes_line = []
    results_line = []

    for i in range(len(problems)):
        first_operand = first_operands[i]
        second_operand = second_operands[i]
        operator = operators[i]
        result = results[i]
        
        length = max(len(first_operand), len(second_operand)) + 2
        first_line.append(first_operand.rjust(length))
        second_line.append(operator + second_operand.rjust(length - 1))
        dashes_line.append('-' * length)
        results_line.append(result.rjust(length))

    arranged_problems = '  '.join(first_line) + '\n' + '  '.join(second_line) + '\n' + '  '.join(dashes_line)
    if display_answers:
        arranged_problems += '\n' + '  '.join(results_line)
    
    return arranged_problems

print(arithmetic_arranger())