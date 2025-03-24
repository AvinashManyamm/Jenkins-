 class CLArgs2 {
    public static void main(String[] args) {
        // Check if exactly two arguments are passed
        if (args.length != 2) {
            System.out.println("Usage: java CLArgs $n1 $n2");
            return;
        }

        try {
            // Convert command-line arguments to integers
            int n1 = Integer.parseInt(args[0]);
            int n2 = Integer.parseInt(args[1]);

            // Compute and display the sum
            int sum = n1 + n2;
            System.out.println("Sum of " + n1 + " and " + n2 + " is: " + sum);
        } catch (NumberFormatException e) {
            System.out.println("Error: Please enter valid integers.");
        }
    }
}

