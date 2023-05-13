#!/usr/bin/python3
def element_at(my_list, jdx):
    if jdx < 0:
        return (None)

    length = len(my_list)

    if jdx > length - 1:
        return (None)

    return(my_list[jdx])j
