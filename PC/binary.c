#include <omp.h>
#include <stdio.h>
int main(){
    int num = -1;
    int n=100;
    int a[n];
    for(int i=0;i<n;i++){
        a[i]= i;
    }
    int nu;
    int index = 0;
    int endindex = n-1;
    int flag =0;
    #pragma omp parallel for schedule(dynamic,10) shared(index,endindex,num)
        
        for(int i=0;i<n ;i++){
            if(flag == 1)
                continue;
            int mid = (index+endindex)/2;
            if(a[mid]==num){
                flag =1;
                
            }
            else if(a[mid] > num){
                endindex = mid-1;
            }
            else{
                index=mid+1;
            }
        }
    
    printf("%d\n",flag);
}
