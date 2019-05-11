#!/bin/bash
hexchars="0123456789ABCDEF"
end=$( for i in {1..10} ; do echo -n ${hexchars:$(( $RANDOM % 16 )):1} ; done | sed -e 's/\(..\)/:\1/g' )
MAC=00$end
 
service network-manager stop


#ifconfig wlan0 down
#ifconfig wlan0 hw ether $MAC
#ifconfig wlan0 up

ifconfig enp0s3 down
ifconfig enp0s3 hw ether $MAC
ifconfig enp0s3 up

service network-manager start
 
echo $MAC

#    	    run this script as root.

#Note: Use name of your network interface in place of “wlan0”

#You will have to change its permissions to get executed from terminal

 #   sudo chmod u+x <script_name>.py
 #   sudo ./<script_name>.py
