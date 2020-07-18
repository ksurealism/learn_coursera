def place_boxes(a1, b1, c1, a2, b2, c2):
    boxes_count = 0
    nxt = (a1 // a2) * (b1 // b2) * (c1 // c2)
    if nxt > boxes_count:
        boxes_count = nxt
    nxt = (a1 // b2) * (b1 // a2) * (c1 // c2)
    if nxt > boxes_count:
        boxes_count = nxt
    nxt = (a1 // c2) * (b1 // a2) * (c1 // b2)
    if nxt > boxes_count:
        boxes_count = nxt
    nxt = (a1 // a2) * (b1 // c2) * (c1 // b2)
    if nxt > boxes_count:
        boxes_count = nxt
    nxt = (a1 // b2) * (b1 // c2) * (c1 // a2)
    if nxt > boxes_count:
        boxes_count = nxt
    nxt = (a1 // c2) * (b1 // b2) * (c1 // a2)
    if nxt > boxes_count:
        boxes_count = nxt
    return boxes_count


if __name__ == "__main__":
    arg1 = int(input())
    arg2 = int(input())
    arg3 = int(input())
    arg4 = int(input())
    arg5 = int(input())
    arg6 = int(input())
    result = place_boxes(arg1, arg2, arg3, arg4, arg5, arg6)
    print(result)
