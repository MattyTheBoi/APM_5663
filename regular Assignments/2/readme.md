# Huffman Coding Program

## Overview

This program implements Huffman coding, a compression algorithm used to reduce the size of data. The program reads input files containing symbols and their frequencies, builds a Huffman tree, generates Huffman codes for each symbol, and writes the results to output files.

## Data Structures and Main Variables

1. **Node Class**:
   - **Attributes**:
     - `symbol`: The symbol represented by this node.
     - `freq`: The frequency of the symbol.
     - `left`: Left child of the node.
     - `right`: Right child of the node.
   - **Methods**:
     - `__init__(self, symbol, freq)`: Initializes the node with a symbol and its frequency.
     - `__lt__(self, other)`: Comparison method for the priority queue (min-heap), compares nodes based on their frequency.

2. **Functions**:
   - `read_input_file(file_path)`: Reads the input file and returns a list of tuples containing symbols and their frequencies.
     - **Variables**:
       - `file_path`: Path to the input file.
       - `num_symbols`: Number of symbols in the input file.
       - `symbols_freq`: List of tuples containing symbols and their frequencies.
   - `build_huffman_tree(symbols_freq)`: Builds the Huffman tree from the list of symbols and frequencies.
     - **Data Structures**:
       - `heap`: A priority queue (min-heap) used to build the Huffman tree.
     - **Variables**:
       - `symbols_freq`: List of tuples containing symbols and their frequencies.
       - `left`: Node with the smallest frequency.
       - `right`: Node with the second smallest frequency.
       - `merged`: New node created by merging `left` and `right`.
   - `generate_huffman_codes(root)`: Generates Huffman codes for each symbol by traversing the Huffman tree.
     - **Variables**:
       - `root`: Root node of the Huffman tree.
       - `codes`: Dictionary to hold the symbol and its corresponding code.
       - `current_code`: Current binary code being generated.
   - `write_output_file(file_path, codes, symbols_freq)`: Writes the Huffman codes and average number of bits per symbol to the output file.
     - **Variables**:
       - `file_path`: Path to the output file.
       - `codes`: Dictionary containing the Huffman codes for each symbol.
       - `symbols_freq`: List of tuples containing symbols and their frequencies.
       - `total_bits`: Total number of bits used to encode the symbols.
       - `total_freq`: Total frequency of all symbols.
       - `avg_bits_per_symbol`: Average number of bits used per symbol.
   - `huffman_algo(input_file, output_file)`: Main function that orchestrates reading the input file, building the Huffman tree, generating codes, and writing the output file.
     - **Variables**:
       - `input_file`: Path to the input file.
       - `output_file`: Path to the output file.
       - `symbols_freq`: List of tuples containing symbols and their frequencies.
       - `huffman_tree_root`: Root node of the Huffman tree.
       - `huffman_codes`: Dictionary containing the Huffman codes for each symbol.
   - `process_all_files(input_dir, output_dir)`: Processes all files in the input directory with allowed extensions and writes the results to the output directory.
     - **Variables**:
       - `input_dir`: Directory containing the input files.
       - `output_dir`: Directory to write the output files.
       - `allowed_extensions`: List of allowed file extensions.
       - `file_name`: Name of the current file being processed.
       - `input_file`: Path to the current input file.
       - `output_file`: Path to the current output file.