"""
    Determines the type of operation based on the user's answers.

    Args:
    - user_answers: A tuple representing the user's answers to questions about the operation.

    Returns:
    - A string indicating the type of operation.
"""
def TypeOperation(user_answers: tuple):

    answers = {
        (True, True, True): "permutación con repetición",
        (True, True, False): "permutaciones ordinarias",
        (True, False, True): "variaciones con repetición",
        (True, False, False): "variaciones ordinarias",
        (False, False, True): "combinación con repetición",
        (False, False, False): "combinaciones ordinarias",
    }

    return answers[tuple(user_answers)]

"""
    Calculates the factorial of a given number.

    Args:
    - number: An integer for which the factorial is calculated.

    Returns:
    - The factorial of the input number.
"""
def Factorial(number: int):
  fact = 1
  for i in range(1, number + 1):
      fact *= i
  return fact

# VARIATIONS
"""
    Calculates the number of variations with repetition.

    Args:
    - total: Total number of elements.
    - groups: Size of the groups.

    Returns:
    - The number of variations with repetition.
"""
def VariationsWithRepetition (total: int, groups: int):
    while True:
        try:
            return total ** groups
        except ValueError:
            print("Error: Ingrese un número válido.")

"""
    Calculates the number of variations without repetition.

    Args:
    - total: Total number of elements.
    - groups: Size of the groups.

    Returns:
    - The number of variations without repetition.
"""
def VariationsWithoutRepetition (total: int, groups: int):
    while True:
        try:
            return Factorial(total) / Factorial(total - groups)
        except ValueError:
            print("Error: Ingrese un número válido.")

# PERMUTATIONS
"""
    Calculates the number of permutations without repetition.

    Args:
    - total: Total number of elements.

    Returns:
    - The number of permutations without repetition.
"""
def PermutationsWithoutRepetition (total: int):
    while True:
        try:
            return Factorial(total)
        except ValueError:
            print("Error: Ingrese un número válido.")

"""
    Calculates the number of permutations with repetition.

    Args:
    - total: Total number of elements.
    - iterations: Number of different repeated elements.

    Returns:
    - The number of permutations with repetition.
"""
def PermutationsWithRepetition (total: int, repited_numbers: tuple):
    while True:
        try:
            pass
        except ValueError:
            print("Error: Ingrese un número válido.")

# COMBINATIONS
"""
    Calculates the number of combinations without repetition.

    Args:
    - total: Total number of elements.
    - groups: Size of the groups.

    Returns:
    - The number of combinations without repetition.
"""
def CombinationsWithoutRepetition (total: int, groups: int):
    while True:
        try:
            return Factorial(total) / (Factorial(groups) * Factorial(total - groups))
        except ValueError:
            print("Error: Ingrese un número válido.")

"""
    Calculates the number of combinations with repetition.

    Args:
    - total: Total number of elements.
    - groups: Size of the groups.

    Returns:
    - The number of combinations with repetition.
"""
def CombinationsWithRepetition (total: int, groups: int):
    while True:
        try:
            return Factorial(total + groups - 1) / (Factorial(groups) * Factorial(total - 1))
        except ValueError:
            print("Error: Ingrese un número válido.")