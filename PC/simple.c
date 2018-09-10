#include <stdio.h>
#include <omp.h>
void main(){
	int tid,nthread;
	#pragma omp parallel private(tid)
	{
		tid=omp_get_thread_num();
		printf("Hello from %d", tid);
		if(tid==0){
			nthread= omp_get_num_threads();
			printf("Numm %d\n", nthread);
		}

	}


}