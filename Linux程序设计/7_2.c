// 8-2
#include <sys/types.h>
#include <sys/socket.h>
#include <stdio.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>

int main()
{
    int server_sockfd, client_sockfd;
    int server_len, client_len;
    struct sockaddr_in server_address;
    struct sockaddr_in client_address;
    char string[256];
    char *ans = "yes!";

/*  Create an unnamed socket for the server.  */

    server_sockfd = socket(AF_INET, SOCK_STREAM, 0);

/*  Name the socket.  */

    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = inet_addr("127.0.0.1");
    server_address.sin_port = htons(9734);
    server_len = sizeof(server_address);
    bind(server_sockfd, (struct sockaddr *)&server_address, server_len);

/*  Create a connection queue and wait for clients.  */

    listen(server_sockfd, 5);
    while(1) {
        char ch;

        printf("server waiting\n");

/*  Accept a connection.  */

        client_len = sizeof(client_address);
        client_sockfd = accept(server_sockfd, 
            (struct sockaddr *)&client_address, &client_len);

	printf("Now,client request come in.\n");
	printf("client_address = %s\tclient_port = %u\n",inet_ntoa(client_address.sin_addr),htons(client_address.sin_port));

/*  We can now read/write to client on client_sockfd.  */

        read(client_sockfd, string, sizeof(string));
	printf("client send: %s\n",string);
        write(client_sockfd, ans, strlen(ans) + 1);
        //write(client_sockfd, ans, sizeof(ans));
        //The sizeof operator returns the size of the pointer, not the size of the string it points to. In this case, ans is a pointer to a string literal with size 5 (4 characters + null terminator), but sizeof(ans) returns the size of the pointer (usually 8 bytes on 64-bit systems).To fix the warning, we can use the strlen function to get the size of the string:write(client_sockfd, ans, strlen(ans) + 1);This will send the entire string (including the null terminator) to the client.
        close(client_sockfd);
    }
    close(server_sockfd);
}


