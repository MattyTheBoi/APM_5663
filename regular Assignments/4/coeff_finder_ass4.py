import os

# Function to read the power series from a file
def read_power_series(file_path):
    with open(file_path, 'r') as file:
        n, k, m = map(int, file.readline().strip().split())
        coefficients = [float(file.readline().strip()) for _ in range(n + 1)]
    return n, k, m, coefficients

def multiply_series(a, b, m):
    result = [0] * (m + 1)
    for i in range(m + 1):
        for j in range(i + 1):
            if j < len(a) and (i - j) < len(b):
                result[i] += a[j] * b[i - j]
    return result

def compute_kth_power(n, k, m, coefficients):
    result = [1]  # Start with the series for 1 (neutral element for multiplication)
    for _ in range(k):
        result = multiply_series(result, coefficients, m)
    return result


# Function to compute the first m + 1 coefficients of the reciprocal of the power series
def compute_reciprocal(n, m, coefficients):
    if coefficients[0] == 0:
        return None  # Reciprocal does not exist if a0 is 0
    result = [0] * (m + 1)
    result[0] = 1 / coefficients[0]
    for i in range(1, m + 1):
        result[i] = -sum(coefficients[j] * result[i - j] for j in range(1, min(i, n + 1))) / coefficients[0]
    return result

# Function to compute the first m + 1 coefficients of the inverse of the power series
def compute_inverse(n, m, coefficients):
    # Check it DOESNT exist
    if coefficients[0] != 0 or coefficients[1] == 0:
        return None  # Inverse exists only if a0 = 0 and a1 != 0
    result = [0] * (m + 1)
    result[1] = 1 / coefficients[1]  # Inverse series starts with x / a1
    for i in range(2, m + 1):
        sum_terms = sum(coefficients[j] * result[i - j] for j in range(2, min(i + 1, len(coefficients))))
        result[i] = -sum_terms / coefficients[1]
    return result


# Function to write the output to a file
def write_output(file_path, kth_power, reciprocal, inverse):
    with open(file_path, 'w') as file:
        # Write existence of reciprocal
        if reciprocal is not None:
            file.write("Reciprocal exists.\n")
        else:
            file.write("Reciprocal does not exist.\n")
        
        # Write existence of inverse
        if inverse is not None:
            file.write("Inverse exists.\n")
        else:
            file.write("Inverse does not exist.\n")
        
        # Write k-th power coefficients
        file.write("k-th Power Coefficients:\n")
        file.write(" ".join(f"{coef:.8f}" for coef in kth_power) + "\n")
        
        # Write reciprocal coefficients (if exists)
        if reciprocal is not None:
            file.write("Reciprocal Coefficients:\n")
            file.write(" ".join(f"{coef:.8f}" for coef in reciprocal) + "\n")
        
        # Write inverse coefficients (if exists)
        if inverse is not None:
            file.write("Inverse Coefficients:\n")
            file.write(" ".join(f"{coef:.8f}" for coef in inverse) + "\n")

# Main function to process a single file
def process_file(input_filepath, output_filepath):
    n, k, m, coefficients = read_power_series(input_filepath)
    kth_power = compute_kth_power(n, k, m, coefficients)
    reciprocal = compute_reciprocal(n, m, coefficients)
    inverse = compute_inverse(n, m, coefficients)
    write_output(output_filepath, kth_power, reciprocal, inverse)

# Function to process all files in the input directory
def process_all_files(input_dir, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):  # Assuming input files have .txt extension
            input_filepath = os.path.join(input_dir, filename)
            output_filepath = os.path.join(output_dir, filename.replace(".txt", "_output.txt"))
            process_file(input_filepath, output_filepath)

# Entry point for the program
if __name__ == "__main__":
    input_dir = "Inputs"  # Directory containing input files
    output_dir = "Outputs"  # Directory for output files
    process_all_files(input_dir, output_dir)  # Process all input files
