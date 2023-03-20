FROM quay.io/pypa/manylinux_2_28_x86_64
RUN yum -y update && yum -y groupinstall "Development Tools"
ENV ACLOCAL_PATH="/usr/share/aclocal"
RUN python3.10 -m pip install "wheel>=0.40"