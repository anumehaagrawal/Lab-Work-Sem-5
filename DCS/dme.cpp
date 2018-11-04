#include<bits/stdc++.h>
#include<omp.h>
using namespace std;
int main(){
	int n;
	printf("Enter number of processes\n");
	cin>>n;
	queue<int> process;
	vector<queue<int> > v;
	for(int i=0;i<n;i++){
		queue<int> q;
		v.push_back(q);
	}
	int flag=0;
	int p;
	int count =0;
	#pragma omp parallel num_threads(n) shared(process,n,flag,v,p,count) 
	{
		for(int i=0;i<5;i++){
			
			#pragma omp single
			{
				
				flag=0;
				count=1;
				printf("Enter process number to use critical section\n");
				cin>>p;
				process.push(p);
			}
			int num = omp_get_thread_num();
			if(num==p){
				printf("Sending message to other processes from %d\n",p);
				flag=1;
				v[num].push(p);

			}
			if(num!=p){
				printf("Send reply to %d from %d\n",num,p);
				v[num].push(p);
				flag++;
				

			}
			
			if(process.front()==0){
				process.pop();
				process.pop();
			}
			printf(" Process at top of queue is %d\n",process.front() );
			if(process.front()==p){
				#pragma omp barrier
				{
				#pragma omp single
				{
				if(count==1){
					
					printf("Process %d has entered critical section\n",p );
					printf("acknowledgment sent to all other processes\n");
					process.pop();
					for(int i=0;i<n;i++){
						if(!v[i].empty())
							v[i].pop();
					}
				
				}
				}
				}
			}
			
			
		}


	}
	while(!process.empty()){
		printf("%d\n",process.front() );
		process.pop();
	}

}