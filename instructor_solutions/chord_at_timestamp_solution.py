def chord_at(changes: list[tuple[int, str]], time: int) -> str | None:
    if not changes or time < changes[0][0]:
        return None

    left, right = 0, len(changes) - 1
    while left < right:
        mid = (left + right + 1) // 2
        if changes[mid][0] <= time:
            left = mid
        else:
            right = mid - 1

    return changes[left][1]
