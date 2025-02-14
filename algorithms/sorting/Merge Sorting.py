def merge(a, b):  # < Defining merge function with parameters (a,b)
    c = []  # < Create a list, and keep empty
    while (len(a) > 0 and len(b) > 0):  # < While parameters (a,b) have values, run the loop. Otherwise stop.

        if a[0] < b[0]:
            c.append(a[0])  # {Sort values from list: a into list: c}
            a.remove(a[0])  #

        else:
            c.append(b[0])  # {Otherwise, put the value from list: b to list: c}
            b.remove(b[0])  #
        # print(c)

    while (len(a) > 0):  # < When len(a) has a value,
        c.append(b[0])  # < replace len(b) with len(c)
        b.remove(b[0])  # < remove len(b)

        # When len(b) has a value
        while (len(b) > 0):
            c.append(b[0])  # < replace len(b) with len(c),
            b.remove(b[0])  # < remove len(b)
            return c  # < Returns values to list: c, allowing to use the list outside of the function

# Defines split function (nlogn)
def msort(p):
    if len(p) == 1:  # < If array only has one value, then it is sorted
        return p
    else:
        mid = int(len(p) / 2)  # < Splitting mid in 2 parts
        left = p[0:mid]  # < Everything from the first point to the left side of the mid
        right = p[mid:len(p)]  # < Everything from first point to right side of the mid

    left = msort(left)  # < Splitting multiple times, until there is one (recursion)
    right = msort(right)  # < Splitting right side multiple times, until there is one (recursion)
    return merge(left, right)  # < Returning the result of the function, and merging them together


x = [3, 11, 2, 6, 7, 8, 30]
print(x)
z = msort(x)
print(z)