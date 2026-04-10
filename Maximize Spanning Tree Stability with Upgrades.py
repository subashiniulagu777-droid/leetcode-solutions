class Solution(object):
    def maxStability(self, n, edges, k):
        # Separate edges for handling
        mandatory = []
        optional = []
        for u, v, s, must in edges:
            if must == 1:
                mandatory.append((u, v, s))
            else:
                optional.append((u, v, s))

        # Initial check: Mandatory edges alone must not form a cycle
        parent = list(range(n))
        def find(i, p):
            if p[i] == i: return i
            p[i] = find(p[i], p)
            return p[i]

        for u, v, s in mandatory:
            root_u, root_v = find(u, parent), find(v, parent)
            if root_u == root_v: return -1
            parent[root_u] = root_v

        def check(threshold):
            # Reset DSU for this specific threshold
            p = list(range(n))
            edges_count = 0
            
            # 1. Add all mandatory edges. They must meet the threshold.
            for u, v, s in mandatory:
                if s < threshold: return False
                root_u, root_v = find(u, p), find(v, p)
                p[root_u] = root_v
                edges_count += 1
            
            # 2. Filter optional edges that can meet the threshold
            valid_optional = []
            for u, v, s in optional:
                if s >= threshold:
                    valid_optional.append((0, u, v)) # 0 upgrades needed
                elif s * 2 >= threshold:
                    valid_optional.append((1, u, v)) # 1 upgrade needed
            
            # Prioritize 0-upgrade edges to save k budget
            valid_optional.sort()
            
            upgrades_used = 0
            for cost, u, v in valid_optional:
                if edges_count == n - 1: break
                root_u, root_v = find(u, p), find(v, p)
                if root_u != root_v:
                    if upgrades_used + cost <= k:
                        p[root_u] = root_v
                        upgrades_used += cost
                        edges_count += 1
            
            return edges_count == n - 1

        # Binary search for the maximum possible "minimum" strength
        low, high = 0, 2 * 10**5 
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
