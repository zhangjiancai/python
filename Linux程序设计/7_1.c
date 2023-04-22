// 8-1
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <stdlib.h>

int main()
{
    int sockfd;
    int len;
    struct sockaddr_in address;
    int result;
    char string[256];
    char rcv[256];

/*  Create a socket for the client.  */

    sockfd = socket(AF_INET, SOCK_STREAM, 0);

/*  Name the socket, as agreed with the server.  */

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = inet_addr("127.0.0.1");
    address.sin_port = htons(9734);
    len = sizeof(address);

/*  Now connect our socket to the server's socket.  */

    result = connect(sockfd, (struct sockaddr *)&address, len);

    if(result == -1) {
        perror("oops: client");
        exit(1);
    }

/*  We can now read/write via sockfd.  */
    printf("enter some message: ");fflush(stdout);
    fgets(string,sizeof(string),stdin);

    write(sockfd, string, sizeof(string));
    read(sockfd, rcv, sizeof(rcv));
    printf("from server = %s\n", rcv);
    close(sockfd);
    exit(0);
}
