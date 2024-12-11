items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350},
}

def greedy_algorithm(items, budget):
    """
    Реалізація жадібного алгоритму для максимізації калорійності в межах бюджету.

    Аргументи:
        items (dict): Словник з продуктами, їхньою вартістю та калорійністю.
        budget (int): Максимальний доступний бюджет.

    Повертає:
        list: Обрані продукти для максимальної калорійності.
        int: Загальна калорійність обраних продуктів.
    """
    # Розрахунок співвідношення калорій до вартості та сортування продуктів за цим співвідношенням у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    
    selected_items = []
    total_calories = 0
    remaining_budget = budget

    for item, details in sorted_items:
        if details['cost'] <= remaining_budget:
            selected_items.append(item)
            total_calories += details['calories']
            remaining_budget -= details['cost']

    return selected_items, total_calories

def dynamic_programming(items, budget):
    """
    Реалізація алгоритму динамічного програмування для максимізації калорійності в межах бюджету.

    Аргументи:
        items (dict): Словник з продуктами, їхньою вартістю та калорійністю.
        budget (int): Максимальний доступний бюджет.

    Повертає:
        list: Обрані продукти для максимальної калорійності.
        int: Загальна калорійність обраних продуктів.
    """
    # Отримання назв продуктів, їхньої вартості та калорійності
    item_names = list(items.keys())
    costs = [items[name]['cost'] for name in item_names]
    calories = [items[name]['calories'] for name in item_names]
    
    # Ініціалізація таблиці динамічного програмування
    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    # Заповнення таблиці DP
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if costs[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлення обраних продуктів
    selected_items = []
    total_calories = dp[n][budget]
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_names[i - 1])
            w -= costs[i - 1]

    return selected_items[::-1], total_calories

# Приклад використання
budget = 100
selected_greedy, calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:", selected_greedy, "Калорії:", calories_greedy)

selected_dp, calories_dp = dynamic_programming(items, budget)
print("Динамічне програмування:", selected_dp, "Калорії:", calories_dp)
