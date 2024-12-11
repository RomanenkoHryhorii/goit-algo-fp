import random
import matplotlib.pyplot as plt

# Кількість симуляцій
num_simulations = 100000

# Ініціалізація словника для підрахунку кількості кожної суми
sums_count = {i: 0 for i in range(2, 13)}

# Симуляція кидків кубиків
for _ in range(num_simulations):
    die1 = random.randint(1, 6)  # Кидок першого кубика
    die2 = random.randint(1, 6)  # Кидок другого кубика
    total = die1 + die2          # Сума чисел на кубиках
    sums_count[total] += 1       # Збільшуємо лічильник для відповідної суми

# Обчислення ймовірностей
probabilities = {s: (count / num_simulations) * 100 for s, count in sums_count.items()}

# Виведення результатів у вигляді таблиці
print("Сума\tКількість\tІмовірність (%)")
for s in range(2, 13):
    print(f"{s}\t{sums_count[s]}\t{probabilities[s]:.2f}")

# Аналітичні ймовірності для порівняння
analytical_probabilities = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11,
    6: 13.89, 7: 16.67, 8: 13.89, 9: 11.11,
    10: 8.33, 11: 5.56, 12: 2.78
}

# Візуалізація результатів
plt.figure(figsize=(10, 6))
plt.bar(probabilities.keys(), probabilities.values(), label='Монте-Карло', color='blue', alpha=0.6)
plt.plot(analytical_probabilities.keys(), analytical_probabilities.values(),
         label='Аналітичні', color='red', marker='o')
plt.xlabel("Сума чисел на кубиках")
plt.ylabel("Імовірність (%)")
plt.title("Ймовірності сум при киданні двох кубиків")
plt.xticks(range(2, 13))
plt.legend()
plt.grid(True)
plt.show()