IMA_NAME = modelicagym
IMA_NAME_BASE = yangyangfu/jmodelica_py2_gym_base

COMMAND_RUN = docker run \
	  --name c1 \
	  --detach=false \
	  -e DISPLAY=${DISPLAY} \
	  -v /tmp/.X11-unix:/tmp/.X11-unix \
	  --rm \
	  -v `pwd`:/mnt/shared \
	  -i \
          -t \
	  ${IMG_NAME} /bin/bash -c

build:
	docker build --no-cache --rm -t ${IMA_NAME} .

build_base:
	docker build -f Dockerfile_base --no-cache --rm -t ${IMA_NAME_BASE} .

remove_image:
	docker rmi ${IMA_NAME}

push:
	docker push ${IMA_NAME}:latest

Run:
	${COMMAND_RUN} \
		"cd /mnt/shared && bash"