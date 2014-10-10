#!/usr/bin/env python

import logging
import logging.handlers
import time

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
udp_handler = logging.handlers.DatagramHandler('localhost', 9021)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
udp_handler.setLevel(logging.DEBUG)
logger.addHandler(udp_handler)
logger.addHandler(ch)

logger.info('Hello world')
j = 0
while True:
    time.sleep(1)
    print(j)
    for i in range(100):
        logger.debug('Test {}'.format(i))
    j += 1
