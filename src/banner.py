import pyfiglet
def print_banner():
# Get the version from the file

# Create the banner text
banner = pyfiglet.figlet_format("QNMP"
+ "v1.0", font="slant")
# Print the header with a border of special characters
print("#" * 75)
print(banner) # ASCII art for the program name and version
print("#" * 75)