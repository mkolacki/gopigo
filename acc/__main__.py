"""
This module is the main module of the ACC program.

Running this module will start up the ACC and run the webserver for the user
interface.
"""

#import acc
import api

def main():
    """
    The main function of the ACC program. It starts up the ACC and runs the
    webserver for the user interface.
    """
    api.run(True)

if __name__ == "__main__":
    main()
