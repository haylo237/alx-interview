def canUnlockAll(boxes):
    opened = [False] * len(boxes)
    opened[0] = True
    keys = boxes[0]
    index = 0

    while index < len(keys):
        current_key = keys[index]
        if current_key < len(boxes) and not opened[current_key]:
            opened[current_key] = True
            keys.extend(boxes[current_key])
        index += 1

    return all(opened)
