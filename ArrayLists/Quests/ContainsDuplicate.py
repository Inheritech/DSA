def contains_duplicate(arr):
    existing = set()
    for i in arr:
        if i in existing:
            return True
        existing.add(i)
    return False