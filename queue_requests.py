from queue import Queue
import time

queue = Queue()

def main():
    while True:
        generate_request()
        print(f"Current requests:\n{queue.queue}\n")
        
        print("Processing...") 
        time.sleep(1)
        process_request()

        print("\nAll requests processed sucessfully")
        should_shutdown = input("Enter 'y' or any symbol if you want to continue work of service center. Enter 'n' if you want to shutdown it >>> ")
        if should_shutdown == 'n':
            break

def generate_request():
    request = Request(generate_unique_id())
    queue.put(request)

def process_request():
    if queue.qsize() > 0:
        while queue.qsize() > 0:
            request = queue.get()
            print(f"Request {request.id} processed successfully")
    else:
        print("Requests queue is empty right now, nothing to")


def generate_unique_id():
    return next(id_generator)

def unique_id_generator():
    unique_id_counter = 0

    while True:
        yield unique_id_counter
        unique_id_counter += 1

id_generator = unique_id_generator()

class Request():
    def __init__(self, id):
        self.id = id
    
    def __repr__(self):
        return f"Request {self.id}"


if __name__ == "__main__":
    main()