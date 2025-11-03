from monitor import Monitor


def main():
    original_test_monitor = Monitor("Tester", 1920, 1080)
    other_test = Monitor("Other Tester", 200, 400)
    identical_test_monitor = Monitor("Tester", 1920, 1080)

    print(original_test_monitor.get_resolution(), (1920, 1080))
    print(original_test_monitor.get_total_pixels(), 1920 * 1080)
    print(original_test_monitor == other_test, False)
    print(original_test_monitor == identical_test_monitor, True)


if __name__ == '__main__':
    main()
