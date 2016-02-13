import os.path


def check_file(filename):
    home = os.path.expanduser("~")
    filename.replace("~", home)
    if (os.path.isfile(filename)) is False:
        return (False)
    form = format_ok(filename)
    if form is False:
        return (False)
    else:
        print(form)


def format_ok(fname):
    with open(fname, "r") as f:
        content = f.readline()
        length = len(content)
        for line in f:
            if (len(line) != length):
                return (False)
            else:
                content = content + f.readline()
        return (content)

if __name__ == '__main__':
    check_file("test.txt")
