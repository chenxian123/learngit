#!/bin/bath
#2018/3/29
PATH=/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin:~/bin
export PATH

#huoquyonghushurudeshenririqi
read -p "input borthday(yymmdd > 20180101):" bdate

#panduangeshi
if [ "${bdate}" = "" ];then
	echo "pleas input date!!!";exit 0
fi

echo ${bdate}

bhdate=$(date --date="${bddate}" +%s)

echo ${bhdate} 
#huoqi date zhi
dates=$(date +%s)
xdate=$((${dates}-${bhdate}))

echo "dates=${dates} xdate=${xdate}"
#jisuanshenriqi`
if [ ${xdate} lt "0" ]
