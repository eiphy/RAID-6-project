import galois_filed as GF
import util as U
from driver import Driver
from galois_filed import GaloisNum as GN


def GF_test():
    print("Power Table")
    temp = []
    for i in range(1, 257):
        if i % 17 == 0:
            print(" ".join(temp))
            temp = []
        else:
            temp.append("{:02x}".format(GN.power_table[i - 1]))
    print("Logarithm Table")
    temp = []
    for i in range(1, 257):
        if i % 17 == 0:
            print(" ".join(temp))
            temp = []
        else:
            temp.append("{:02x}".format(GN.log_table[i - 1]))
    a = GN(0x7D)
    b = GN(0x8F)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print("add:")
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print("sub:")
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print("mul:")
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print("div:")
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print("-------------------------------------------")
    a = GN(10)
    b = GN(2)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print("add:")
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print("sub:")
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print("mul:")
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print("div:")
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print("-------------------------------------------")
    a = GN(200)
    b = GN(2)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print("add:")
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print("sub:")
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print("mul:")
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print("div:")
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print("-------------------------------------------")
    a = GN(0)
    b = GN(2)
    print(a, a.get_bin(), a.get_dec())
    print(b, b.get_bin(), b.get_dec())

    print("add:")
    c = a + b
    print(c, c.get_bin(), c.get_dec())
    print("sub:")
    c = a - b
    print(c, c.get_bin(), c.get_dec())
    print("mul:")
    c = a * b
    print(c, c.get_bin(), c.get_dec())
    print("div:")
    c = a / b
    print(c, c.get_bin(), c.get_dec())
    print("-------------------------------------------")

    # a = GN(2)
    # b = GN(0)
    # print(a, a.get_bin(), a.get_dec())
    # print(b, b.get_bin(), b.get_dec())

    # print("add:")
    # c = a + b
    # print(c, c.get_bin(), c.get_dec())
    # print("sub:")
    # c = a - b
    # print(c, c.get_bin(), c.get_dec())
    # print("mul:")
    # c = a * b
    # print(c, c.get_bin(), c.get_dec())
    # print("div:")
    # c = a / b
    # print(c, c.get_bin(), c.get_dec())
    # print("-------------------------------------------")

    a = GF.pow2(-2)
    b = GF.pow2(253)
    c = GF.pow2(257)
    print(f"2^{-2}", hex(a.value), a.get_bin(), a.get_dec())
    print(f"2^{253}", hex(b.value), b.get_bin(), b.get_dec())
    print(f"2^{257}", hex(c.value), c.get_bin(), c.get_dec())


def test_data_to_gn():
    a = [[124, 125, 11], 125, [35, [74]]]
    b = U.data_to_gn(a)
    print(b)


def test_data_conversion():
    a = "hello world! \n from there is somthing different. here."
    data = [ord(c) for c in a]
    data = U.strip_data(data, 10)
    # _data = U.block_data_to_seq(data)

    # temp = []
    # for d in _data:
    #     temp.append(chr(d))
    # print("".join(temp))

    for block in data:
        print(len(block))


def RAID_t_test():
    driver = Driver(6, clear=True)
    driver.write_data(
        "Singapore Airlines is continuing to build back its North American route network with more flights to more cities across the US, ending an eight-month holding pattern during the pandemic that saw the airline operate only one American route.\nOn the heels of launching its newest route just last week between Singapore and New York, which earned the top spot of the world's longest flight by distance, the flag carrier is doubling down with increased flights to the West Coast. Starting in December, Los Angeles will see an increase in daily flights while San Francisco will see its first scheduled flights since April, both laying the foundation for the airline's post-pandemic recovery.\nThe first flight to San Francisco will depart Singapore on December 15 and return\ntwo days later on December 17. The Bay Area will start with three-times-weekly service departing to Singapore on Mondays, Thursdays, and Saturdays as the airline settles into the new route, which sees a duration of 14 hours and 40 minutes on the outbound leg and 17 hours and 35 minutes on the return. Los Angeles, for its part, will see increased frequencies from three weekly flights to five starting December 2, with service on all days of the week except Thursdays and Saturdays. Singapore Airlines never stopped flying the Singapore-Los Angeles route throughout the pandemic, which became its sole non-stop link to the US. Here!!"
    )
    # d.write_data("hello word! \n This message from nobody.")
    driver.disks[4].lost_data()
    driver.disks[0].lost_data()
    print(driver.read_data())


if __name__ == "__main__":
    test_data_conversion()
