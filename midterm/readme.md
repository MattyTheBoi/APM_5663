# Dijkstra's Algorithm Solver

## Overview

This program reads a graph from a given text file, represented via its edges, and finds the minimum weight path between two specified vertices using Dijkstra's algorithm. The program outputs the vertices in the order they are explored and the minimum weight path found between the two vertices, or states that there is no such path if the vertices lie in different components. This was done as part of a Midterm for Oakland University, APM 5663 in Fall, 2024.

## Files

- `dijkstra_solver.py`: The main script that contains the implementation of Dijkstra's algorithm.
- `Inputs/`: Directory containing input files with graph data.
- `Outputs/`: Directory where the output files with results will be saved.

## How to Run

1. Ensure you have Python installed on your system.
2. Place your input files in the `Inputs` directory.
3. Run the script using `python dijkstra_solver.py`.
4. The results will be saved in the `Outputs` directory with filenames corresponding to the input files, appended with `_output`.

## Program Documentation

### 1. Overview

The program reads a graph from an input file, finds the minimum weight path between two specified vertices using Dijkstra's algorithm, and then outputs the result to another file. The output includes the vertices in the order they are explored and the minimum weight path found, or a message stating that there is no path if the vertices lie in different components.

### 2. Key Concepts

- **Explored Vertices**: The vertices that are visited during the execution of Dijkstra's algorithm.
- **Minimum Weight Path**: The path between two vertices in a graph such that the sum of the weights of the edges in the path is minimized.

### 3. File Format

The input file contains the number of vertices on the first line, followed by the start and end vertices on the second line, and then the edges listed on each subsequent line. Each edge is described by two vertices and a weight.

### 4. Functions in the Program

- **`read_graph(filename)`**: Reads the input file and constructs the graph.
  - **Input**: Filename of the input file.
  - **Output**: Number of vertices, start vertex, end vertex, and a list of edges.
  - **Data Structure**: A list of edges where each edge is a tuple of two integers representing vertices and an integer representing the weight.

- **`dijkstra(num_vertices, start_vertex, end_vertex, edges)`**: Implements Dijkstra's algorithm to find the minimum weight path.
  - **Input**: Number of vertices, start vertex, end vertex, and a list of edges.
  - **Output**: Explored vertices, minimum weight path, and total weight of the path.
  - **Data Structure**:
    - `graph`: An adjacency list representation of the graph.
    - `min_heap`: A priority queue to efficiently get the vertex with the smallest distance.
    - `distances`: A dictionary to store the minimum distance from the start vertex to each vertex.
    - `previous`: A dictionary to store the previous vertex in the path for each vertex.
    - `explored`: A list to store the order of explored vertices.
    - `path`: A list to store the minimum weight path.

- **`write_output(output_filename, explored, path, total_weight)`**: Writes the output to a file.
  - **Input**: Output filename, explored vertices, minimum weight path, and total weight of the path.
  - **Output**: Writes the explored vertices, minimum weight path, and total weight to the output file.

- **`process_file(input_filepath, output_filepath)`**: Processes a single input file.
  - **Input**: Input file path and output file path.
  - **Output**: Calls `dijkstra` and `write_output` with the appropriate arguments.

- **`process_all_files(input_dir, output_dir)`**: Processes all files in the input directory.
  - **Input**: Input directory and output directory.
  - **Output**: Processes each input file and writes the results to the output directory.

### 5. Data Structures (General)

- **Graph Representation**: The graph is stored as an adjacency list using a default dictionary where the keys are vertices and the values are lists of tuples representing neighboring vertices and the weights of the edges.
- **Distances Dictionary**: The minimum distance from the start vertex to each vertex is stored in a dictionary.
- **Previous Dictionary**: The previous vertex in the path for each vertex is stored in a dictionary.
- **Explored List**: A list to store the order of explored vertices.
- **Path List**: A list to store the minimum weight path.

### 6. Main Variables

- `graph`: The adjacency list representing the graph.
- `distances`: A dictionary storing the minimum distances from the start vertex to each vertex.
- `previous`: A dictionary storing the previous vertex in the path for each vertex.
- `explored`: A list storing the order of explored vertices.
- `path`: The final minimum weight path (list of vertices in the order they are visited).
- `min_heap`: A priority queue used to efficiently get the vertex with the smallest distance.

## Contact

For any questions, feel free to email mhorvath@oakland.edu