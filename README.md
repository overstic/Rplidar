# Rplidar

1.How to connect 2 machines in the ROS system:

  change files: /etc/hosts          add the IP address and hostname of another system anywher, like :"209.2.234.161	raspberrypi"
  
  change files: ~/.bashrc           add "export ROS_HOSTNAME=ubuntu   
  
  export ROS_MASTER_URI=http://209.2.234.161:11311  "    in the end of this file
                                         
  (where the ros_hostname correspond to the computer itself but master_uri correspond to the
                                         
  only IP address,ie http://209.2.234.161 is the address of raspberry pi,I want to use raspy
                                         
  as the master pc, so both raspy and another pc has to write:
                                        
  export ROS_MASTER_URI=http://209.2.234.161:11311 ,11311 is a must.

