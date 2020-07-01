FROM centos
RUN yum install -y python3 
RUN python3 -m pip install --upgrade pip
RUN pip install numpy
RUN pip install matplotlib
RUN pip install scikit-learn
RUN pip install pandas
RUN pip install opencv-python
RUN pip install scipy
RUN pip install tensorflow
RUN pip install keras
RUN pip install pillow
