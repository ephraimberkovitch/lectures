def cpu_bound(x):
    count = 0
    for i in range(0, x**x):
      count += 1
    return count

def io_bound(i):
    file_name = "file" + str(i) + ".txt"
    f = open(file_name, "w")
    print("writing to a file")
    for j in range(0, 8 ** 8):
        f.write("This is a sample text")
