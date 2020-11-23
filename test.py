import util as U


def test_data_to_gn():
    a = [[124, 125, 11], 125, [35, [74]]]
    b = U.data_to_gn(a)
    print(b)


if __name__ == "__main__":
    test_data_to_gn()
