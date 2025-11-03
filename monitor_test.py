from monitor import Monitor


def main():
    test_monitor = Monitor("Tester", 1920, 1080)
    print(test_monitor.get_resolution())
    print(test_monitor.get_total_pixels())


if __name__ == '__main__':
    main()