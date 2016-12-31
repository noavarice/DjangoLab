#base62 tools (convert number <=> string)
# v1.0/20130109
# python 2.x/3.x supported
#
#author: Ady Liu(imxylz@gmail.com)
#github: github.com/adyliu

import sys
from Lab5.settings import CREATED_URL_MAX_LENGTH

basedigits='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
BASE=len(basedigits)


def decode(s):
    ret,mult = 0,1
    for c in reversed(s):
        ret += mult*basedigits.index(c)
        mult *= BASE
    return ret

def encode(num):
    if num <0: raise Exception("positive number "+num)
    ret=''
    while num != 0:
        ret = (basedigits[num%BASE])+ret
        num = int(num/BASE)
    while len(ret) < CREATED_URL_MAX_LENGTH:
        ret = '0' + ret
    return ret
