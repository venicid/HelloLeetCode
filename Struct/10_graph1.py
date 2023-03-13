"""
图 邻接表

"""

class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_list = [[] for _ in range(num_vertices)]

    def add_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def remove_edge(self, src, dest):
        self.adj_list[src].remove(dest)
        self.adj_list[dest].remove(src)

    def get_adj_list(self, vertex):
        return self.adj_list[vertex]

    def dfs(self, start):
        visited = [False] * self.num_vertices
        self._dfs(start, visited)

    def _dfs(self, vertex, visited):
        visited[vertex] = True
        print(vertex, end=" ")
        for neighbor in self.adj_list[vertex]:
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
            for neighbor in self.adj_list[vertex]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True


if __name__ == '__main__':
    """
    0 -> 1 ->   2 
    ^           |
    |           v
     5 <- 4  <- 3

    """
    # 创建一个有 6 个顶点的图对象
    graph = Graph(6)

    # 添加边
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 0)

    # 获取邻接表
    print(graph.get_adj_list(0))  # [5]
    print(graph.get_adj_list(1))  # [2]
    print(graph.get_adj_list(2))  # [1, 3]

    # 移除边
    graph.remove_edge(0, 1)

    # 深度优先搜索
    graph.dfs(0)  # 0 5 4 3 2 1
    print()

    # 广度优先搜索
    graph.bfs(0)  # 0 5 1 4 2 3
    print()
