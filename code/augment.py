#!/usr/bin/env python
# -*- coding: utf-8 -*-

#运行前安装依赖
#pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
#提前下载并移动文件至:/home/wanghao/anaconda3/lib/python3.6/site-packages/synonyms/data/words.vector.gz
#确保转换的文档的编码 保存成txt,不能是unicode.
#conda activate base  #我不小心给装到了base里面.以后要新建一个环境 安装requirement
#bash 调用命令
#python code/augment.py --input=xqb_die_merge_1000to100_for_augument.txt --output=train_augmented_numaug4_alpha005.txt --num_aug=2 --alpha=0.05

#num_aug参数：每一条语料将增强的个数
#alpha参数：每一条语料中改动的词所占的比例

from eda import *

#从bash读入参数
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True, type=str, help="原始数据的输入文件目录")
ap.add_argument("--output", required=False, type=str, help="增强数据后的输出文件目录")
ap.add_argument("--num_aug", required=False, type=int, help="每条原始语句增强的语句数")
ap.add_argument("--alpha", required=False, type=float, help="每条语句中将会被改变的单词数占比")
args = ap.parse_args()

#输出文件
output = None
if args.output:
    output = args.output
else:
    from os.path import dirname, basename, join
    output = join(dirname(args.input), 'eda_' + basename(args.input))

#每条原始语句增强的语句数
num_aug = 9 #default
if args.num_aug:
    num_aug = args.num_aug

#每条语句中将会被改变的单词数占比
alpha = 0.1 #default
if args.alpha:
    alpha = args.alpha

def gen_eda(train_orig, output_file, alpha, num_aug=9):

    writer = open(output_file, 'w')
    lines = open(train_orig, 'r').readlines()

    print("正在使用EDA生成增强语句...")
    for i, line in enumerate(lines): # enumerate() (枚举) .函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
        parts = line[:-1].split('\t')    #使用[:-1]是把\n去掉了
        label = parts[0]
        sentence = parts[1]
        aug_sentences = eda(sentence, alpha_sr=alpha, alpha_ri=alpha, alpha_rs=alpha, p_rd=alpha, num_aug=num_aug) #增强后生成的好几句
        for aug_sentence in aug_sentences:
            #原始生成的语句有空格,下面的代码去除空格
            aug_sentence.replace(" ", "")
            writer.write(label + "\t" + aug_sentence + '\n')


    writer.close()
    print("已生成增强语句!")
    print(output_file)

if __name__ == "__main__":
    gen_eda(args.input, output, alpha=alpha, num_aug=num_aug)
