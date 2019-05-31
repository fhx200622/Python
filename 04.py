#!/usr/bin/env python
# encoding: utf-8
 
import os
import argparse
import logging
 
 
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
parser.add_argument("--input", default="", type=str, help='input file')
args = parser.parse_args()
 
 
def main():
	f=open(os.path.join(args.input,"input.txt","r")
	s=f.read()
	linecount=len(s.split("\n")
	wordcount=len(s.split())
	charactercount=os.path.getsize(os.path.join(args.input,"input.txt","r")
	wordfreq={}
	for word in s.split()
		if word in wordfreq
			wordfreq[word]+=1
		else
			wordfreq=1
	sorted(wordfreq.items(),key=lambda x,y: cmp(x[1],y[1]),reverse = True)
	nums=5
	if wordcount<5
		nums=wordcount
	for i in range(nums)
		print (wordfreq[i])
    exit(0)
 
 
if __name__ == '__main__':
    main()
