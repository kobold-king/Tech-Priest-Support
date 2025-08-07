def line_center(line):
    line = "this is a test"
    max_w = 50
    line_w = len(line)
    empty = (max_w - line_w - 2) // 2
    if (empty * 2)+ 2 + line_w < max_w:
        empty_2 = empty + 1
    else:
        empty_2 = empty

    new_line = "|" + " " * empty + line + " " * empty_2 + "|"
    print(new_line)
