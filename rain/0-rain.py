#!/usr/bin/python3
def rain(walls):
    """Collecting water between walls"""
    if not walls:
        return 0  # No walls, no water

    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    water_trapped = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, walls[left])
            water_trapped += max(0, left_max - walls[left])
        else:
            right -= 1
            right_max = max(right_max, walls[right])
            water_trapped += max(0, right_max - walls[right])

    return water_trapped