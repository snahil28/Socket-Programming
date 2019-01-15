from socket import *
msg = 'I love computer networks'
endmsg = '\r\n.\r\n'
# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = 'smtp.nyu.edu'
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
#Fill in end
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != '220':
print('220 reply not received from server.')
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode('utf-8'))
recv1 = clientSocket.recv(1024)
print(recv1)
#Send MAIL FROM command and print server response.
print('Sending MAIL FROM Command')
clientSocket.send(b"MAIL From: singhsnahil@gmail.com\r\n")
recv2 = clientSocket.recv(1024)
#Send RCPT TO command and print server response.
print("Sending RCPT TO Command")
clientSocket.send(b"RCPT TO: ss11381@nyu.edu\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
#Send DATA command and print server response.
print("Sending DATA Command")
clientSocket.send(b"DATA\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
#Send Data and print server response.
print("Sending Data")
clientSocket.send(b"SUBJECT: SMTP Mail Client Test\n"+msg.encode('utf-8')+b"\n.\n\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
#Send QUIT and print server response.
print("Sending QUIT")
clientSocket.send(b"QUIT\r\n")
recv2 = clientSocket.recv(1024)
print(recv2)
print("Mail Sent")
