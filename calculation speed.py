#!/usr/bin/env python
# encoding: utf-8

import os
import logging
import argparse

def create_logger(logger_name,
                  log_format=None,
                  log_level=logging.INFO,
                  log_path=None):
    logger = logging.getLogger(logger_name)
    assert (len(logger.handlers) == 0)
    logger.setLevel(log_level)
    if log_path is None:
        handler = logging.StreamHandler()
    else:
        os.stat(os.path.dirname(os.path.abspath(log_path)))
        handler = logging.FileHandler(log_path)
    handler.setLevel(log_level)
    if log_format is not None:
        formatter = logging.Formatter(log_format)
        handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


logger = create_logger(
    logger_name='template',
    log_format='[%(asctime)s %(name)-13s \
                %(levelname)s %(process)d \
                %(thread)d %(filename)s:%(lineno)-5d] \
                %(message)s',
    log_level=logging.INFO)

parser = argparse.ArgumentParser()
parser.add_argument("--a", default=3, type=int, help='one param to caculate')
parser.add_argument("--b", default=8, type=int, help='another param to caculate')
args = parser.parse_args()


def calculate(a, b):
    times = 10000000

    logger.info("Adding {} and {} by {} times".format(a, b, times))
    for i in range(times):
        a + b
    logger.info("Done")

    logger.info("Subtracting {} and {} by {} times".format(a, b, times))
    for i in range(times):
        a - b
    logger.info("Done")

    logger.info("Multiplying {} and {} by {} times".format(a, b, times))
    for i in range(times):
        a * b
    logger.info("Done")

    logger.info("Dividing {} and {} by {} times".format(a, b, times))
    for i in range(times):
        a / b
    logger.info("Done")

    logger.info("Powering {} and {} by {} times".format(a, b, times))
    for i in range(times):
        a ** b
    logger.info("Done")


def main():
    calculate(args.a, args.b)
    exit(0)


if __name__ == '__main__':
    main()
