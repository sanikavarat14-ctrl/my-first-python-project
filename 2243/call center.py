from collections import deque

# Create a queue
call_queue = deque()

def addCall(customerID, callTime):
    call_queue.append((customerID, callTime))
    print(f"Call added: Customer ID = {customerID}, Call Time = {callTime} min")


def answerCall():
    if not call_queue:
        print("Queue is empty. No calls to answer.")
    else:
        customerID, callTime = call_queue.popleft()
        print(f"Answered call: Customer ID = {customerID}, Call Time = {callTime} min")


def viewQueue():
    if not call_queue:
        print("Queue is empty.")
    else:
        print("\nCalls currently in queue:")
        for customerID, callTime in call_queue:
            print(f"Customer ID: {customerID}, Call Time: {callTime} min")


def isQueueEmpty():
    return len(call_queue) == 0


# Main program
while True:
    print("\n--- Call Center Queue ---")
    print("1. Add Call")
    print("2. Answer Call")
    print("3. View Queue")
    print("4. Check if Queue is Empty")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customerID = input("Enter Customer ID: ")
        callTime = int(input("Enter Call Time (minutes): "))
        addCall(customerID, callTime)

    elif choice == 2:
        answerCall()

    elif choice == 3:
        viewQueue()

    elif choice == 4:
        if isQueueEmpty():
            print("Queue is empty.")
        else:
            print("Queue is not empty.")

    elif choice == 5:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")
