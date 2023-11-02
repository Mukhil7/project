def arithmetic_arranger(problems, show_answers=True):
  if len(problems) > 5:
    return "Error: Too many problems"

  arranged_problems = []
  for problem in problems:
    operand1, operator, operand2 = problem.split()

    if operator not in ('+', '-'):
      return "Error: Operator must be '+' or '-'"

    if not operand1.isdigit() or not operand2.isdigit():
      return "Error: Numbers must only contain digits"

    if len(operand1) > 4 or len(operand2) > 4:
      return "Error: Numbers cannot be more than four digits"

    max_width = max(len(operand1), len(operand2)) + 2
    arranged_problems.append((operand1, operator, operand2, max_width))

  top_line, middle_line, bottom_line, answer_line = "", "", "", ""

  for problem in arranged_problems:
    operand1, operator, operand2, max_width = problem
    top_line += operand1.rjust(max_width) + "    "
    middle_line += operator + operand2.rjust(max_width - 1) + "    "
    bottom_line += "-" * max_width + "    "

    if show_answers:
      if operator == '+':
        result = str(int(operand1) + int(operand2))
      else:
        result = str(int(operand1) - int(operand2))
      answer_line += result.rjust(max_width) + "    "

  arranged_problems_str = top_line.rstrip() + "\n" + middle_line.rstrip(
  ) + "\n" + bottom_line.rstrip()

  if show_answers:
    arranged_problems_str += "\n" + answer_line.rstrip()

  return arranged_problems_str


# Input arithmetic problems from the user
problems = []
for i in range(4):
  problem = input("Enter an arithmetic problem (e.g., '32 + 698'): ")
  problems.append(problem)

# Call the arithmetic_arranger function without showing answers
arrangement = arithmetic_arranger(problems)
print(arrangement)

