import re
import os  # Don't forget to import the os module

def urls(file_path):  # No changes needed here
    urls = []
    url_regex = r"(https?://(?:www\.)?\w+\.\w+)"
    with open(file_path, 'r') as file:
        for line in file:
            matches = re.findall(url_regex, line)
            urls.extend(matches)
    return urls

def main():
    file_path = input("Enter the path to the text file: ")  # Prompt user for file path
    if os.path.exists(file_path):  # Check if the file exists
        found_urls = urls(file_path)
        if found_urls:
            print("URLs found in the file:")
            for url in found_urls:
                print(url)
        else:
            print("No URLs found in the file.")
    else:
        print("File not found. Please enter a valid file path.")  # Notify if file not found

if __name__ == "__main__":
    main()
