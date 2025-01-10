# Deploy RustDesk in remote server

## Install docker
1. Install docker in remote server system. 
2. Open relative ports: TCP 21115-21119, UDP 21116.

## Create docker-compose.yml
1. Create a folder, named `rustdesk`. 
2. Edit `docker-compose.yml` like the following content.
```
version: '3'

networks:
  rustdesk-net:
    external: false

services:
  hbbs: # RustDesk ID/Rendezvous 服务器
    container_name: hbbs
    ports:
      - 21115:21115           # TCP for NAT type test
      - 21116:21116           # TCP 
      - 21116:21116/udp       # UDP / ID server
      - 21118:21118           # If run web client，use TCP to web socket
    image: rustdesk/rustdesk-server:latest
    command: hbbs
    volumes:
      - /data/rustdesk/hbbs:/root
    environment:
      - "RELAY=x.x.x.x:21117"   # IP:port or domain name to run the docker image
      - "ENCRYPTED_ONLY=1"      # Enable encryption
      - "KEY=xxxxxx"            # Define key. Remove this line, key will be generated auto. 
    networks:
      - rustdesk-net
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr: # RustDesk 中继服务器
    container_name: hbbr
    ports:
      - 21117:21117           # TCP relay
      - 21119:21119           # If run web client，use TCP to web socket
    image: rustdesk/rustdesk-server:latest
    command: hbbr
    volumes:
      - /data/rustdesk/hbbr:/root
    networks:
      - rustdesk-net
    restart: unless-stopped
```

3. Start run. 
```
docker compose up -d
```
