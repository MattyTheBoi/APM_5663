# Stoer-Wagner Minimum Cut Program Documentation

## Overview
This program implements the Stoer-Wagner Minimum Cut algorithm for weighted, undirected graphs. The algorithm finds a global minimum cut: a partition of the graph’s vertices into two subsets such that the sum of the edge weights crossing the partition is minimized.

**Note:** This program requires **Python 3.x** to run properly.

## Key Theoretical Insight (The Stoer-Wagner Theorem)
The Stoer-Wagner theorem states that a global minimum cut can be found by considering s-t cuts derived through a maximum adjacency search process. In other words, among all the s-t cuts identified by repeatedly merging vertices according to the maximum adjacency search, at least one is a global minimum cut. By performing these successive searches and merges, the algorithm will eventually identify the true minimum cut.

## Key Steps of the Stoer-Wagner Algorithm

1. **Phase (Maximum Adjacency Search)**:
   - Start from an arbitrary vertex.
   - Iteratively add the vertex that has the largest cumulative weight to the chosen set until all vertices are added.
   - During this process, we look for a "valid ordered pair" (as discussed in class). Conceptually, this corresponds to scanning what would be an "adjacency matrix" (or adjacency list) to determine the next vertex to add.
   - The last two vertices added define an s-t cut for that phase. According to the Stoer-Wagner theorem, one of these s-t cuts will be the global minimum cut. If this cut is smaller than any previously recorded cut, we update our best cut.

2. **Merge (Contract) Vertices**:
   - Merge the final two vertices from the phase into one "super-vertex."
   - Update all edges to reflect this merged vertex rather than two separate ones.
   - Remove self-loops and combine parallel edges, simplifying subsequent processing.

3. **Repeat**:
   - Continue the above phases until only two vertices remain, effectively leaving a single edge representing the final cut.
   - The smallest cut found during these phases is the global minimum cut.

After completion, the algorithm uses the recorded merging steps to reconstruct which original vertices form each side of the minimum cut. It then reports the minimum cut weight, the vertices on one side, and the edges that cross the cut. (While this method of tracking the partition is not the most elegant, it works.)

## Data Structures and Main Variables

- **defaultdict**:  
  The code uses Python's `collections.defaultdict` extensively to handle dictionaries with default values. This simplifies the construction and modification of the graph structure during merges and updates.

- **graph (Dict[int, List[Tuple[int,int]]])**:  
  A mapping from each vertex to a list of `(neighbor, weight)` pairs, implemented as a `defaultdict(list)` for easy edge insertion.

- **original_edges (List[Tuple[int,int,int]])**:  
  A list of all original edges, each represented as `(u, v, weight)`.

- **merged_vertices (Dict[int, Set[int]])**:  
  Tracks the merging of vertices. Keys are "super-vertices" and values are sets of the original vertices they represent.

- **best_cut_weight (int)**:  
  The smallest (best) minimum cut weight found so far. Starts at infinity and updates whenever a better cut is discovered.

- **best_partition (Set[int])**:  
  A set of super-vertices representing one side of the best minimum cut found. Later expanded into the set of original vertices.

- **cut_edges (Set[Tuple[int,int,int]])**:  
  The set of edges that cross the discovered minimum cut. Computed after identifying the minimum cut partition.

## Functions

1. **run_stoer_wagner(input_file, output_file)**  
   - Reads the graph from `input_file`.
   - Calls `compute_min_cut` to determine the min cut partition and weight.
   - Identifies the edges crossing the cut using `original_edges`.
   - Writes the results (min-cut weight, partition, and cut edges) to `output_file`.

2. **read_graph_from_file(file_path)**  
   - Reads the graph from the given file.
   - The first line contains the number of vertices.
   - Each subsequent line describes an edge: `u v weight`.
   - Returns `graph` and `original_edges`.

3. **compute_min_cut(graph)**  
   - Implements the Stoer-Wagner algorithm.
   - Repeatedly performs maximum adjacency searches to identify s-t cuts.
   - Tracks and updates the best (minimum) cut found.
   - Merges vertices after each phase until only one vertex remains.
   - Returns the best partition and the minimum cut weight.

4. **maximum_adjacency_search(g)** (sub-function within `compute_min_cut`)  
   - Performs one phase of the Stoer-Wagner algorithm.
   - Iteratively selects vertices by choosing the vertex with the largest cumulative connection weight to the chosen set.
   - Conceptually scans an "adjacency matrix" or adjacency list to find the next vertex.
   - Returns the last two added vertices (defining an s-t cut), the cut weight, and the order of added vertices.

5. **merge_vertices(g, s, t, merged_vertices)**  
   - Merges two vertices `s` and `t` in the graph `g`.
   - Updates `merged_vertices` to reflect the merge.
   - Redirects and combines edges, removing self-loops and merging parallel edges.
   - Returns the updated `graph`.

6. **write_output_file(file_path, partition, other_side, cut_edges, min_cut_weight)**  
   - Writes the computed min cut results to file:
     - The min-cut weight.
     - The vertices on one side of the cut.
     - The edges crossing the cut and their weights.

7. **process_all_files(input_dir, output_dir)**  
   - Processes all `.txt` files in `input_dir`.
   - For each file, runs `run_stoer_wagner` and writes the results to `output_dir`.

## Usage

1. Ensure you have **Python 3.x** installed.
2. Place input files in the `Inputs` directory.  
   The first line in each file should be the number of vertices, followed by lines in the format: u v weight
3. Run the program:
- It reads each input file, computes the min cut, and writes results to the `Outputs` directory.
4. The output file includes:
- The weight of the minimum edge-cut.
- The set of vertices on one side of the cut.
- The edges that cross the cut and their weights.

Adjust `input_dir` and `output_dir` in the `__main__` section as needed.

## External Reference

- [Thomas Jungblut's Blog on Minimum Cut](https://blog.thomasjungblut.com/graph/mincut/mincut/)

For additional questions, contact: [mhorvath@oakland.edu](mailto:mhorvath@oakland.edu)
