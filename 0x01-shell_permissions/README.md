<strong>Shell Permissions<strong>
0. My name is Betty== su betty
1. Who am I == whoami
2. Groups == groups
3. New owner == sudo chown betty hello
4. Empty! == touch hello
5. Execute == chmod u+x hello
6. Multiple permissions == chmod ug+x,a+r hello
7. Everybody! == chmod uga+x hello
8. James Bond == chmod 007 hello
9. John Doe == chmod 753 hello
10. Look in the mirror == chmod --reference=olleh hello 
11. Directories == chmod a+X *
12. More directories == mkdir -m 751 dir_holberton 
13. Change group == chgrp holberton hello
14. Owner and group == chown betty:holberton *
15. Symbolic links == chown -h betty:holberton _hello
16. If only == chown --from=guillaume betty hello