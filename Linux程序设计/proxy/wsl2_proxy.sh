#!/bin/bash
host_ip=$(cat /etc/resolv.conf |grep "nameserver" |cut -f 2 -d " ") # 获取ip地址
echo $host_ip # 输出ip地址
export ALL_PROXY="http://$host_ip:15732" # 设置代理，15732为我的代理端口
curl -I https://www.google.com # 尝试访问Google, 验证代理的有效性