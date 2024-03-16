def TypeOperation(user_answers):

    answers = {
        (True, True, True): "permutación con repetición",
        (True, True, False): "permutaciones ordinarias",
        (True, False, True): "variaciones con repetición",
        (True, False, False): "variaciones ordinarias",
        (False, False, True): "combinación con repetición",
        (False, False, False): "combinaciones ordinarias",
    }

    return answers[tuple(user_answers)]

def Factorial(number):
  fact = 1
  for i in range(1, number + 1):
      fact *= i
  return fact

# VARIATIONS
def VariationsWithRepetition(total, groups):
    while True:
        try:
            return total ** groups
        except ValueError:
            print("Error: Ingrese un número válido.")

def VariationsWithoutRepetition(total, groups):
    while True:
        try:
            return Factorial(total) / Factorial(total - groups)
        except ValueError:
            print("Error: Ingrese un número válido.")

# PERMUTATIONS
def PermutationsWithoutRepetition(total):
    while True:
        try:
            return Factorial(total)
        except ValueError:
            print("Error: Ingrese un número válido.")

def PermutationsWithRepetition(total, iterations):
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
def CombinationsWithoutRepetition(total, groups):
    while True:
        try:
            return Factorial(total) / (Factorial(groups) * Factorial(total - groups))
        except ValueError:
            print("Error: Ingrese un número válido.")

def CombinationsWithRepetition(total, groups):
    while True:
        try:
            return Factorial(total + groups - 1) / (Factorial(groups) * Factorial(total - 1))
        except ValueError:
            print("Error: Ingrese un número válido.")