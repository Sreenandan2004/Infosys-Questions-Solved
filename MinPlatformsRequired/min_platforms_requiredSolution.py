def time_to_minutes(t) -> int:
    """
    Helper function to convert a time representation (string 'HH:MM' or integer HHMM)
    into minutes from midnight.
    """
    if isinstance(t, str):
        parts = t.split(':')
        hours = int(parts[0])
        minutes = int(parts[1])
        return hours * 60 + minutes
    elif isinstance(t, (int, float)):
        # Treat as HHMM format (e.g., 900 -> 9:00 -> 9 * 60 + 0 = 540)
        hours = int(t) // 100
        minutes = int(t) % 100
        return hours * 60 + minutes
    return int(t)

def find_platform(arr: list, dep: list) -> int:
    """
    Finds the minimum number of platforms required for the railway station.
    Accepts arrival and departure arrays representing times as HH:MM strings or HHMM integers.
    """
    # Convert all arrival and departure times to minutes from midnight
    arr_min = sorted([time_to_minutes(t) for t in arr])
    dep_min = sorted([time_to_minutes(t) for t in dep])
    
    n = len(arr_min)
    i = 0  # Pointer for arrivals
    j = 0  # Pointer for departures
    
    current_platforms = 0
    max_platforms = 0
    
    # Traverse through all arrival and departure events chronologically
    while i < n and j < len(dep_min):
        # If the next event is an arrival
        if arr_min[i] <= dep_min[j]:
            current_platforms += 1
            max_platforms = max(max_platforms, current_platforms)
            i += 1
        # If the next event is a departure
        else:
            current_platforms -= 1
            j += 1
            
    return max_platforms

if __name__ == "__main__":
    # Test cases
    # Example 1: Given as strings
    arr1 = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
    dep1 = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
    print(f"Arrivals: {arr1}")
    print(f"Departures: {dep1}")
    print(f"Minimum Platforms: {find_platform(arr1, dep1)}\n")
    
    # Example 2: Given as strings
    arr2 = ["9:00", "9:40"]
    dep2 = ["9:10", "12:00"]
    print(f"Arrivals: {arr2}")
    print(f"Departures: {dep2}")
    print(f"Minimum Platforms: {find_platform(arr2, dep2)}\n")
    
    # Example 3: Given as integers (HHMM)
    arr3 = [900, 940, 950, 1100, 1500, 1800]
    dep3 = [910, 1200, 1120, 1130, 1900, 2000]
    print(f"Arrivals (int): {arr3}")
    print(f"Departures (int): {dep3}")
    print(f"Minimum Platforms: {find_platform(arr3, dep3)}\n")
