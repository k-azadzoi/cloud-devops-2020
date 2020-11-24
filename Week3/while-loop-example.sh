# while the `/tmp/foo` file does not exist
while [ ! -f /tmp/foo ]
	do 
		touch /tmp/foo # makes /tmp/foo on success
		sleep 1 #wait 1 sec
done