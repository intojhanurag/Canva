
'''
https://python.langchain.com/docs/introduction/

https://python.langchain.com/docs/concepts/

https://python.langchain.com/docs/tutorials/
'''

import threading
import requests

# List of URLs to fetch
urls = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/concepts/',
    'https://python.langchain.com/docs/tutorials/'
]

# Function to fetch content from a given URL
def fetch_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Successfully fetched content from {url}")
        else:
            print(f"Failed to fetch {url}, status code: {response.status_code}")
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")

# List to hold threads
threads = []

# Creating threads for each URL
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()  # Start the thread

# Join threads to ensure they all finish before the main program exits
for thread in threads:
    thread.join()

print("Finished fetching all content.")


