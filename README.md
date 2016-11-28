##Deploying Docker cluster with Ansible

The cluster consists of:
* Load balancer HAProxy
* 2 nodes Web server Django/Python 1.10.3
* 2 nodes (master/slave) PostgreSQL 5.3 database

The deployment was performed on local VM Linux Ubuntu 16.04 with Ansible v. 2.2.0.0 and Docker v. 1.12.1 installed. 

1: First you need to make sure that the SSH keys were created for current user (root) with the appropriate permissions.

2: In inventory file ```/etc/ansible/hosts``` was added:
```
[local]
localhost
```
3: Clone repository:
```
git clone https://github.com/flyer8/loyalty-ans.git /opt/loyalty-ans
```
The directory contains scripts of the Web application Django in ```code/```, Dockerfile-files for building appropriate images and Ansible playbook ```site.yml``` for deploying the cluster. File ```docker-compose.yml``` is not used as it was needed for testing with Docker-compose tool.
```
drwxr-xr-x  4 root root 4096 Nov 28 13:56 ./
drwxr-xr-x 13 root root 4096 Nov 28 13:56 ../
drwxr-xr-x  4 root root 4096 Nov 28 13:56 code/
-rw-r--r--  1 root root 1264 Nov 28 13:56 docker-compose.yml.bak
-rw-r--r--  1 root root  166 Nov 28 13:56 Dockerfile.django
-rw-r--r--  1 root root 2827 Nov 28 13:56 Dockerfile.pgmaster
-rw-r--r--  1 root root 1788 Nov 28 13:56 Dockerfile.pgslave
drwxr-xr-x  8 root root 4096 Nov 28 13:56 .git/
-rw-r--r--  1 root root 3649 Nov 28 13:56 site.yml
```
Note: Please specify your source IP or Subnet in ```– iptables:``` section of the ```site.yml```:
```
Iptables: Please change value of <source> to your IP or Subnet
  - iptables: chain=INPUT policy=DROP
  - iptables: chain=FORWARD policy=DROP
  - iptables: action=append chain=INPUT protocol=tcp source=192.168.0.0/24 destination_port=22 jump=ACCEPT
  - iptables: action=insert chain=FORWARD protocol=tcp source=192.168.0.0/24 jump=ACCEPT
    become: yes
  - name: Insert rule connection limit 5 for HTTP
    command: /sbin/iptables -I DOCKER -p tcp -m connlimit --connlimit-above 5 --dport 80 -d 172.20.0.6 -j DROP
```
4: Change directory ```/opt/loyalty-ans```  and execute the command:
```
ansible-playbook -i hosts site.yml
```
