# Copyright 2011 Ryan P. Kelly <rpkelly@cpan.org>
#
# This code was inspired by this thread on stackoverflow:
# http://stackoverflow.com/questions/132058/getting-stack-trace-from-a-running-python-application
#
# This code is BSD licensed, please see LICENSE for the full text.

import sys
import signal
import traceback
import threading
from pdb import Pdb


__version__ = "0.2"


def interactive(signum, frame):
    """Enter into pdb at the location the process was interrupted.

    :param signum: The signal that was received.
    :param frame: A python stack frame.

    """
    banner = "Received signal %s, Entering console.\nTraceback:\n" % signum
    banner += "".join(traceback.format_stack(frame))
    print(banner)

    Pdb().set_trace(frame)

def stack(signum, frame):
    """When invoked, print out the Traceback for the provided stack frame.

    :param signum: The signal that was received.
    :param frame: A python stack frame.

    """
    print("Traceback:\n" + "".join(traceback.format_stack(frame)))

def threadstacks(signum, frame):
    """Print out the Traceback of every thread currently available.

    :param signum: The signal that was received.
    :param frame: A python stack frame.

    """
    for thread, stack in sys._current_frames().items():
        message = "Thread #%s Traceback:\n" % thread
        message += "".join(traceback.format_stack(frame))
        print(message)

def register(signum, handler):
    """Register the given handler function for the given signal.

    :param signum: The signal to respond to.
    :param handler: The handler function.

    """
    signal.signal(signum, handler)

def debug():
    """This function installs the interactive signal handler for SIGUSR1."""
    register(signal.SIGUSR1, interactive)

