#!/usr/bin/env python
# encoding: utf-8
 
import os
import argparse
import logging
import collections
 
 
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
 
class LRU_cache
	def _init_(self,max_capacity)
		self.max_capacity=max_capacity
		self.cache=OrderdDict()
		
	def get(self,key)
		if key not in self.cache
			logger.log(logging.WARNING,"No such key")
			return -1
		value = self.cache[key]
		self.cache.pop(key)
		self.cache[key]=value
		return value
		
	def put(self,key,value)
		if key in self.cache
			logger.log(logging.INFO,"Update value")
			self.cache.pop(key)
			self.cache[key]=value
		else
			if len(self.cache)>=self.max_capacity
				self.cache.popitem(last=False)
			logger.log(logging.INFO,"Insert value")
			self.cache[key]=value

 
if __name__ == '__main__':
