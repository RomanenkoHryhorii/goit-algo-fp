import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, val, color="skyblue"):
        self.val = val
        self.left = None
        self.right = None
        self.id = str(uuid.uuid4())
        self.color = color

def create_sample_tree():
    """Створення прикладного бінарного дерева"""
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

def generate_color_gradient(num_steps):
    """
    Генерує градієнт кольорів від темного до світлого.
    
    :param num_steps: кількість унікальних кольорів
    :return: список кольорів у форматі RGB
    """
    colors = []
    for i in range(num_steps):
        # Інтенсивність від 20 до 255
        intensity = 20 + int((i / (num_steps - 1)) * 235)
        color = f'#{intensity:02x}{intensity:02x}FF'
        colors.append(color)
    return colors

def depth_first_search(root):
    """
    Обхід дерева в глибину з використанням стеку
    
    :param root: корінь дерева
    :return: список вузлів у порядку обходу
    """
    if not root:
        return []
    
    stack = [(root, False)]
    result = []
    
    while stack:
        node, visited = stack.pop()
        
        if visited:
            continue
        
        result.append(node)
        
        # Додаємо праву гілку першою, щоб зберегти порядок обходу
        if node.right:
            stack.append((node.right, False))
        if node.left:
            stack.append((node.left, False))
        
        stack.append((node, True))
    
    return result

def breadth_first_search(root):
    """
    Обхід дерева в ширину з використанням черги
    
    :param root: корінь дерева
    :return: список вузлів у порядку обходу
    """
    if not root:
        return []
    
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()
        result.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    """Додавання ребер до графу"""
    if node is not None:
        graph.add_node(node.id, color=node.color, label=str(node.val))
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree_traversal(traversed_nodes, title):
    """
    Малювання дерева з позначенням послідовності обходу
    
    :param traversed_nodes: список вузлів у порядку обходу
    :param title: заголовок графіку
    """
    tree_root = traversed_nodes[0]
    
    # Встановлення кольорів для вузлів
    color_gradient = generate_color_gradient(len(traversed_nodes))
    for node, color in zip(traversed_nodes, color_gradient):
        node.color = color
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, 
            node_size=2500, node_color=colors, with_labels=True)
    plt.title(title)
    plt.show()

# Головна функція для демонстрації
def main():
    # Створення дерева
    tree_root = create_sample_tree()
    
    # Обхід у глибину
    dfs_nodes = depth_first_search(tree_root)
    print("Обхід у глибину (DFS):")
    for node in dfs_nodes:
        print(node.val, end=" ")
    print("\n")
    draw_tree_traversal(dfs_nodes, "Обхід у глибину (DFS)")
    
    # Оновлення дерева для обходу в ширину
    tree_root = create_sample_tree()
    
    # Обхід у ширину
    bfs_nodes = breadth_first_search(tree_root)
    print("Обхід у ширину (BFS):")
    for node in bfs_nodes:
        print(node.val, end=" ")
    print("\n")
    draw_tree_traversal(bfs_nodes, "Обхід у ширину (BFS)")

# Виконання основної функції
if __name__ == "__main__":
    main()