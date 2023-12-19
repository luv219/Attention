import difflib
from tkinter import Tk, filedialog

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def compare_files(file1_content, file2_content):
    d = difflib.Differ()
    diff = d.compare(file1_content.splitlines(), file2_content.splitlines())
    return '\n'.join(diff)

def calculate_similarity_percentage(file1_content, file2_content):
    matcher = difflib.SequenceMatcher(None, file1_content, file2_content)
    similarity_ratio = matcher.ratio()
    return similarity_ratio * 100

def ask_for_file_path():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

def main():
    # Get file paths from the user
    file1_path = ask_for_file_path()
    file2_path = ask_for_file_path()

    # Read file contents
    file1_content = read_file(file1_path)
    file2_content = read_file(file2_path)

    # Compare files and calculate similarity
    comparison_result = compare_files(file1_content, file2_content)
    similarity_percentage = calculate_similarity_percentage(file1_content, file2_content)

    # Print results
    print("\nComparison Result:")
    print(comparison_result)
    print("\nSimilarity Percentage: {:.2f}%".format(similarity_percentage))

if __name__ == "__main__":
    main()
