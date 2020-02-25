def FizzBuzz(d,m):
    s = ""
    l = sorted(d)
    for i in l:
        if m % i == 0:
            s += d[i]
    if s == "":
        print(m)
    else:
        print(s)
            

if __name__ == "__main__":
    d = {}
    m = 0
    f = open("./input.txt")
    line = f.readline()
    while line :
        if ":" in line:
            x = line.split(":")
            key = int(x[0])
            value = x[1].replace("\n","")
            d[key] = value
        elif line != "":
            m = int(line)
        line = f.readline()
    f.close()
    FizzBuzz(d,m)
    
