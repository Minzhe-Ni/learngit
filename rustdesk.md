# Deploy RustDesk in remote server

## Install docker
1. Install docker in remote server system. 
2. Open relative ports: TCP 21115-21119, UDP 21116.

## Create docker-compose.yml
1. Create a folder, named 'rustdesk'. 
2. Edit content in docker-compose.yml.
```
version: '3'

networks:
  rustdesk-net:
    external: false

services:
  hbbs: # RustDesk ID/Rendezvous 服务器
    container_name: hbbs
    ports:
      - 21115:21115           # 用于 NAT 类型测试的 TCP
      - 21116:21116           # TCP打孔
      - 21116:21116/udp       # UDP心跳/ID服务器
      - 21118:21118           # 如果要运行web客户端，则使用TCP进行web套接字
    image: rustdesk/rustdesk-server:latest
    command: hbbs
    volumes:
      - /data/rustdesk/hbbs:/root
    environment:
      - "RELAY=x.x.x.x:21117"   # 运行这些容器的服务器的【IP:port】或域名
      - "ENCRYPTED_ONLY=1"      # 开启加密
      - "KEY=xxxxxx"            # 自定义KEY，去掉这一行可以自动生成
    networks:
      - rustdesk-net
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr: # RustDesk 中继服务器
    container_name: hbbr
    ports:
      - 21117:21117           # TCP中继
      - 21119:21119           # 如果要运行web客户端，则使用TCP进行web套接字
    image: rustdesk/rustdesk-server:latest
    command: hbbr
    volumes:
      - /data/rustdesk/hbbr:/root
    networks:
      - rustdesk-net
    restart: unless-stopped
```

3. Start run. \
    `docker compose up -d`
