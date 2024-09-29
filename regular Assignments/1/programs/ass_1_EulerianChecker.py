import os
from collections import defaultdict

# Function to read the graph from a file. PRetty simple
def read_graph(filename):
    with open(filename, 'r') as f:
        num_vertices = int(f.readline().strip())
        edges = [tuple(map(int, line.split())) for line in f]
    return num_vertices, edges

# Function to check if the graph is connected (ignoring isolated vertices)
#   This function will perform a dfs, maybe another way is more efficent?
def is_connected(graph, num_vertices):
    visited = set()

    # Find a vertex with a nonzero degree to start the search 
    for v in range(1, num_vertices + 1):
        if graph[v]:
            start_vertex = v
            break
    else:
        return True  # All vertices are isolated
    
    # Perform dfs to get connectivity, ensuring is is a connected graph. If not, 
    #   then we'll return false
    stack = [start_vertex]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    stack.append(neighbor)
    
    # Check if all vertices with edges are visited
    for v in range(1, num_vertices + 1):
        if graph[v] and v not in visited:
            # Return false, so its not connected
            return False
    # Return true, so it is connected
    return True

# Function to find the degrees of vertices
def get_degrees(graph):
    degrees = defaultdict(int)
    for v in graph:
        for neighbor in graph[v]:
            degrees[v] += 1
    return degrees

# Function to find an Eulerian path or tour using Hierholzer's algorithm. Pulled from a combination of class and the internet
# https://medium.com/@yusufaksoyeng/finding-the-eulerian-cycle-with-hierholzers-algorithm-f60bb773db3c#:~:text=In%201873,%20Hierholzer%20proposed%20an%20algorithm%20to%20find%20the%20Eulerian
def find_eulerian_path_or_tour(graph, num_vertices):
    degrees = get_degrees(graph)
    odd_vertices = [v for v, degree in degrees.items() if degree % 2 == 1]

    if len(odd_vertices) == 0:
        # Eulerian tour (all vertices have even degrees)
        start_vertex = next(v for v in range(1, num_vertices + 1) if graph[v])
        path_type = "closed"
    elif len(odd_vertices) == 2:
        # Eulerian trail (exactly two vertices have odd degrees)
        start_vertex = odd_vertices[0]
        path_type = "open"
    else:
        return None, None, "The graph has more than two vertices with odd degrees."

    # Start setting up the path, stack, and local graph (Local graph being a copy of the graph)
    path = []
    stack = [start_vertex]
    local_graph = defaultdict(list)
    for v in graph:
        local_graph[v] = list(graph[v])

    # Utilize a stack to keep track of the path, and then pop off the stack to find the path
    while stack:
        # Current vertex
        v = stack[-1] 
        if local_graph[v]: # If there are still unexplored edges
            u = local_graph[v].pop() # Remove the edge from the graph
            local_graph[u].remove(v) # Remove the edge from the other vertex
            stack.append(u) # Add the other vertex to the stack
        # If there are no more edges to explore
        else: 
            path.append(stack.pop()) # Add the vertex to the path
    
    # return thhe path as well as the path type, and no error message if good. 
    return path[::-1], path_type, None

# Main function to determine Eulerian trail or tour
def eulerian_trail(filename, output_filename):
    num_vertices, edges = read_graph(filename)
    
    # Build adjacency list, this uses a defaultdict to make it easier to add edges since we don't have to check if the key exists
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    # Check if the graph is connected
    if not is_connected(graph, num_vertices):
        with open(output_filename, 'w') as f:
            f.write("The graph is not connected, it has edges that reside in more than 1 component.\n")
        return
    
    # Check for Eulerian path or tour
    path, path_type, error_message = find_eulerian_path_or_tour(graph, num_vertices)
    
    # Some basic processing here, open the file and write the output information
    with open(output_filename, 'w') as f:
        if path is None:
            f.write(f"No Eulerian trail. Reason: {error_message}\n")
        else:
            if path_type == "closed":
                f.write("The graph has an Eulerian tour (closed).\n")
            else:
                f.write("The graph has an Eulerian trail (open).\n")
            f.write("The Eulerian path or tour is: " + " -> ".join(map(str, path)) + "\n")

# Function to process all files in the input directory
def process_all_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    # Iterate over all files in the input directory, then just append "_output.txt" to the filename and set that as the output file
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):  # Assuming input files have .txt extension
            input_filepath = os.path.join(input_dir, filename)
            output_filepath = os.path.join(output_dir, filename.replace(".txt", "_output.txt"))
            eulerian_trail(input_filepath, output_filepath)

# Driver code, not much to see here
if __name__ == "__main__":
    input_dir = "Inputs"
    output_dir = "Outputs"
    process_all_files(input_dir, output_dir)