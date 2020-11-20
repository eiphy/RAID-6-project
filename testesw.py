with open('222.txt', 'r+') as f:
    content=['w1', 'w2', '3']
    print(f.read(1))
    f.seek(0)
    print(f.read(1))
    f.seek(2)
    for c in content:
        print(c)
        f.write(c)

    for i in range(5):
        print(i)
