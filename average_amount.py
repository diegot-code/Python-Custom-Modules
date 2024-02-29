
def calculate_average(numbers):
    if not numbers:
        return "List is empty, cannot calculate average"
    else:
        return sum(numbers) / len(numbers)

if __name__ == "__main__":
    # This block will be executed if the script is run directly
    print("This script is meant to be imported, not run directly.")
