def dfs(src: str, dst: str, graph: dict, paths: list, path: list = None):
    path = path or [src]
    if src == dst:
        paths.append(path)
    else:
        for adjacent in graph[src]:
            if adjacent not in path:
                path.append(adjacent)
                dfs(adjacent, dst, graph, paths, path)
                path.pop()
