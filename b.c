#include <stdio.h>
#include <stdlib.h>
 int main
 {
    int n,i,j;
    printf("Enter the number: \n");
    scanf("%d",&n);
    for(i=1;i<=n;i=i+2)
    {
        for(j=i+1;j>=i;j--)
        {
            printf("%d ",j)
        }
    }
    return 0;
 }