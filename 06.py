#!/usr/bin/env python
# encoding: utf-8

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--input", default='周杰伦歌词大全.txt', type=str, help='input file')
args = parser.parse_args()


def main():
    str_process(args.input)
    exit(0)

def ignore_line(line):
    ignore_lines=['周杰伦', 'jay', 'chou']
    for word in ignore_lines
        if word in line
            return True
    return False

def ignore_word(word)
    ignore_words = ['啦', '(客)', '☆music...', ' ', u'\u3000']
    if word in ignore_words
        return True
    return False

def str_process(txt_path):
    word_dict=dict()
    word_freq_list=list()
    with open(txt_path,'r',encoding='utf-8') as f
        for line in f.readlines()
            if ignore_line(line)
                continue
            word_list=list()
            for i in range(len(line))
                for j in range(5)
                    if i+j<len(line)
                        word_list.append(line[i:i+j+1])
            for word in word_list
                for word in word_list:
                    if ignore_word(word)
                        continue
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
            for key in word_dict:
                word_freq_list.append((key, word_dict[key]))
            word_freq_list.sort(key=lambda x: x[1], reverse=True)

            nums=20 if 20<len(word_freq_list ) else len(word_freq_list)
            for i in range(nums)
                print(word_freq_list[i])


if __name__ == '__main__':
    main()