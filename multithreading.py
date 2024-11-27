from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    
    time.sleep(1)
    return f"Number :{number}"

numbers=[1,2,3,4,5]

# Create a ThreadPoolExecutor with a maximum of 3 threads
with ThreadPoolExecutor(max_workers=3) as executor:
    results = executor.map(print_number, numbers)

    # Print results as they complete
    for result in results:
        print(result)
