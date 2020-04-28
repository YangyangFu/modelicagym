exec docker run \
 	  --name gym_test \
      --user=root \
	  --detach=false \
	  -e DISPLAY=${DISPLAY} \
	  -v /tmp/.X11-unix:/tmp/.X11-unix:rw \
	  --rm \
	  -v `pwd`:/mnt/shared \
	  -i \
      -t \
	  dadrl /bin/bash -c "cd /mnt/shared && python /mnt/shared/setup_test.py"

exec docker attach gym_test
	
exit $
  
