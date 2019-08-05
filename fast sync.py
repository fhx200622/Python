#!/usr/bin/env python
# encoding: utf-8

import os
import argparse



parser = argparse.ArgumentParser()
parser.add_argument("--config", type=str, help='config file')
parser.add_argument("--sync", type=str, help='file to transport')
args = parser.parse_args()


def main():
    if not os.path.exists(args.config)
        print("config file does not exist")
        exit(1)
    if not os.path.exists(args.sync)
        print("sync file does not exist")
        exit(1)
    config=args.config
    sync=args.sync
    user=os.system("head -1 config | cut -f1 -d ' '")
    pas=os.system("head -1 config | cut -f2 -d ' '")
    os.system("sshpass -p scp sync" + user + ": /sync")
    length=(len(open(os.path(config,"r").read().split("\n")))+1)/2
    os.system("split -l length config config_")
    os.system("cp -f config config_aa")
    os.system("sshpass -p" + pas + "scp 07.py" + user + ":/07.py")
    os.system("sshpass -p" + pas + "scp config_ab" + user + "/config")
    os.system("sshpass -p" + pas + "ssh" + user +"python3 sh/07.py config sync")
    exit(0)


if __name__ == '__main__':
    main()