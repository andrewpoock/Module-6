def measurements(x):
    if len(x) == 2:
        def area():
            return float(x[0]*x[1])

        def perimeter():
            return float(x[0]*2 + x[1]*2)
    elif len(x) == 1:
        def area():
            return float(x[0]*x[0])
        def perimeter():
            return float(x[0]*4)

    s = "Perimeter = " + str(perimeter()) + " Area = " + str(area())
    return s


if __name__ == '__main__':
    print(measurements([2, 3]))
