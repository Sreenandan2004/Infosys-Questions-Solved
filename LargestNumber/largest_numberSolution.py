import functools

def largest_number(arr: list[str]) -> str:
    """
    Arranges an array of strings representing non-negative integers
    to form the largest possible number. Returns the result as a string.
    """
    # Custom comparison function
    def compare(x: str, y: str) -> int:
        # Compare concatenated versions: x + y vs y + x
        if x + y > y + x:
            return -1  # x should come before y (ascending order representation)
        elif x + y < y + x:
            return 1   # y should come before x
        else:
            return 0

    # Sort using our custom comparison logic converted to a key function
    sorted_arr = sorted(arr, key=functools.cmp_to_key(compare))
    
    # If the largest number is "0", the entire concatenated number is 0
    if sorted_arr[0] == "0":
        return "0"
        
    return "".join(sorted_arr)

if __name__ == "__main__":
    # Test cases
    arr1 = ["3", "30", "34", "5", "9"]
    print(f"Input: {arr1} -> Output: {largest_number(arr1)}")
    
    arr2 = ["54", "546", "548", "60"]
    print(f"Input: {arr2} -> Output: {largest_number(arr2)}")
    
    arr3 = ["0", "0", "0"]
    print(f"Input: {arr3} -> Output: {largest_number(arr3)}")
