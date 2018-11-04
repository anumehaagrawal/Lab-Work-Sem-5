#include <stdio.h>
#include <omp.h>
#include <sys/time.h>
#include <stdlib.h>
int main()
{
	struct timeval TimeValue_start;
	struct timeval TimeValue_end;
	struct timezone TimeZone_start;
	struct  timezone TimeZone_end;
	long time_start,time_end;
	double time_overhead;
	double pi = 0.0;
	int n = 1000;
	double x;
	int chunk = 5;
	gettimeofday(&TimeZone_start,&TimeZone_start);
	#pragma omp parallel for schedule(dynamic,chunk) private(x) reduction(+:pi)
	
		for(int i=0;i<n;i++){
			x = (double)i/n;
			pi += 4/(1+x*x);
		}
	pi = pi/n;
	gettimeofday(&TimeValue_end,&TimeZone_end);
	time_start = TimeValue_start.tv_sec*1000000 + TimeValue_start.tv_usec;
	time_end = TimeValue_end.tv_sec*1000000 + TimeValue_end.tv_usec;
	time_overhead = (time_end-time_start)/1000000.0;
	printf("%f\n",time_overhead );
	printf("%f\n",pi );
}


