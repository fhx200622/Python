#!/usr/bin/env python
# -*- coding: utf-8 -*-

#nearest point

import os
import json
import math
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
parser.add_argument("--inputfile", default="", type=str, help='input directory')
parser.add_argument("--city", default="", type=int, help='target city')
args = parser.parse_args()


def distance(lat1, lon1, lat2, lon2):
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)
    return (lat1 - lat2) * (lat1 - lat2) + (lon1 - lon2) * (lon1 - lon2)

def find_nearest_point(inputfile, args):
    #read json
    input_json_file = os.path.abspath(inputfile) + "/input.json"
    if not os.path.exists(input_json_file):
        logger.error("file does not exist at: " + input_json_file)
        exit(1)
    logger.info("Loading input json at: " + input_json_file)
    with open(input_json_file) as fin:
        cities = json.load(fin)

    #get the target
    target_cities = list(filter(lambda x: x["name"] == city, cities))
    if not target_cities:
        logger.error("wrong city name: " + city)
        exit(1)
    if len(target_cities) > 1:
        logger.error("airport name is not unique: " + city)
        exit(1)
    target_city = target_cities[0]

    #find the nearest airpot
    nearest_city = None
    min_distance = 1000000;
    for city in cities:
        if city != target_city:
            dis = distance(target_city["lat"], target_city["lon"], \
                           city["lat"], city["lon"])
            if dis < min_distance:
                min_distance = dis
                nearest_city = city
    return nearest_city["name"]


def main():
	result = find_nearest_point(args.inputfile,args.city)
	print (result)
    exit(0)
 
 
if __name__ == '__main__':
    main()
