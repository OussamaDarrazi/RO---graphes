import heapq

class Graphe:
    def __init__(self, sommets: tuple[str], matrice_adj: list[list[int]]):
        if(len(sommets) != len(matrice_adj) or any([len(sommets) != len(_) for _ in matrice_adj])):
            raise ValueError("Le nombre de sommets et les dimensions de la matrice ne sont pas compatibles")
        else:
            self.sommets = sommets
            self.matrice_adj = matrice_adj
    
    def get_successeurs(self, node: str):
        successors = {}
        if node not in self.sommets:
            print(f"le sommet {node} n'exist pas dans le graphe")
        else:
            node_index = self.sommets.index(node)
            successors = {self.sommets[i]: weight for i, weight in enumerate(self.matrice_adj[node_index]) if weight != 0}
        return successors
    
    
    def dijkstra(self, start_node: str):
        if start_node not in self.sommets:
            print(f"le sommet {start_node} n'exist pas dans le graphe")
            return
        for _ in self.matrice_adj:
            if any(i<0 for i in _):
                print(f"Le graphe contient des valeurs negatives")
                return
        distances = {node: float('inf') for node in self.sommets}
        distances[start_node] = 0

        predecessors = {node: None for node in self.sommets}
        predecessors[start_node] = start_node

        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            successors = self.get_successeurs(current_node)
            for successor, weight in successors.items():
                distance = current_distance + weight
                if distance < distances[successor]:
                    distances[successor] = distance
                    predecessors[successor] = current_node
                    heapq.heappush(priority_queue, (distance, successor))

        path = []
        predecessors_list = []
        for node in self.sommets:
            path.append(distances[node])
            predecessors_list.append(predecessors[node])

        result = {"PCC": path, "Predecesseurs": predecessors_list}
        return result

    def bellman_ford(self, start_node: str):
        if start_node not in self.sommets:
            print(f"le sommet {start_node} n'exist pas dans le graphe")
            return
        distances = {node: float('inf') for node in self.sommets}
        distances[start_node] = 0

        predecessors = {node: None for node in self.sommets}
        predecessors[start_node] = start_node

        for _ in range(len(self.sommets) - 1):
            for node in self.sommets:
                successors = self.get_successeurs(node)
                for successor, weight in successors.items():
                    distance = distances[node] + weight
                    if distance < distances[successor]:
                        distances[successor] = distance
                        predecessors[successor] = node
        for node in self.sommets:
            successors = self.get_successeurs(node)
            for successor, weight in successors.items():
                if distances[node] + weight < distances[successor]:
                    print("Le graphe contient un cycle absorbat")
                    return
        path = [distances[node] for node in self.sommets]
        predecessors_list = [predecessors[node] for node in self.sommets]

        result = {"PCC": path, "Predecesseurs": predecessors_list}
        return result

        
graphe = Graphe(("A", "B", "C", "D", "E", "F"),
                [[0, 7, 1, 0, 0, 0],
                 [0, 0, 0, 4, 0, 1],
                 [0, 5, 0, 0, 2, 7],
                 [0, 0, 0, 0, 0, 0],
                 [0, 2, 0, 5, 0, 0],
                 [0, 0, 0, 0, 3, 0]])
print(graphe.dijkstra("A"))