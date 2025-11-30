# импорт библиотек
import math

# хэш таблица путей
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['end'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5
graph['end'] = {}

# хэш таблица весов
inf = math.inf
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['end'] = inf

# хэш таблица родителей
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None

# множество обработанных элементов
processed = set()

# функция для поиска наименьшего веса
def find_lowest_cost_node(costs):
    lowest_cost = inf
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost< lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    print(lowest_cost_node)
    return lowest_cost_node

# алгоритм Дейкстры
node = find_lowest_cost_node(costs)
while node is not None:
    print(costs, parents)
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs)
