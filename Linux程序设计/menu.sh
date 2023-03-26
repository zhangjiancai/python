#2-1 menu
MYDATE=`date +%d/%m/%y`
THIS_HOST=`hostname -s`
USER=`whoami`

file_run()
{
        # 列出当前目录下的所有可执行文件
        echo "Executable files in current directory:"
        find . -maxdepth 1 -type f -executable -printf "%f\n"
}
uers()
{
echo "there are `who|wc -l` users online"
for i in  "who are\n`who|awk '{print $1}'`"
	do 
		echo -n $I
		echo -n " "
	done
}

while :
do
	tput clear
	cat <<aaa
---------------------------------------------------------------------
User:$USER		Host:$THIS_HOST			Date:$MYDATE
---------------------------------------------------------------------
		1 : List subdirectory in current directory 
		2 : List files in current directory which can run
		3 : See who is on the system
		H : Help screen
		Q : Exit Menu
--------------------------------------------------------------------
aaa
	echo -e -n "\tYour Choice [1,2,3,H,Q] >"
	read CHOICE
	case $CHOICE in
	1) ls -l|awk '/^d/ {print $8}' 
	;;
	2) file_run 
	;;
	3) uers
	;;
	H|h)
	cat <<aaa
This is the help screen,nothing here yet to help you!
aaa
;;
	Q|q) exit 0
	;;
	*) echo -e "\t\007 unkown user response"
	;;
	esac
	echo -e -n "\n\n\tHit the return key to continue"
	read DUMMY
done


