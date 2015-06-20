# (c) anupamkumar08---->https://github.com/anupamkumar08
# easy to implement and can be automated easily
#Notifies as soon as the battery is fully charged or is receding below 10% by an alarm and notification
# Here is the small code


import subprocess
import os
import time
#x=os.system("acpi")
import subprocess
v=1
while v==1:
	test = subprocess.Popen(["acpi"], stdout=subprocess.PIPE)
	output = test.communicate()[0]
	file=open('battery.txt','w+')
	file.write(str(output))
	file.close()
	with open('battery.txt','r')as f:
		for line in f:
	    		word=line.split(" ")[3]
	#r=int(f)
	#print f
	print word
        if word[2] == '%':
		t=[word[0],word[1]]
	else:
		t=[word[0],word[1],word[2]]
	h="".join(t)
	print h
	file.close()
	i=int(h)
	if i<=10:
		os.system("notify-send 'very less battery left'")
		print "\a\a\a"
	elif i==100:
		os.system("notify-send battery full")
		print "\a"
	else:
		os.system("notify-send charging")
	open('battery.txt','w').close()
	time.sleep(600)
