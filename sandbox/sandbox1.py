import rosebot


def main():
    robot = rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_less_than(50, 100)

main()