#!/usr/bin/env python
# coding=utf-8

import random
import os, sys

def randomPhoneNumber():
    result = ''
    for i in range(0, 11):
        value = random.randint(1, 9)
        result = result + str(value)
    return result

def deal(phoneNumber):
    command = './rename_phone.sh ' + phoneNumber + ' ' + randomPhoneNumber()
    print "execute command: " + command
    os.system(command)
    print "done"


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "usage: change_phone.py <origin phone number>"
    else:
        deal(sys.argv[1])