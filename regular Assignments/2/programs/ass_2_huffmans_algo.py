import heapq
import os

class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol  # The symbol represented by this node
        self.freq = freq      # The frequency of the symbol
        self.left = None      # Left child of the node
        self.right = None     # Right child of the node

    def __lt__(self, other):
        # Comparison method for the priority queue (min-heap)
        return self.freq < other.freq

def read_input_file(file_path):
    # Read input symbols and their frequencies from a file
    with open(file_path, 'r') as file:
        num_symbols = int(file.readline().strip())  # First line: number of symbols
        symbols_freq = []
        for _ in range(num_symbols):
            symbol, freq = file.readline().strip().split()  # Read symbol and frequency
            symbols_freq.append((symbol, float(freq)))  # Store as a tuple (symbol, frequency)
    return symbols_freq

def build_huffman_tree(symbols_freq):
    # Build the Huffman tree based on symbol frequencies
    heap = [Node(symbol, freq) for symbol, freq in symbols_freq]  # Create nodes for each symbol
    heapq.heapify(heap)  # Convert list to a min-heap
    
    while len(heap) > 1:
        # While there is more than one node in the heap
        left = heapq.heappop(heap)  # Get the node with the smallest frequency
        right = heapq.heappop(heap)  # Get the next node with the smallest frequency
        # Create a new internal node with these two nodes as children
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)  # Add the merged node back to the heap
    
    return heap[0]  # Return the root of the Huffman tree

# Function to generate Huffman codes for each symbol
def generate_huffman_codes(root):
    # Generate binary codes for each symbol by traversing the Huffman tree
    codes = {}  # Dictionary to hold the symbol and its corresponding code
    generate_codes_helper(root, '', codes)  # Start generating codes from the root
    return codes 

# recursive helper function to generate codes for each symbol
def generate_codes_helper(node, current_code, codes):
    if node is None:
        return
    if node.symbol is not None:
        codes[node.symbol] = current_code  # Assign code to the symbol
    # Traverse left (add '0') and right (add '1') to generate codes
    generate_codes_helper(node.left, current_code + '0', codes)
    generate_codes_helper(node.right, current_code + '1', codes)

def write_output_file(file_path, codes, symbols_freq):
    # Write the generated codes and average bits per symbol to the output file
    total_bits = 0  # To accumulate total bits used
    total_freq = sum(freq for _, freq in symbols_freq)  # Total frequency of all symbols
    
    # Write the codes and average bits per symbol to the output file
    with open(file_path, 'w') as file:
        file.write("Symbol Codeword\n")  # Header for output file
        for symbol, freq in symbols_freq:
            codeword = codes[symbol]  # Get the code for the symbol
            file.write(f"{symbol} {codeword}\n")  # Write symbol and codeword to file
            total_bits += len(codeword) * freq  # Accumulate total bits used
        
        avg_bits_per_symbol = total_bits / total_freq  # Calculate average bits per symbol
        file.write(f"Average number of bits used per symbol: {avg_bits_per_symbol:.3f}\n")

# Defintion for Huffman's algorithm, i.e. the main function
def huffman_algo(input_file, output_file):
    # Main function to execute Huffman's algorithm
    symbols_freq = read_input_file(input_file)  # Read symbols and frequencies
    huffman_tree_root = build_huffman_tree(symbols_freq)  # Build Huffman tree
    huffman_codes = generate_huffman_codes(huffman_tree_root)  # Generate Huffman codes
    write_output_file(output_file, huffman_codes, symbols_freq)  # Write output to file

def process_all_files(input_dir, output_dir):
    # Process all .txt files in the input directory and generate output files
    for file_name in os.listdir(input_dir):
        if file_name.endswith(".txt"):  # Check for .txt files
            input_file = os.path.join(input_dir, file_name)  # Full path to input file
            output_file = os.path.join(output_dir, file_name + "_output.txt")  # Output file path
            huffman_algo(input_file, output_file)  # Execute Huffman's algorithm

# Entry point for the program
if __name__ == "__main__":
    input_dir = "Inputs"  # Directory containing input files
    output_dir = "Outputs"  # Directory for output files
    process_all_files(input_dir, output_dir)  # Process all input files
