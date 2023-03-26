#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>


int main()
{
        char output[30] ;
        read (0, output, 30) ;			// read data from pipe and write it to output
        printf("%s \n child, child. \n" , output) ;
        return(0) ;
}

