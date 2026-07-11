class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize DSU where each node is its own parent
        # For both of par and rank lists, we need n+1 items to skip 0
        n = len(edges)
        par = [i for i in range(n+1)] # ith node -> parent (1 - n)
        # Also maintain the size or rank of each connected component
        # This is so that we can merge the smaller component to the larger component
        rank = [1] * (n+1) 

        # Define find function to find the parent of a node n
        def find(n):
            # Recursive implementation of path compression
            # Compress height of tree so every node in component points to same root parent
            # Without path compression, a DSU tree can become a long, lopsided chain (essentially a linked list)
            # Finding the root parent of a node will take O(n), which is inefficient
            # The tree will keep reshaping itself so all nodes will have same parent
            # especially since it might not be the case when two components are initially merged
            if n != par[n]:
                par[n] = find(par[n]) # find the root parent and set parent of current node to that
            return par[n]

        # Define union function to merge two nodes/components
        def union(n1, n2):
            # Return true if n1 and n2 were not already connected
            p1, p2 = find(n1), find(n2) # find their parents first
            if p1 == p2:
                return False
                # if have same parent, they are already connected
            
            # Want to perform union by rank
            if rank[p1] >= rank[p2]: 
                # if p1 is in a larger component, then we want p2 to be the child
                par[p2] = p1
                rank[p1] += rank[p2] # update the rank of p1 by adding to it rank of p2
            else:
                # vice versa
                par[p1] = p2
                rank[p2] += rank[p2]
            return True

        for n1, n2 in edges:
            if not union(n1, n2): # if you can't union, then they're already connected
                return [n1, n2]

