# SSH via python using Paramiko
The source code explains the basic working of the "Paramiko" python module

To run this make sure you install the module:
```
pip install paramiko
```

If you see crypto graphy warnings then are thrown from paramiko, likely becaue they need to update their code to use more up-to-date parameters. The code should still run though. To avoid the warning you can try the following version of cryptography:
```
pip install cryptography==2.4.2
```
