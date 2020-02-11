FROM senhuang/fncs_gridlabd

# update


# ============================ Install OpenGym ==========================
### Install OpenAI gym with libav-tools for visualization purposes
RUN apt update && \
	apt install -y ffmpeg 
RUN apt-get update && \
    apt-get install -y python-opengl

RUN pip install --upgrade pip &&\
	pip install gym && \
	pip install pyglet 