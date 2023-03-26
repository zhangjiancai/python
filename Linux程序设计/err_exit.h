#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
int err_exit(char *s)
{
    perror(s);
    exit(1);
};
