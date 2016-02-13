import os.path


def check_file(filename):
    home = os.path.expanduser("~")
    filename.replace("~", home)
    if (os.path.isfile(filename)) is False:
        return (False)
    form = format_ok(filename)
    if form is False:
        print ("Failure")
    return (form)


def format_ok(fname):
    with open(fname, "r") as f:
        content = f.readlines()
    change = 0
    length = 0
    ret = ""
    for line in content:
        if len(line.rstrip('\n')) != length and change is 0:
            length = len(line.rstrip('\n'))
            change = 1
        elif len(line.rstrip('\n')) != length and change is 1:
            # print(line.rstrip('\n'))
            return (False)
        ret = ret + line
    return (ret)

if __name__ == '__main__':
    check_file("maps/test3.txt")
