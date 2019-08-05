#!/usr/bin/env python
# encoding: utf-8

import subprocess

def process_info(nums):
    results=subprocess.Popen("ps aux", stdout=subprocess.PIPE, shell=True).communicate()
    results=str(results[0],encoding='utf-8').split("\n")
    sort_list=list()
    for i in range(1,-1)
        line_array = results[i].split()
        user = line_array[0]
        pid = line_array[1]
        time = line_array[9]
        command = line_array[10]
        time_val = int(time.split(':')[0]) * 60 + int(time.split(':')[1])
        sort_list.append((time, pid, user, command, time_val))

    sort_list.sort(key=lambda x: x[4], reverse=True)
    num = nums if nums < len(sort_list) else len(sort_list)
    for i in range(num):
        print(sort_list[i][0], '\t', sort_list[i][1], '\t', sort_list[i][2], '\t', sort_list[i][3], end='\n')




def main():
    process_info(5)
    exit(0)


if __name__ == '__main__':
    main()