"""
Problem 1: Duplicate Tracker

You are given a collection of product IDs. Some IDs may appear more than once.
Write a function that returns True if any duplicates are found, and False otherwise.

Example:
Input: [10, 20, 30, 20, 40]
Output: True

Input: [1, 2, 3, 4, 5]
Output: False
"""

def has_duplicates(product_ids):
    # Your implementation here
    seen = set()
    for ids in product_ids:
        if ids in seen:
            return True
        seen.add(ids)
    return False

print(has_duplicates([10,20,30,40]))  # Output: False
print(has_duplicates([10,20,30,20])) # Output: True

# Justification: A set works best for detecting duplicates because it automatically stores
# unique values. This operations that are used are efficient so this approach could be used 
# for much larger lists.

"""
Problem 2: Order Manager

You need to maintain a list of tasks in the order they were added, and support removing tasks from the front.
Implement a class that supports add_task(task) and remove_oldest_task().

Example:
task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
task_queue.remove_oldest_task() → "Email follow-up"
"""

class TaskQueue:
    def __init__(self):
        # Your initialization here
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_oldest_task(self):
        if len(self.tasks) == 0:
            return None
        return self.tasks.pop(0)

task_queue = TaskQueue()
task_queue.add_task("Email follow-up")
task_queue.add_task("Code review")
print(task_queue.remove_oldest_task())  # Output: "Email follow-up"

# Justification: A list works for this problem because it naturally preserves the order in whcih tasks are added,
# and allows for easy removal of the oldest tasks. By appending the new tasks to the end, the oldest tasks
# are in the front so they will be removed first.
"""
Problem 3: Unique Value Counter

You receive a stream of integer values. At any point, you should be able to return the number of unique values seen so far.

Example:
tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
tracker.get_unique_count() → 2
"""

class UniqueTracker:
    def __init__(self):
        self.values = set()

    def add(self, value):
        self.values.add(value)

    def get_unique_count(self):
        return len(self.values)

tracker = UniqueTracker()
tracker.add(10)
tracker.add(20)
tracker.add(10)
print(tracker.get_unique_count())  # Output: 2

# Justification: A set is used here because it automatically handles uniqueness. 
# When a value is added, if it already exists in the set, it will not be added again. 
# This allows for efficient tracking of unique values and counting them.