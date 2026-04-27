import pyfiglet


def print_banner():
    """
    Print the project banner using ASCII art.

    Uses the pyfiglet library to display the project name and version
    in a stylized format, surrounded by a decorative border.
    """
    banner = pyfiglet.figlet_format("QNMP v1.0", font="slant")

    print("#" * 75)
    print(banner)
    print("#" * 75)