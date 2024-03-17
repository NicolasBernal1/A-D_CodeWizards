import re

def isTuple(text: str):
    """
    Checks if the given text is a valid tuple.

    Args:
    - text: A string representing the text to be checked.

    Returns:
    - True if the text is a valid tuple, False otherwise.
    """
    regularExpresson = r'^\s*\(?\s*[^\s,]+(\s*,\s*[^\s,]+)*\s*\)?\s*$'
    return bool(re.match(regularExpresson, text))

def strToTuple(text: str) -> tuple:
    """
    Converts a comma-separated string into a tuple of stripped values.
    
    Args:
        text (str): The comma-separated string to convert.
        
    Returns:
        tuple: A tuple of stripped values from the input string.
    """
    return tuple(int(char.strip()) for char in text.split(",") if char.strip())


def TypeOperation(user_answers: tuple) -> str:
    """
    Determines the type of operation based on the user's answers.

    Args:
    - user_answers: A tuple representing the user's answers to questions about the operation.

    Returns:
    - A string indicating the type of operation.
    """
    answers = {
        (True, True, True): "permutación con repetición",
        (True, True, False): "permutaciones ordinarias",
        (True, False, True): "variaciones con repetición",
        (True, False, False): "variaciones ordinarias",
        (False, False, True): "combinación con repetición",
        (False, False, False): "combinaciones ordinarias",
    }

    return answers[tuple(user_answers)]

def Factorial(number: int) -> float:
    """
    Calculates the factorial of a given number.

    Args:
    - number: An integer for which the factorial is calculated.

    Returns:
    - The factorial of the input number.
    """
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

def VariationsWithRepetition (total: int, groups: int) -> float:
    """
    Calculates the number of variations with repetition.

    Args:
    - total: Total number of elements.
    - groups: Size of the groups.

    Returns:
    - The number of variations with repetition.
    """
    while True:
        try:
            return total ** groups
        except ValueError:
            print("Error: Ingrese un número válido.")

def VariationsWithoutRepetition (total: int, groups: int) -> float:
    """
    Calculates the number of variations without repetition.

    Args:
    - total: Total number of elements.
    - groups: Size of the groups.

    Returns:
    - The number of variations without repetition.
    """
    while True:
        try:
            return Factorial(total) / Factorial(total - groups)
        except ValueError:
            print("Error: Ingrese un número válido.")

def PermutationsWithoutRepetition (total: int) -> float:
    """
    Calculates the number of permutations without repetition.

    Args:
    - total: Total number of elements.

    Returns:
    - The number of permutations without repetition.
    """
    while True:
        try:
            return Factorial(total)
        except ValueError:
            print("Error: Ingrese un número válido.")

def PermutationsWithRepetition (total: int, repited_numbers: tuple) -> float:
    """
    Calculates the number of permutations with repetition.

    Args:
    - total: Total number of elements.
    - repited_numbers: A tuple representing the number of different repeated elements.

    Returns:
    - The number of permutations with repetition.
    """
    while True:
        try:
            numerator = Factorial(total)
            dem_factorial = map(Factorial, repited_numbers)
            denominator = 1
            for i in dem_factorial:
                denominator *= i
            return numerator/denominator
        except ValueError:
            print("Error: Ingrese un número válido.")

def CombinationsWithoutRepetition (total: int, groups: int) -> float:
    """
    Calculates the number of combinations without repetition.

    Args:
    - total: Total number of elements.
    - groups: Size of the groups.

    Returns:
    - The number of combinations without repetition.
    """
    while True:
        try:
            return Factorial(total) / (Factorial(groups) * Factorial(total - groups))
        except ValueError:
            print("Error: Ingrese un número válido.")

def CombinationsWithRepetition (total: int, groups: int) -> float:
    """
    Calculates the number of combinations with repetition.

    Args:
    - total: Total number of elements.
    - groups: Size of the groups.

    Returns:
    - The number of combinations with repetition.
    """
    while True:
        try:
            return Factorial(total + groups - 1) / (Factorial(groups) * Factorial(total - 1))
        except ValueError:
            print("Error: Ingrese un número válido.")