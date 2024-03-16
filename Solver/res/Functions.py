"""
    Determines the type of operation based on the user's answers.

    Args:
    - user_answers: A tuple representing the user's answers to questions about the operation.

    Returns:
    - A string indicating the type of operation.
"""
def TypeOperation(user_answers):

    answers = {
        (True, True, True): "PERMUTACIONES CON REPETICIÓN",
        (True, True, False): "PERMUTACIONES ORDINARIAS",
        (True, False, True): "VARIACIONES CON REPETICIÓN",
        (True, False, False): "VARIACIONES ORDINARIAS",
        (False, False, True): "COMBINACIONES CON REPETICIÓN",
        (False, False, False): "COMBINACIONES ORDINARIAS",
    }

    return answers[tuple(user_answers)]

"""
    Calculates the factorial of a given number.

    Args:
    - number: An integer for which the factorial is calculated.

    Returns:
    - The factorial of the input number.
"""
def Factorial(number):
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
def VariationsWithRepetition (total, groups):
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
def VariationsWithoutRepetition (total, groups):
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
def PermutationsWithoutRepetition (total):
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
def PermutationsWithRepetition (total, iterations):
    while True:
        try:
            repetitions = []
            for i in range(0, iterations):
                repetition = int(input("Cuantas veces se repite: "))
                repetitions.append(repetition)
            denominator = 1
            for repetition in repetitions:
                denominator *= Factorial(repetition)

            return Factorial(total) / denominator
        
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
def CombinationsWithoutRepetition (total, groups):
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
def CombinationsWithRepetition (total, groups):
    while True:
        try:
            return Factorial(total + groups - 1) / (Factorial(groups) * Factorial(total - 1))
        except ValueError:
            print("Error: Ingrese un número válido.")