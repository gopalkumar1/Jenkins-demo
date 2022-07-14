FROM gopalkumar/e2b:1.0
USER ubuntu
WORKDIR /home/ubuntu
ENV PATH="/home/ubuntu/anaconda3/bin:${PATH}"
ADD . /home/ubuntu/hello.py
CMD python /home/ubuntu/hello.py
