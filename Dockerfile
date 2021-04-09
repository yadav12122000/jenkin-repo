FROM centos:latest
RUN yum install httpd -y && echo hello docker123  > /var/www/html/index.html && date
WORKDIR /root
