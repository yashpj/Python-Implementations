"""
Understand:
Can a quest appear more than once? YES. That's multiple prerequisites

Are all the quests connected? NOT NECESSARILY.

Are there cycles? MAYBE - if there are it's a bug.

Match: TOPOSORT

Plan:
3 quests
[1, 0], [2, 1]

Maintain a queue of nodes that are ready to process
Use indegree to find a starting place - nodes with indegree 0
Process each node
    Add it to the list
    Find all neighbors - reduce their indegree by 1, process nodes that are now 0
    
When we empty the queue
    We saw all nodes
    We missed something

"""

# We need this for our queue
from collections import deque, defaultdict

def get_quest_order(num_quests, prerequisites):

    # We need to know what quests each quest helps unlock.
    # In graph terms, this is adjacency.
    adj = defaultdict(list)
    # We also need to know how many unsatisfied requirements each quest has.
    # In graph terms, this is the in degree.
    in_degree = defaultdict(int)

    for quest, prereq in prerequisites:
        # Make a link from the prereq to the quest
        adj[prereq].append(quest)
        # Increase the in degree of the quest to count the new link
        in_degree[quest] += 1

    # Start with quests that have no prerequisites
    starting_points = [i for i in range(num_quests) if in_degree[i] == 0]
    # Initialize the queue with these
    queue = deque(starting_points)

    # Set up a list to hold the order we're building
    order = []
    while queue:
        current = queue.popleft()
        order.append(current)

        # "Complete" the quest and unlock neighbors
        for neighbor in adj[current]:
            in_degree[neighbor] -= 1

            # If all prereqs are done, the quest is now available
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    # Once the queue is empty, check if all quests are included.
    if len(order) != num_quests:
        return []
    
    return order

# Test it:
tests = [
    # Input                             # Expected Output
    ((3, [[1,0], [2,1]]),               [0, 1, 2]),
    ((4, [[1,0], [2,1]]),               [0, 3, 1, 2,]),
    ((3, [[1,0], [2,1], [0,2]]),        []),
    ((4, [[0,1], [0,2], [1,3], [2,3]]), [3, 1, 2, 0])
]

# This is a little test harness for checking a list of test cases
for (input, output) in tests:
    num_quests, prerequisites = input
    description = f"quests: {num_quests} prereqs:{prerequisites} => {output}"
    result = get_quest_order(num_quests, prerequisites)
    print(description, "✅" if result == output else "❌")
    if result != output:
        print(result)


