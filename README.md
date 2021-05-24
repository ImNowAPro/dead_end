![DEAD END](https://i.imgur.com/9bluzqS.jpg)

## How to use

Just download the source and run `py bruter.py`. The program will now download a list of mirai botnet hosts from URLhaus
and try to log in to mysql with the specified credentials in `combo.txt` (feel free to edit it). If there was any
success, the program will write a `log.txt` where you can find the host with the used username and password.\
This means you know the IP of a mirai botnet, you can now try to log in to mysql with a client of your choice and run
these commands:

```sql
SHOW DATABASES;
USE BOTNETDB; --It should be pretty obvious which is the botnet database
```

From there you can list all username and passwords which are stored in _plaintext_, or inject your own login with admin
permissions:

```sql
SELECT * FROM users;
INSERT INTO users VALUES (NULL, 'username', 'password', 0, 0, 0, 0, -1, 1, 30, '');
```

Once you have done this, do a simple TCP portscan to find the mirai port, connect with Telnet, and login with your
username and password.

## How and why does this work?

There are some tutorials on YouTube where people show how to create a mirai botnet. Some very intelligent people just
use the default login `root:root` like in the video.\
So, the program basically just goes through the reported malware list of [URLHaus](https://urlhaus.abuse.ch)
and filters the tag "mirai". Then it tries to brute the mysql-server of the filtered hosts with some default logins.

## What should I do if I find such a botnet?

**Delete it.**
This kind of people aren't able to change a password, so they definitely shouldn't have botnet.
\
\
\
Let me know if there is any similar site like URLhaus where I can find some mirai botnets!\
Also feel free to create a pull request if you have any improvements!
