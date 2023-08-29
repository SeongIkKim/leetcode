from collections import defaultdict

class Solution:
    count = 0

    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        """
        모든 city를 node 0로 이어야하기때문에,
        node 0를 root로 뻗어나가는 tree를 역전시킨 형태로 생각할 수 있음.
        dfs하면서 root를 향하지 않는 edge가 있다면(parent를 향하지 않는 child가 있다면) 방향 변경
        """
        adj = defaultdict(set)
        for frm, to in connections:
            # out = 1, come = 0, root부터 child로 탐색하는데 root를 향하도록 만들어야하므로 out인 것들은 되돌려야할 간선
            adj[frm].add((to, 1))
            adj[to].add((frm, 0))
        
        def dfs(node, parent):
            if node not in adj: # 최초의 root parent(-1)을 위해 만들어둔 예외처리
                return
            for neighbor, reverse in adj[node]: 
                if (neighbor != parent):
                    child = neighbor # undirected tree에서 인접한 노드는 parent를 제외하고는 모두 child라고 생각하자
                    self.count += reverse
                    dfs(child, node)
        
        dfs(0, -1);
        return self.count


        


        