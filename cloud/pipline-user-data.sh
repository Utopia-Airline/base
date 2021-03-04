#!/bin/sh
yum update -y

# Install Jenkins and Java 8
wget -O /etc/yum.repos.d/jenkins.repo \
    https://pkg.jenkins.io/redhat-stable/jenkins.repo
rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key
yum upgrade -y
yum install jenkins java-1.8.0-openjdk-devel -y
systemctl daemon-reload
# Install Git
yum install git -y
# Install Docker
yum install docker -y
service docker start
usermod -aG docker ec2-user
usermod -a -G docker jenkins
yum update -y

# Add Jenkins and Docker to startup
chkconfig jenkins on
chkconfig docker on
chkconfig --list
# Start Jenkins and Docker as a service
service jenkins start
service docker start
# sudo -su jenkins
# aws configure