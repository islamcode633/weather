"""
A wrapper script for retrieving weather information
using the wttr.in console service.
"""

from subprocess import run
import sys


def main():
    """ Receiving weather information """
    try:
        city = sys.argv[1]
        command =  f"curl wttr.in/{city}"
        run(command.split(), check=True)
    except IndexError as e:
        print(e)


if __name__ == '__main__':
    main()
