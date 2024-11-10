# Ford-Fulkerson Algorithm Solver

## Overview

This program reads a graph from a given text file, represented by its edges and capacities, and finds the maximum flow between two specified vertices using the Ford-Fulkerson algorithm. The program also computes the minimum cut of the graph and outputs the flow values on all edges, as well as the vertices on the left side of the minimum cut. This was done as part of a Midterm for Oakland University, APM 5663 in Fall, 2024.

## Files

- `ford_fulkerson_solver.py`: The main script that implements the Ford-Fulkerson algorithm to find the maximum flow and minimum cut in a flow network.
- `Inputs/`: Directory containing input files with graph data.
- `Outputs/`: Directory where the output files with results will be saved.

## How to Run

1. Ensure you have Python installed on your system.
2. Place your input files in the `Inputs` directory.
3. Run the script using `python ford_fulkerson_solver.py`.
4. The results will be saved in the `Outputs` directory with filenames corresponding to the input files, appended with `_output`.

## Program Documentation

### 1. Overview

The program reads a graph from an input file, finds the maximum flow between a source and a sink vertex using the Ford-Fulkerson algorithm, and computes the minimum cut. The results are written to an output file, including the maximum flow, the flow on each edge, and the minimum cut edges.

### 2. Key Concepts

- **Maximum Flow**: The total amount of flow that can be sent from the source to the sink through the network of edges, subject to the capacity constraints of each edge.
- **Minimum Cut**: A set of edges whose removal minimizes the flow from the source to the sink. The minimum cut is closely related to the maximum flow due to the Max-Flow Min-Cut Theorem.
- **Flow Values**: The amount of flow sent along each edge from the source to the sink.

### 3. File Format

The input file contains the following information:
1. The number of vertices on the first line.
2. The source and sink vertices on the second line.
3. The edges of the graph on the subsequent lines, where each edge is represented by a tuple of two vertices and a weight (capacity).

### 4. Functions in the Program

- **`read_graph(filename)`**: Reads the input file and constructs the graph.
  - **Input**: Filename of the input file.
  - **Output**: Number of vertices, source vertex, sink vertex, and a list of edges with capacities.
  - **Data Structure**: A list of edges where each edge is a tuple of two integers representing the vertices and an integer representing the capacity.

- **`bfs(capacity, source, sink, parent)`**: Implements the breadth-first search (BFS) to find an augmenting path in the residual graph.
  - **Input**: The capacity matrix, source vertex, sink vertex, and a parent dictionary for reconstructing the path.
  - **Output**: Returns `True` if an augmenting path is found, `False` otherwise.

- **`ford_fulkerson(num_vertices, source, sink, edges)`**: Implements the Ford-Fulkerson algorithm to find the maximum flow and minimum cut.
  - **Input**: Number of vertices, source vertex, sink vertex, and a list of edges.
  - **Output**: Maximum flow value, flow values on all edges, the minimum cut, and the set of visited vertices.
  - **Data Structure**:
    - `capacity`: A dictionary representing the residual capacities of the edges.
    - `flow`: A dictionary storing the flow values along each edge.
    - `original_capacity`: A dictionary storing the original capacities of the edges for computing the minimum cut.

- **`write_output(output_filename, max_flow, flow, min_cut, visited, source)`**: Writes the output to a file.
  - **Input**: Output filename, maximum flow value, flow values, minimum cut edges, visited vertices, and the source vertex.
  - **Output**: Writes the maximum flow, flow on edges, vertices on the left side of the minimum cut, and the edges in the minimum cut.

- **`process_file(input_filepath, output_filepath)`**: Processes a single input file.
  - **Input**: Input file path and output file path.
  - **Output**: Calls `ford_fulkerson` and `write_output` with the appropriate arguments.

- **`process_all_files(input_dir, output_dir)`**: Processes all files in the input directory.
  - **Input**: Input directory and output directory.
  - **Output**: Processes each input file and writes the results to the output directory.

### 5. Data Structures (General)

- **Graph Representation**: The graph is stored as a residual capacity matrix using a default dictionary, where the keys are vertices and the values are dictionaries representing the adjacent vertices and the capacities of the edges.
- **Flow Dictionary**: The flow along each edge is stored in a dictionary.
- **Parent Dictionary**: This dictionary is used to store the parent of each vertex along the augmenting path.
- **Visited Set**: A set to track the vertices reachable from the source during the BFS and to help identify the minimum cut.

### 6. Main Variables

- `capacity`: The residual capacity matrix representing the network.
- `flow`: The flow matrix storing the flow along each edge.
- `original_capacity`: The original capacity matrix used to compute the minimum cut.
- `parent`: A dictionary storing the parent of each vertex in the augmenting path.
- `max_flow`: The total maximum flow value from the source to the sink.
- `min_cut`: A list of edges that form the minimum cut of the graph.
- `visited`: A set of vertices that are reachable from the source after the Ford-Fulkerson algorithm completes.

## Contact

For any questions, feel free to email mhorvath@oakland.edu.

