
NOTES

Uses systemd / systemctl

3 services defined in /etc/systemd/system/multi-user.target.wants

lrwxrwxrwx  1 root root   36 Oct 30  2017 fermnode.service -> /lib/systemd/system/fermnode.service
lrwxrwxrwx  1 root root   41 Oct 22  2017 fermtemp-cool.service -> /lib/systemd/system/fermtemp-cool.service
lrwxrwxrwx  1 root root   41 Oct 23  2017 fermtemp-heat.service -> /lib/systemd/system/fermtemp-heat.service


ex:
systemctl start fermtemp-cool

