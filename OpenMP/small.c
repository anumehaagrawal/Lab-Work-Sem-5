#include <stdio.h>
#include <omp.h>
#include <sys/time.h>
int main()
{
	struct timeval TimeValue_start;
	struct timeval TimeValue_end;
	struct timezone TimeZone_start;
	struct  timezone TimeZone_end;
	long time_start,time_end;
	double time_overhead;
	
	int n = 10000;
	int a[n];
	for(int i=0;i<n;i++){
		a[i] = n-2*i +9;
	}
	int x = a[0];
	int chunk = 5;
	gettimeofday(&TimeZone_start,&TimeZone_start);
	#pragma omp parallel for schedule(runtime,chunk) shared(x) 
	
		for(int i=0;i<n;i++){
			 if(x>a[i])
			
				x = a[i];
			
		}

	gettimeofday(&TimeValue_end,&TimeZone_end);
	time_start = TimeValue_start.tv_sec*1000000 + TimeValue_start.tv_usec;
	time_end = TimeValue_end.tv_sec*1000000 + TimeValue_end.tv_usec;
	time_overhead = (time_end-time_start)/1000000.0;
	printf("%f\n",time_overhead );
	printf("%d\n",x );
}


