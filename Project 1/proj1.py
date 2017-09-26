import socket
import argparse
import sys
import operator
import ssl

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # add optional parameters port and socket
    parser.add_argument('-p', dest='port', type=int, nargs='?')
    parser.add_argument('-s', dest='socket', action='store_true', default=False)
    # add mandatory parameters hostname and student_id
    parser.add_argument('hostname')
    parser.add_argument('student_id')
    args = parser.parse_args()
    # save input parameters into variables
    port = args.port
    sock = args.socket
    hostname = args.hostname
    student_id = args.student_id
    
    # connect to inputted hostname and port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # check to see if ssl socket was chosen
    if sock:
        s = ssl.wrap_socket(s)
    
    # check to see if port number is provided, or if ssl socket was chosen
    if port:
        s.connect((hostname, port))
    elif sock:
        s.connect((hostname, 27999))
    else:
        s.connect((hostname, 27998))

    # send hello message
    s.send('cs3700fall2017 HELLO %s\n' % student_id)
    msg = s.recv(4096)
    operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.div}

    # iterate through loop until end message received
    while ('BYE' not in msg):
        msg_array = msg.split()
        first_number = int(msg_array[2])
        second_number = int(msg_array[4])
        answer = operators[msg_array[3]](first_number, second_number)
        
        # send answer to previous math equation and receive new message
        s.send('cs3700fall2017 %i\n' % answer)
        msg = s.recv(4096)
    print msg
    # close the connection
    s.close()
