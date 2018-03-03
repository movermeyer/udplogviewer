

About
=====

This is a small utility that receives log messages sent over udp via the udp
handler which is built into the python standard library.

The utility listens to udp port 9021. To test the utility, run the example_client.py
file. To run the logger, run the udplogreceiver script.

Installation
------------

You can install the logviewer via pip:

.. code:: bash

  $ pip install udplogviewer


Usage
-----

The package includes one script, the log viewer. To hook a client script, add
the udp handler (built in python module) to your logging system:

.. code:: python

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    udp_handler = logging.handlers.DatagramHandler('localhost', 9021)
    udp_handler.setLevel(logging.DEBUG)
    logger.addHandler(udp_handler)


Dependencies
------------

- python3
- PyQt4 or PyQt5 Qt bindings


Screenshot
----------

.. image:: screenshot.png


Status
------

.. image:: https://img.shields.io/pypi/dm/udplogviewer.svg
    :target: https://pypi.python.org/pypi/udplogviewer

.. image:: https://img.shields.io/pypi/v/udplogviewer.svg
    :target: https://pypi.python.org/pypi/udplogviewer
