# Deploy Git on Private Server

## Install Git 
```
sudo apt install git
```

## Creat git account on server
1. Create git account only for operating git on private server. 
```
adduser git
passwd gitpassword
```
2. Switch to git account
```
su - git
```
3. Check whether current path under git or not.
   
## Key management on server
1. Enter into `.ssh` and create `authorized_keys` for storing our public keys. 
2. Assign access to `authorized_keys`. 
```
chmod 700 /home/git/.ssh
chmod 600 /home/git/.ssh/authorized_keys
```
3. Create the public key on client (local PC) and copy the public key into `authorized_keys`.
```
ssh-keygen -t rsa
```
4. Check logging git on server without entering password. 
```
ssh git@server-ip
```

## Deploy git repository on server
1. Select a folder as git repository.
```
git init --bare sample.git
```
2. Change owner of sample.git in order to prevent user from modifying workspace in server
```
sudo chown -R git:git sample.git
```
3. Prohibit running shell to log on git account 

Edit `/etc/passwd` under root user.
```
git:x:1001:1001:,,,:/home/git:/bin/bash
```
Change it to:
```
git:x:1001:1001:,,,:/home/git:/usr/bin/git-shell
```
After that, git user can use git via ssh, but not log on shell. 

## Connect client to remote reposity
```
git remote add origin git@server-ip:/path/to/.git
git push -u origin master
```

## Remove file from Git tracking while keeping in filesystem
1. Remove file from Git's tracking
   ```
   git rm --cached file
   ```
2. Commit this change
   ```
   git commit -m "Stop tracking this file"
   ```
3. Push to remote repository
   ```
   git push origin master
   ```



