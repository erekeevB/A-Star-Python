import matplotlib.pyplot as plt
from search import *

barrier = []
barrier.append([(2,5),(3,5),(3,6),(3,7),(4,7),(5,7),(6,7),(6,6),(6,5),(6,4),(6,3),(5,3),(4,3)])

grid_border = []
grid_border.append([(1,1),(1,8),(8,8),(8,1),(1,1)])

optimalPath, expandedNodes, cost = aStarSearch((1,1), (8,8), barrier)

print ("number of expanded nodes with A* search is:", len(expandedNodes))
print ("route returned by A* search :", optimalPath)
print ("cost of A* search is", cost)

plt.title('A* search')
for bpt in grid_border:
    plt.plot([v[0] for v in bpt], [v[1] for v in bpt],'g--')

for bar_pt in barrier:
    plt.plot([v[0] for v in bar_pt], [v[1] for v in bar_pt],'r*-')

plt.plot([u[0] for u in optimalPath], [u[1] for u in optimalPath],'bo-')
    
plt.xlim(0,9)
plt.ylim(0,9)
plt.grid()
plt.show()

optimalPath2, expandedNodes2, cost2 = UCSearch((1,1), (8,8), barrier)

print ("number of expanded nodes with UCS is:", len(expandedNodes2))
print ("route returned by UCS :", optimalPath2)
print ("cost of UCS is", cost2)

plt.title('UCS search')
for bpt in grid_border:
    plt.plot([v[0] for v in bpt], [v[1] for v in bpt],'g--')

for bar_pt in barrier:
    plt.plot([v[0] for v in bar_pt], [v[1] for v in bar_pt],'r*-')

plt.plot([u[0] for u in optimalPath2], [u[1] for u in optimalPath2],'bo-')
    
plt.xlim(0,9)
plt.ylim(0,9)
plt.grid()
plt.show()
plt.title('UCS search')