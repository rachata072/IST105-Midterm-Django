import requests
import time
import random
from concurrent.futures import ThreadPoolExecutor

def perform_calculation(url):
    operations = ['add', 'sub', 'mul', 'div']
    while True:
        try:
            # Generate random numbers
            num1 = random.randint(1, 1000)
            num2 = random.randint(1, 1000)
            operation = random.choice(operations)
            
            # Make the request
            response = requests.post(url, data={
                'input1': num1,
                'input2': num2,
                'operation': operation
            })
            
            # Print status
            print(f"Request completed with status: {response.status_code}")
            
            # Small delay to prevent overwhelming the server
            time.sleep(0.1)
            
        except Exception as e:
            print(f"Error occurred: {e}")
            time.sleep(1)

def main():
    # Replace with your load balancer URL
    load_balancer_url = "http://your-load-balancer-url/calculate/"
    
    # Number of concurrent threads
    num_threads = 50
    
    print(f"Starting stress test with {num_threads} concurrent threads")
    print(f"Target URL: {load_balancer_url}")
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(perform_calculation, load_balancer_url) 
                  for _ in range(num_threads)]
        
        # Wait for all threads to complete (they won't in this case as they run indefinitely)
        for future in futures:
            future.result()

if __name__ == "__main__":
    main() 