#!/bin/bash
#2018/3/28
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#yonghushuruzhi
read -p "please input (Y/N):" yn

#panduanyonghusurushifoweikong
test -z ${yn}&&echo "please input!!!"

#shurudezhiwei Y or N tisi
[ "${yn}" == "Y" -o "${yn}" == "y" ]&&echo "OK,continue"&&exit 0
[ "${yn}" == "N" -o "${yn}" == "n" ]&&echo "oh,interrup!"&&exit 0

#panduanyonghushurudezhishifohege
echo "I don't know what your choice is"&&exit 0
