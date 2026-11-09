6.18.54.1-microsoft-standard-WSL2
PRETTY_NAME="Ubuntu 26.04.1 LTS"
NAME="Ubuntu"
VERSION_ID="26.04"
VERSION="26.04.1 LTS (Resolute Raccoon)"
VERSION_CODENAME=resolute
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=resolute
LOGO=ubuntu-logo
hamza
uid=1000(hamza) gid=1000(hamza) groups=1000(hamza),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),100(users)
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  0.0  0.4  24276 15492 ?        Ss   09:31   0:01 /sbin/init
root           2  0.0  0.0   3804  2508 hvc0     Sl+  09:31   0:00 /init
root           3  0.0  0.0   3664  2136 hvc0     S+   09:31   0:00 init-watcher
root           7  0.0  0.0   3804  2276 hvc0     Sl+  09:31   0:00 plan9 --control-socket 7 --log-level 4 --server-fd 8 --pipe-fd 10 --log-truncate
root          47  0.0  0.5  50680 19744 ?        S<s  09:31   0:00 /usr/lib/systemd/systemd-journald
systemd+      82  0.0  0.3  22428 14492 ?        Ss   09:31   0:00 /usr/lib/systemd/systemd-resolved
root          90  0.0  0.3  34756 12060 ?        Ss   09:31   0:02 /usr/lib/systemd/systemd-udevd
root         135  0.0  0.0   2888  2012 ?        Ss   09:31   0:00 /bin/sh /usr/lib/systemd/scripts/chronyd-starter.sh -n -F 1
root         140  0.0  0.0   4472  3148 ?        Ss   09:31   0:00 /usr/sbin/cron -f -P
message+     143  0.0  0.1   8800  5460 ?        Ss   09:31   0:00 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
root         148  0.0  0.7  44112 29868 ?        Ss   09:31   0:00 /usr/bin/python3 /usr/bin/networkd-dispatcher --run-startup-triggers
root         161  0.0  0.2  18440  9420 ?        Ss   09:31   0:00 /usr/lib/systemd/systemd-logind
syslog       169  0.0  0.1 220548  5864 ?        Ssl  09:31   0:00 /usr/sbin/rsyslogd -n -iNONE
_chrony      262  0.0  0.2  23944 11160 ?        S    09:31   0:00 /usr/sbin/chronyd -n -F 1 -x
State             Recv-Q            Send-Q                        Local Address:Port                        Peer Address:Port            Process
LISTEN            0                 4096                          127.0.0.53%lo:53                               0.0.0.0:*
LISTEN            0                 4096                             127.0.0.54:53                               0.0.0.0:*
LISTEN            0                 1000                         10.255.255.254:53                               0.0.0.0:*
 total        used        free      shared  buff/cache   available
Mem:           3.7Gi       434Mi       3.1Gi       4.1Mi       244Mi       3.2Gi
Swap:          1.0Gi          0B       1.0Gi
