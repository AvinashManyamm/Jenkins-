import sys

# Check if arguments are provided
if len(sys.argv) == 1:
    print("No command-line arguments provided.")
    print("Usage: python cl_args.py <arg1> <arg2> ...")
    sys.exit(1)

# Print all arguments
print("Command-line arguments:")
for i, arg in enumerate(sys.argv[1:], start=1):  # Skipping sys.argv[0] (script name)
    print(f"Argument {i}: {arg}")

