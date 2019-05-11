    #!/usr/bin/python
    import os
    import time
    while True:
    	    os.system("service network-manager stop")
    	    
    	    #os.system("ifconfig wlan0 down")
    	    #print(os.popen("macchanger wlan0 -r").read())
    	    #os.system("ifconfig wlan0 up")
    	    
    	    os.system("ifconfig enp0s3 down")
    	    print(os.popen("ifconfig enp0s3 -r").read())
    	    os.system("ifconfig enp0s3 up")
    	    
    	    os.system("service network-manager start")
    	    time.sleep(10)
    	    
    	    
    	    
    	    
    	    
#    	    run this script as root.

#Note: Use name of your network interface in place of “wlan0”

#You will have to change its permissions to get executed from terminal

 #   sudo chmod u+x <script_name>.py
 #   sudo ./<script_name>.py
