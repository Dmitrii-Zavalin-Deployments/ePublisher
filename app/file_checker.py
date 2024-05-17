import os

def get_max_file_number(directory):
    """Get the maximum number from file names in the directory."""
    max_number = -1
    for filename in os.listdir(directory):
        name, _ = os.path.splitext(filename)
        if name.isdigit():
            max_number = max(max_number, int(name))
    return max_number

def check_sequential_files(directories):
    """Check if files with sequential numeric names exist in all directories."""
    max_numbers = [get_max_file_number(directory) for directory in directories]
    max_number = min(max_numbers)  # Use the smallest max_number to ensure sequence in all directories
    missing_files = {directory: [] for directory in directories}
    for i in range(max_number + 1):
        for directory in directories:
            expected_filename = f"{i}.txt" if 'text' in directory or 'hashtags' in directory else f"{i}.png"
            if not os.path.isfile(os.path.join(directory, expected_filename)):
                missing_files[directory].append(expected_filename)
    return missing_files

def calculate_remainder(run_number, max_number):
    """Calculate the remainder of run_number divided by max_number."""
    return run_number % (max_number + 1)  # +1 because max_number is an index, and we need count
