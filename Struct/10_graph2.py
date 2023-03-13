"""
图 邻接矩阵
"""
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, i, j, weight=1):
        self.adj_matrix[i][j] = weight
        self.adj_matrix[j][i] = weight

    def remove_edge(self, i, j):
        self.adj_matrix[i][j] = 0
        self.adj_matrix[j][i] = 0

    def get_edge(self, i, j):
        return self.adj_matrix[i][j]

    def get_neighbors(self, vertex):
        neighbors = []
        for j in range(self.num_vertices):
            if self.adj_matrix[vertex][j]:
                neighbors.append(j)
        return neighbors

    def dfs(self, start):
        visited = [False] * self.num_vertices
        self._dfs(start, visited)

    def _dfs(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")
        for neighbor in self.get_neighbors(vertex):
            if not visited[neighbor]:
                self._dfs(neighbor, visited)

    def bfs(self, start):
        visited = [False] * self.num_vertices
        queue = []
        queue.append(start)
        visited[start] = True

        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            for neighbor in self.get_neighbors(vertex):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


if __name__ == '__main__':
    g = Graph(4)

    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 0)

    print("Edges:")
    for i in range(4):
        for j in range(i + 1, 4):
            if g.get_edge(i, j):
                print(f"{i}-{j}: {g.get_edge(i, j)}")

    print("Neighbors:")
    for i in range(4):
        print(f"{i}: {g.get_neighbors(i)}")

    print("DFS traversal:")
    g.dfs(0)

    print("\nBFS traversal:")
    g.bfs(0)