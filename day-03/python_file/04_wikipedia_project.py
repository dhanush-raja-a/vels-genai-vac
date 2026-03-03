# Day 03 Project: Wikipedia Text Fetcher
# This script combines functions, APIs, and file handling.

import requests

def fetch_wikipedia_summary(topic):
    """
    Fetches the summary of a Wikipedia page using its REST API.
    """
    # Wikipedia Summary API endpoint
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    
    print(f"Fetching summary for: {topic}...")
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        summary = data.get('extract', 'No summary available.')
        return summary
    else:
        return f"Error: Could not find page for '{topic}'."

def save_to_file(filename, content):
    """
    Saves the provided content to a text file.
    """
    with open(filename, "w") as file:
        file.write(content)
    print(f"Content successfully saved to {filename}")

def main():
    # 1. Ask user for a topic
    topic = input("Enter a topic (e.g., Python_programming, NLP): ").strip()
    
    # 2. Fetch data from API
    summary = fetch_wikipedia_summary(topic)
    
    print("\n--- Summary Snippet ---")
    print(summary[:200] + "...") # Print first 200 characters
    
    # 3. Save it to a file
    output_file = "wikipedia_data.txt"
    save_to_file(output_file, summary)

if __name__ == "__main__":
    main()
