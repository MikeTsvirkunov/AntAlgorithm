import networkx as nx
import networkx as nx
import json
# Создаем новый граф
G = nx.Graph()

# Добавляем узел node1
G.add_node('node1')

# Добавляем узел node2 и ребро между node1 и node2
G.add_edge('node1', 'node2')

# Добавляем еще один узел node3 и ребро между node2 и node3
G.add_edge('node2', 'node3')


# Конвертируем граф в словарь Python
d = {"nodes": [{"id": n} for n in G.nodes()],
     "edges": [{"id": f"{i}_{j}", "source": i, "target": j} for i, j in G.edges()]}

# Конвертируем словарь Python в JSON-строку
s = json.dumps(d)

# Выводим JSON-строку на экран (для демонстрации)
print(s)