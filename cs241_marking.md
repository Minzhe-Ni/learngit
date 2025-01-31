# CS241 Coursework Marking Criterion

## Preliminary
1. **Create VM and log into the VM**
   
    ```
    /courses/cs241/coursework-multi-test2021 &

    ssh -p 3231 root@localhost
    ```
2. **Mount the directory**
   
    ```
    sshfs u5565481@remote-81.dcs.warwick.ac.uk:cs241 cs241
    ```

## Memory Leaking Test
1. Run `valgrind` (under `src` folder)
   
    ```
    valgrind --leak-check=full ../build/idsniff
    ```
2. send the packet in another terminal.
   
    ```
    wget --no-hsts www.google.co.uk 
    ```

## SYN Flooding Attack
Open loopback (`lo`) interface under `src` folder. 
```
../build/idsniff -i lo
```
1. Positive test
   
    ```
    hping3 -c 10000 -d 120 -S -w 64 -p 80 -i u100 --rand-source localhost
    ```
    
2. Flase positive test
   
    ```
    hping3 -c 10000 -d 120 -S -w 64 -p 80 -i u100 localhost
    ```
    ```
    hping3 -c 10000 -d 120 -S -A -w 64 -p 80 -i u100 --rand-source localhost
    ```

## ARP Cache Poisoning
Run `arp-poison.py`. 
```
python3 arp-poison.py
```

## Blacklisted URLs
1. Open the sniffer code on the `eth0` interface.
    ```
    ../build/idsniff -i eth0
    ```
    Run the following commands in another terminal.
    ```
    wget --no-hsts www.google.co.uk 
    ```
    ```
    wget --no-hsts www.bbc.co.uk 
    ```

2. False positive test of blacklisted URLs. \
   Open the sniffer code on the `lo` interface.
   ```
   ../build/idsniff -i lo
   ```
   Run the following command. 
   ```
   hping3 -c 10 -d 32 -S -w 64 -p 80 -i u100 --rand-source localhost -E file.txt 
   ```
   Only 10 SYN packets can be detected (no blacklisted URLs).








