import sys

# Check if exactly two arguments are passed
if len(sys.argv) != 3:
    print("Usage: python cl_args.py $n1 $n2")
    sys.exit(1)

try:
    # Convert command-line arguments to integers
    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])

    # Compute and display the sum
    total = n1 + n2
    print(f"Sum of {n1} and {n2} is: {total}")

except ValueError:
    print("Error: Please enter valid integers.")

