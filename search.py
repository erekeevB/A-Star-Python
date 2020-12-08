def heuristic(pos, goal):
    return max(abs(pos[0] - goal[0]),abs(pos[1] - goal[1]))

def get_neighbors(pos):
    neighbors = []
    for ix, iy in [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]:
        nx = pos[0] + ix
        ny = pos[1] + iy
        if nx < 1 or nx > 8 or ny < 1 or ny > 8:
            continue
        neighbors.append((nx,ny))
    return neighbors

def move_cost(next_node, barrier):
    for bar_pos in barrier:
        if next_node in bar_pos:
            return 200
    return 1 



def UCSearch(start, goal, barrier):
    G = {} 
    
    G[start] = 0
    
    expandedNodes = set() 
    fringe = set([start]) 
    parent = {} 
    
    while len(fringe) > 0:
        curNode = None
        curGscore = None
        
        for pos in fringe:
            if curNode is None or G[pos] < curGscore:
                curGscore = G[pos]
                curNode = pos
        fringe.remove(curNode)
        
        if curNode == goal:
            path = [curNode]
            while curNode in parent:
                curNode = parent[curNode]
                path.append(curNode)
            path.reverse()
            return path, expandedNodes, G[goal]
              
        if curNode != goal:

        	expandedNodes.add(curNode)

        	neighbor = get_neighbors(curNode)

        	for nodes in neighbor:
        		if nodes not in expandedNodes:
	        		if nodes in fringe:
	        			temp = G[curNode] + move_cost(nodes, barrier)
	        			if temp < G[nodes]:
	        				G[nodes] = temp
	        				parent[nodes] = curNode
	        		else:
	        			G[nodes] = G[curNode] + move_cost(nodes, barrier)
	        			parent[nodes] = curNode
	        			fringe.add(nodes)
            
    raise RuntimeError("UCS failed to find a solution")
    


def aStarSearch(start, goal, barrier):
    
    G = {} 
    F = {} 
    
    G[start] = 0
    F[start] = heuristic(start, goal)
    
    expandedNodes = set() 
    fringe = set([start]) 
    
    parent = {} 
    
    while len(fringe) > 0:
        curNode = None
        curFscore = None
        
        for pos in fringe:
            if curNode is None or F[pos] < curFscore:
                curFscore = F[pos]
                curNode = pos
        fringe.remove(curNode)
        
        if curNode == goal:
            path = [curNode]
            while curNode in parent:
                curNode = parent[curNode]
                path.append(curNode)
            path.reverse()
            return path, expandedNodes, F[goal]
        
        if curNode != goal:

        	expandedNodes.add(curNode)

        	neighbor = get_neighbors(curNode)

        	for nodes in neighbor:
        		if nodes not in expandedNodes:
	        		if nodes in fringe:
	        			temp = G[curNode] + move_cost(nodes, barrier) + heuristic(nodes, goal)
	        			if temp < F[nodes]:
	        				G[nodes] = G[curNode] + move_cost(nodes, barrier)
	        				F[nodes] = temp
	        				parent[nodes] = curNode
	        		else:
	        			G[nodes] = G[curNode] + move_cost(nodes, barrier)
	        			F[nodes] = G[nodes] + heuristic(nodes, goal)
	        			parent[nodes] = curNode
	        			fringe.add(nodes)
    raise RuntimeError("A* failed to find a solution")