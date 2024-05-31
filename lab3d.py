#!/usr/bin/env python3
# Author ID: wkao4

import subprocess
def free_space():
 p = subprocess.Popen("df -h | grep '/$' | awk '{print $4}'", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
 output,_= p.communicate()
 free_space = output.decode('utf-8').strip()

 return free_space

print(free_space())