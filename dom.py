import random
import math

CROSSOVER_RATE = 0.8
GENERATIONS = 150
POPULATION_SIZE = 1000
PI = math.pi

def generate_initial_x1():
    temp1 = random.randint(0, 2400) / 100.0
    r = temp1 / 2 if temp1 > 12 else -(temp1 / 2)
    return r

def generate_initial_x2():
    temp1 = random.randint(0, 1200) / 100.0
    r = temp1 / 2 if temp1 > 6 else -(temp1 / 2)
    return r

def crossover(population):
    crossover_size = int(POPULATION_SIZE * CROSSOVER_RATE / 2)
    indices = random.sample(range(POPULATION_SIZE), k=crossover_size * 2)
    for i in range(crossover_size):
        idx1 = indices[2*i]
        idx2 = indices[2*i + 1]
        population[idx1], population[idx2] = population[idx2], population[idx1]

def mutate(population):
    mutation_size = 200
    indices = random.sample(range(POPULATION_SIZE), k=mutation_size)
    for idx in indices:
        population[idx]["x1"] += random.randint(0, 2)
        population[idx]["x2"] += random.randint(0, 2)

def calculate_fitness(population):
    for i in range(POPULATION_SIZE):
        x1 = population[i]["x1"]
        x2 = population[i]["x2"]
        if -12 <= x1 <= 12 and -6 <= x2 <= 6:
            fitness = 21.5 + x1 * math.sin(4 * PI * x1) + x2 * math.sin(20 * PI * x2)
        else:
            fitness = 0
        population[i]["fitness"] = fitness
    population.sort(key=lambda x: x["fitness"], reverse=True)

def main():
    random.seed()

    population = [{"x1": generate_initial_x1(), "x2": generate_initial_x2(), "fitness": 0} for i in range(POPULATION_SIZE)]
    best_fitnesses = []
    average_fitnesses = []
    standard_deviations = []

    for generation in range(GENERATIONS):
        crossover(population)
        mutate(population)
        calculate_fitness(population)

        best_fitness = population[0]["fitness"]
        average_fitness = sum(individual["fitness"] for individual in population) / POPULATION_SIZE
        standard_deviation = math.sqrt(sum((individual["fitness"] - average_fitness)**2 for individual in population) / POPULATION_SIZE)

        best_fitnesses.append(best_fitness)
        average_fitnesses.append(average_fitness)
        standard_deviations.append(standard_deviation)

        print(f"Generation {generation + 1}:")
        print(f"Best fitness: {best_fitness}")
        print(f"Average fitness: {average_fitness}")
        print(f"Standard deviation: {standard_deviation}")

    return best_fitnesses, average_fitnesses, standard_deviations

if __name__ == "__main__":
    main()
