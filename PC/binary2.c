#include <omp.h>
#include <stdio.h>
#include <sys/time.h>
int main(){
    int num =9;
    int n=100;
    int a[n];
    int nu;
    struct timeval
    for(int i=0;i<n;i++){
        a[i]= i;
    }
    #pragma omp parallel
    {
        #pragma omp single
        {
            nu = binary(a,0,n-1,num);
        }
    }
    if(nu == 0){
        printf("Value not found\n");
    }
    else
     printf("Value found \n",nu);
}

int binary(int a[],int low,int high,int num){
    if(high < low)
        return 0;
    int mid = (low+high)/2;
    int val;
    int val2;
    if(a[mid]== num){
        return 1;
    }
    #pragma omp task shared(val,num,mid,low)
    {
        if(a[mid]>num)
            val = binary(a,low,mid-1,num);
    }
    #pragma omp task shared(val2,num,mid,high)
    {
        if(a[mid]<num){
            val2 = binary(a,mid+1,high,num);
        }
    }
    #pragma omp taskwait
    {
        return val|val2;
    }
    
}