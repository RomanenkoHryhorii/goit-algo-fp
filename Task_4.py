import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_heap_tree(heap):
    """
    Перетворює масив купи у бінарне дерево.
    
    :param heap: list, масив купи
    :return: корінь бінарного дерева
    """
    if not heap:
        return None
    
    nodes = [Node(val) for val in heap]
    
    # Зв'язування вузлів батько-діти
    for i in range(len(nodes)):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        
        if left_idx < len(nodes):
            nodes[i].left = nodes[left_idx]
        
        if right_idx < len(nodes):
            nodes[i].right = nodes[right_idx]
    
    return nodes[0]

def add_edges(graph, node, pos, x=0, y=0, layer=1):
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

def draw_heap(heap, is_max_heap=True):
    """
    Візуалізує бінарну купу.
    
    :param heap: list, масив купи
    :param is_max_heap: bool, чи це купа максимумів (за замовчуванням True)
    """
    if not heap:
        print("Купа порожня")
        return
    
    # Встановлення кольорів для купи
    tree_root = build_heap_tree(heap)
    
    # Зафарбовування вузлів залежно від типу купи
    def color_nodes(node):
        if node is None:
            return
        
        if is_max_heap:
            # Для купи максимумів: більш насичений колір для більших значень
            color_intensity = min(255, int(node.val * 2))
            node.color = f'#{color_intensity:02x}8CFF'  # Відтінки блакитного
        else:
            # Для купи мінімумів: більш насичений колір для менших значень
            color_intensity = min(255, int((max(heap) - node.val) * 2))
            node.color = f'#{color_intensity:02x}8CFF'  # Відтінки блакитного
        
        color_nodes(node.left)
        color_nodes(node.right)
    
    color_nodes(tree_root)
    
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}
    
    plt.figure(figsize=(10, 6))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.title(f"{'Купа максимумів' if is_max_heap else 'Купа мінімумів'}")
    plt.show()

# Приклади використання
max_heap = [100, 70, 50, 40, 30, 20, 15]
min_heap = [10, 20, 15, 30, 40, 50, 70]

print("Купа максимумів:")
draw_heap(max_heap)

print("\nКупа мінімумів:")
draw_heap(min_heap, is_max_heap=False)