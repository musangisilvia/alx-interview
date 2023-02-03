#!/usr/bin/python3

"""
    0-lockboxes
"""


def canUnlockAll(boxes):
    """
        a function
        Params: boxes, a list of lists
        return: True if all boxes can be opened, else return False

        Check readme for details of what this function does
    """
    unlocked = [0]

    for box in boxes:
        if len(box) == 0:
            continue
        for key in box:
            if key != boxes.index(box) and key < len(boxes) \
                    and key not in unlocked:
                unlocked.append(key)

    if len(unlocked) == len(boxes):
        return True

    return False
