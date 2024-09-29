# Eulerian Tour/Trail Finder

## Overview

This program reads from a given graph, represented via its edges from a text file, and will process it and look if a Eulerian Tour/Trail exists. It's based on the Hierholzer Algorithm (for undirected graphs) to find it. This was done as an assignment for Oakland University, APM 5663 in Fall, 2024.

## Files

- `ass_1_EularianChecker.py`: The main script that contains the implementation of the algorithm.
- `Inputs/`: Directory containing input files with graph data.
- `Outputs/`: Directory where the output files with results will be saved.

## How to Run

1. Ensure you have Python installed on your system.
2. Place your input files in the `input` directory.
3. Run `pip install -r requirements.txt`
4. Now you can run the python script
5. The results will be saved in the `output` directory with filenames corresponding to the input files, appended with `_output`.

## Program Documentation

### 1. Overview

The program reads a graph from an input file, checks if it has an Eulerian trail or tour, and then outputs the result to another file. If an Eulerian trail or tour exists, the program prints the sequence of vertices representing the trail or tour, along with whether it is "open" (trail) or "closed" (tour).

The program makes use of Hierholzer's algorithm (Using undirected version) ([Medium Article](https://medium.com/@yusufaksoyeng/finding-the-eulerian-cycle-with-hierholzers-algorithm-f60bb773db3c#:~:text=In%201873,%20Hierholzer%20proposed%20an%20algorithm%20to%20find%20the%20Eulerian)) to find the Eulerian path or tour. It also checks the necessary conditions for the existence of such paths or tours.

### 2. Key Concepts

- **Eulerian Tour (Closed)**: A tour that starts and endbs at the same vertex, visiting every edge exactly once. All vertices with edges must have an even degree.
- **Eulerian Trail (Open)**: A path that starts at one vertex and ends at a different vertex, visiting every edge exactly once. Exactly two vertices have an odd degree, and the others have an even degree.

### 3. File Format

The input file contains the number of vertices on the first line, followed by edges listed on each subsequent line. Each edge is described by two vertices, representing a connection between them.

### 4. Functions in the Program

- **`read_graph(filename)`**: Reads the input file and constructs the graph.
  - **Input**: Filename of the input file.
  - **Output**: Number of vertices and a list of edges.
  - **Data Structure**: A list of edges where each edge is a tuple of two integers representing vertices.

- **`is_connected(graph, num_vertices)`**: Checks if the graph is connected by performing a depth-first search (DFS) to ensure all vertices with edges can be reached from one another.
  - **Input**: Adjacency list representation of the graph and the number of vertices.
  - **Output**: True if the graph is connected, False otherwise.
  - **Data Structure**: Uses an adjacency list (graph) to store vertices and their connections, and a set (visited) to keep track of visited vertices.

- **`get_degrees(graph)`**: Calculates the degree (number of edges) for each vertex.
  - **Input**: Adjacency list representation of the graph.
  - **Output**: A dictionary of vertex degrees.
  - **Data Structure**: A dictionary (degrees) where the key is the vertex, and the value is its degree (an integer).

- **`find_eulerian_path_or_tour(graph, num_vertices)`**: Uses Hierholzer's algorithm to find the Eulerian trail or tour.
  - **Input**: Adjacency list representation of the graph and the number of vertices.
  - **Output**: A tuple containing the Eulerian path or tour (list of vertices), a string specifying whether it's "open" (trail) or "closed" (tour), and an error message if no Eulerian trail/tour exists.
  - **Data Structure**:
    - `local_graph`: A temporary copy of the adjacency list to modify during the traversal.
    - `stack`: A stack used to keep track of vertices during traversal.
    - `path`: A list that stores the final Eulerian trail or tour.

- **`eulerian_trail(filename, output_filename)`**: The main function that coordinates reading the graph, checking for connectivity, finding the Eulerian trail or tour, and writing the result to the output file.
  - **Input**: Input file and output file names.
  - **Output**: Writes whether an Eulerian trail or tour exists, and if so, prints the path/tour to the output file.
  - **Data Structure**: Uses all the helper functions and writes results to the file using formatted strings.

### 5. Data Structures

- **Graph Representation**: The graph is stored as an adjacency list using a dictionary where the keys are vertices and the values are lists of neighboring vertices (i.e., those connected by an edge). This allows efficient traversal and modification of the graph during the Eulerian path/tour search.

- **Degrees Dictionary**: The degree of each vertex (number of edges connected to it) is stored in a dictionary. This is crucial for determining whether the graph can have an Eulerian trail or tour.

- **Stack and Path (for Hierholzer's Algorithm)**: A stack is used to keep track of vertices during the Eulerian trail/tour construction, and a list stores the final path.

### 6. Main Variables

- `graph`: The adjacency list representing the graph.
- `degrees`: A dictionary storing the degrees of vertices.
- `path`: The final Eulerian trail or tour (list of vertices in the order they are visited).
- `stack`: A stack used in Hierholzer's algorithm to backtrack through the graph while constructing the Eulerian path or tour.
- `odd_vertices`: A list of vertices with odd degrees, used to determine if the graph has an Eulerian trail or tour.
- `start_vertex`: The vertex where the traversal starts. In the case of an Eulerian tour, this can be any vertex with edges. For an Eulerian trail, it is one of the odd-degree vertices.

### 7. Algorithm Explanation: Hierholzer's Algorithm

Hierholzer’s algorithm is used to find the Eulerian trail or tour. The steps of the algorithm are as follows:

1. **Choose a Starting Vertex**:
   - If the graph has an Eulerian tour, any vertex with edges can be the starting point.
   - If the graph has an Eulerian trail, the starting vertex must be one of the two vertices with an odd degree.

2. **Traversal**:
   - A stack is used to explore the graph. Starting from the selected vertex, follow edges, adding them to the stack and removing them from the graph to prevent revisiting them.
   - Once no more edges can be followed from the current vertex, backtrack by popping the stack and adding the vertex to the final path.
   - Repeat until all edges are visited and added to the path.

3. **Output the Path**: If the traversal completes and all edges are visited, the path is printed in reverse (since it's constructed backward due to the stack).

### 8. Conditions for Eulerian Trail or Tour

- **Eulerian Tour (Closed)**:
  - All vertices have even degrees.
  - The graph is connected.

- **Eulerian Trail (Open)**:
  - Exactly two vertices have odd degrees.
  - The graph is connected.

- **No Eulerian Trail or Tour**:
  - More than two vertices have odd degrees, or the graph is disconnected.

## Contact

For any questions, feel free to email mhorvath@oakland.edu