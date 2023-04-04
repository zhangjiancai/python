#!/bin/bash -  注意：
#如果你在运行 shell 脚本时出现了权限不足的问题，可能是因为该脚本没有执行权限。可以通过以下命令为脚本添加可执行权限：
#chmod +x your_script.sh
#其中 your_script.sh 是你要执行的脚本文件名。执行上述命令后，你应该就可以通过以下方式运行该脚本了：
#./your_script.sh
 #===============================================================================
 #
 #          FILE: hostupdate
 # 
 #         USAGE: ./hostupdate 
 # 
 #   DESCRIPTION: 实时更新自己电脑上的hosts，加速网络的访问。
 # 
 #       OPTIONS: ---
 #  REQUIREMENTS: ---
 #          BUGS: ---
 #         NOTES: ---
 #        AUTHOR: linkscue(scue), 
 #  ORGANIZATION: 
 #       CREATED: 2013年08月10日 22时58分48秒 HKT
 #      REVISION:  ---
 #===============================================================================
 
 rm -f /tmp/host_new*
 host_new=/tmp/host_new$$
 host_new_from_online=/tmp/host_new_from_online$$

 curl -o /tmp/host_new_from_online https://gitee.com/fliu2476/github-hosts/raw/main/hosts

 # 1. 获取旧hosts文件来源
 if [[ -f "$1" ]]; then
     ref_host="$1"                               # 参考的host来源，建议smarthosts
 else
     ref_host=/tmp/host_new_from_online                       # 默认从/etc/hosts上获取链接参考
 fi
 
 touch $host_new && tail -f $host_new &
 
 # 2. 更新hosts
 echo -e "\e[0;35m --> 开始更新hosts文件\e[0m" # purple
 cat $ref_host | while read line; do
     if [[ ${line:0:1} == '#' ]] || [[ ${#line} == 0 ]] \
         || [[ $(echo $line | grep localhost) != "" ]] \
         || [[ $(echo $line | grep $HOSTNAME) != "" ]]; then
         echo $line >> $host_new
     else
         addr=$(echo $line|awk '{print $2}')
         link=$(nslookup "$addr" | sed '/^$/d' | sed -n '$p' | sed -n 's/Address: //gp')
         if [[ "$link" != "" ]]; then
             printf "%-19s%s\n" $link $addr >> $host_new
         fi
     fi
 done
 
 # 3. 复制至 /etc/hosts
 echo -en "\e[0;35m --> 更新hosts文件完毕，是否将新文件 $host_new 移动至 /etc/hosts[Y/n]:\e[0m" # purple
 read -p "" reply
 if [[ ${reply} != "n" ]]; then
     sudo mv /etc/hosts{,.bak}
     sudo cp $host_new /etc/hosts
 fi
 echo -e "\e[0;36m --> 全部操作完成，Enjoy!\e[0m" # cyan

