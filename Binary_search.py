class BinarySearch:
    def __init__(self, arr):
        self.arr = arr

    def search(self, target):
        left, right = 0, len(self.arr) - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the target is at the middle
            if self.arr[mid] == target:
                return mid

            # If target is greater, ignore the left half
            elif self.arr[mid] < target:
                left = mid + 1

            # If target is smaller, ignore the right half
            else:
                right = mid - 1

        # Target not found
        return -1


if __name__ == "__main__":
    # User input for array and target
    arr = list(map(int, input("Enter a sorted list of numbers (separated by spaces): ").split()))
    target = int(input("Enter the target number to search for: "))

    # Create a BinarySearch object and search for the target
    binary_search = BinarySearch(arr)
    result = binary_search.search(target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")