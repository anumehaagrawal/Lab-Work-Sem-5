#include <omp.h>
#include <stdio.h>
#include <sys/time.h>
#include <stdlib.h>
int main(){
    int n = 100;
    int num;
    int chunk = 5;
    int count =0;
    struct timeval TimeVal_start;
    struct timeval TimeVal_end;
    struct timezone TimeZone_start;
    struct timezone TimeZone_end;
    long st,et;
    double to;
    gettimeofday(&TimeVal_start,&TimeZone_start);
    #pragma omp parallel for schedule(dynamic,chunk) reduction(+:count)
    
        for(int i=1;i<n;i++){
            
                if(factors(i)==0){
                    count = count +1;
                }
            
        }
    gettimeofday(&TimeVal_end,&TimeZone_end);
    st = TimeVal_start.tv_sec*1000000 + TimeVal_start.tv_usec;
    et = TimeVal_end.tv_sec*1000000 + TimeVal_end.tv_usec;
    to = (et-st)/1000000.0;
    printf("%lf\n",to);
}

int factors(int num){
    int count =0;
    if(num/2 >1 && num%2 ==0){
        return 1;
    }
    #pragma omp parallel for schedule(dynamic,5) reduction(+:count)
    
        for(int i=2;i<num/2;i++){
            if(num%i==0){
                count=count+1;
            }
        }
    
    return count;
}

