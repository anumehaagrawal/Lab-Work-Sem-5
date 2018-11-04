#include <stdio.h>
#include <omp.h>

int main(){
	int n = 100;
	double a[n][n],result[n][n];
	for(int i=0;i<n;i++){
		for(int j=0;j<n;j++){
			a[i][j] = 1;
			result[i][j] = 0;
		}
	}
	int t1 = omp_get_wtime();
	#pragma omp parallel
	{
		#pragma omp for collapse(3) 
		
			for(int i=0;i<n;i++){
				for(int j=0;j<n;j++){
					for(int k=0;k<n;k++){
						result[i][j]+=a[i][k]*a[k][j];
					}
				}
			}
		
	}
	int t2 = omp_get_wtime();
	printf("%d\n",t2-t1 );
	
}