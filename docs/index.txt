sigdebug
========

* `Bugs <https://github.com/f0rk/sigdebug/issues/>`_

.. contents::

.. comment: split here

Status and License
------------------

``sigdebug`` is set a debug aids that work by installing them as signal
handlers.

It was written by Ryan Kelly, with inspiration from `this Stack Overflow thread
<http://stackoverflow.com/questions/132058/getting-stack-trace-from-a-running-python-application>`_.

It is licensed under an
`BSD-style permissive license <https://github.com/f0rk/sigdebug/raw/master/LICENSE>`_.

You can install it with ``easy_install sigdebug``.

What It Does
------------

``sigdebug`` can be used to install signal handlers that can help you debug
your program. It comes with an interactive handler, which will drop you into a
``pdb`` shell, a traceback printer, and a handler for printing the traceback
for every thread.

The basic problem being addressed is one of how to enter into a debugger on a
program that seems to be stuck or hung. With this module, you can register the
signal handler and signal the program, allowing you to interact with it at the
point at which it appears to be hung.

The basic usage is::

    import sigdebug
    sigdebug.debug()

This installs the interactive handler for SIGUSR1.

Also available are::

    import signal
    from sigdebug import register, stack, threadstacks
    register(signal.SIGQUIT, stack) # print the stacktrace of the main thread
    register(signal.SIGQUIT, threadstacks) # print stacks for all threads

Of course, the second register call clobbers the first: you only get one
handler, not both.

Windows Notes
~~~~~~~~~~~~~

See the notes provided for ``signal`` in the Python standard library.

PyPy Support
~~~~~~~~~~~~

Supported.

Contributing
------------

`Pull requests! <https://github.com/f0rk/sigdebug/>`_

