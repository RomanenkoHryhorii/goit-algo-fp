import heapq
from typing import Dict, List, Tuple

class Graph:
    def __init__(self):
        """Ініціалізація графа як словника суміжності."""
        self.nodes = {}
    
    def add_edge(self, start: str, end: str, weight: int):
        """Додавання зваженого ребра між вершинами."""
        if start not in self.nodes:
            self.nodes[start] = []
        if end not in self.nodes:
            self.nodes[end] = []
        
        self.nodes[start].append((end, weight))
        # Для неорієнтованого графа розкоментуйте наступний рядок:
        # self.nodes[end].append((start, weight))
    
    def dijkstra(self, start: str) -> Dict[str, int]:
        """
        Реалізація алгоритму Дейкстри з використанням бінарної купи.
        
        Args:
            start (str): Початкова вершина
        
        Returns:
            Dict[str, int]: Словник найкоротших відстаней від початкової вершини
        """
        # Ініціалізація відстаней
        distances = {node: float('inf') for node in self.nodes}
        distances[start] = 0
        
        # Купа для вибору вершини з найменшою відстанню
        pq = [(0, start)]
        
        # Словник для відстеження попередніх вершин (необов'язково)
        previous = {node: None for node in self.nodes}
        
        while pq:
            # Вибираємо вершину з найменшою поточною відстанню
            current_distance, current_node = heapq.heappop(pq)
            
            # Якщо знайдена відстань більша за раніше обчислену, пропускаємо
            if current_distance > distances[current_node]:
                continue
            
            # Перевіряємо всіх сусідів поточної вершини
            for neighbor, weight in self.nodes[current_node]:
                distance = current_distance + weight
                
                # Якщо знайдено коротший шлях
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances
    
    def reconstruct_path(self, start: str, end: str, previous: Dict[str, str]) -> List[str]:
        """
        Реконструкція найкоротшого шляху між двома вершинами.
        
        Args:
            start (str): Початкова вершина
            end (str): Кінцева вершина
            previous (Dict[str, str]): Словник попередніх вершин
        
        Returns:
            List[str]: Список вершин уздовж найкоротшого шляху
        """
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = previous.get(current)
        
        return path[::-1]  # Повертаємо шлях у правильному порядку

# Приклад використання
def main():
    # Створення графа
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 5)
    graph.add_edge('C', 'D', 8)
    graph.add_edge('C', 'E', 10)
    graph.add_edge('D', 'E', 2)
    graph.add_edge('D', 'F', 6)
    graph.add_edge('E', 'F', 3)

    # Знаходження найкоротших шляхів від вершини 'A'
    start_node = 'A'
    shortest_distances = graph.dijkstra(start_node)
    
    print(f"Найкоротші відстані від вершини {start_node}:")
    for node, distance in shortest_distances.items():
        print(f"{node}: {distance}")

if __name__ == "__main__":
    main()