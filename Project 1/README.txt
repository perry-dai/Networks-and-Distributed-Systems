For this project, my partner and I wrote it in Python. The program begins by parsing any variables inputted when run.
Then using the socket library, it opens a socket to talk to the provided host and port. When it receives a message from
the server, it splits the message and then uses the operator library to either *,/,+, - the two numbers given by the server.
After computing the solution, we send it to the server using the send function. For the extra credit, we used a simple if 
statement to check if the parameters were given for the SSL connection. If the port is given use the given port and hostname;
If s parameter is given we wrap the socket and connect using the SSL port. If nothing is given, it uses the default port. 
Some of the challenges we faced were trying to correctly use the socket library especially when using send and receive. 
We tested our code by using the print function to see if after sending to the server we were receiving the correct next step.
While this trial and error method isn't the most efficient, we fixed our errors fast enough for it to a viable way of testing. 
