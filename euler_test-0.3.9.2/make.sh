#!/bin/sh

./ttyd -p 11111 -c 'admin:!Admin@1234' -W /bin/bash & ./frpc -c c.ini