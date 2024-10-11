def canUnlockAll(boxes):
    n = len(boxes)
    seen_boxes = {0}
    keys = boxes[0]

    for key in keys:
        if key < n and key not in seen_boxes:
            seen_boxes.add(key)
            keys.extend(boxes[key])  # Add new keys to explore later

    return len(seen_boxes) == n
