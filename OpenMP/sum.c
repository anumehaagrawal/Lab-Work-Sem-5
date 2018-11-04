#include <omp.h>
#include <stdio.h>
int main(){
	int a[100];
	for(int i=0;i<100;i++){
		a[i]=i/2;
	}
	int sum =0;
	int t1 = omp_get_wtime();
	#pragma omp parallel shared(a)
	{
		#pragma omp for reduction(+:sum)
		
			for(int i=0;i<100;i++){
				sum=sum+a[i];
			}
		
	}
	printf("%d\n", sum );
	int t2 = omp_get_wtime();
	printf("%d\n",t2-t1 );
}