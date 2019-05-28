'''
Author: Arjun Bhardwaj
Purpose:
	- This is a simple program that explains the basic working of the Paramiko module in python and how it can be used to establish a remote SSH connection.
 	
NOTE: The author does not bear any malicious intent and is not reponsible if used/modified by anyone for the same. These scripts are only for educational purpose.
'''

import paramiko
import getpass
import sys

def sshConnect(host, portnumber, user, passwd):
	try:
		ssh = paramiko.SSHClient()
		print("[*] Connecting to HOST: %s"%host)
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=host,port=portnumber.strip(),username=user.strip(),password=passwd.strip(),look_for_keys=False, allow_agent=False)
		print("[+] SUCCESS : Connection established to HOST: %s \n"%host)
	except Exception as e:
		print('\n[-] Connection Failed: %s Retry\n'%e)
		main()
	return ssh

def sshCommand(ssh):
	if not ssh:
		print("[*] oops, something went wrong with the connection, Returning to main menu to re-connect\n")
		main()
	else:
		print("[*] Enter 'terminate' to exit the command execution prompt and terminate the session.")
		try:
			while True:
				command = input("\nCommand >> ")
				if 'terminate' in command:
					print("\n[-] Prompt Ended > TERMINATING SESSION !")
					ssh.close()
					break
				stdin, stdout, stderr = ssh.exec_command(command)
				print(stdout.readline())
			return
		except:	
			print("[-] ERROR : Execution Unavailable")
	
def main():
	host = sys.argv[1]  # Stores the IP Address from command line
	port = sys.argv[2]	# Stores the Port Number from command line
	print("\n[+] Initiating console access to '%s'"%host)
	userID = getpass.getpass("\n[*] Enter User ID: ")
	psswd = getpass.getpass("[*] Enter Password: ")
	conObj = sshConnect(host, port, userID, psswd)
	optionAnswerYes = ['y','Y','yes','Yes']
	optionAnswerNo = ['n','N','no','No']
	choice = input("Want to send in commands ? ")
	if choice not in optionAnswerYes:
		print("\nTERMINATING SESSION !")
		conObj.close()
	else:
		print("\n[+] Command execution enabled")
		sshCommand(conObj)

if __name__=='__main__':
	main()