
#include<bits/stdc++.h>
#include<omp.h>
using namespace std;

int main()
{
	int n;
	printf("Enter number of processes\n");
	cin>>n;
	queue<int> process;
	int flag=0;
	int p;
	int count =0;
	// Vector to keep track of inquire process
	vector<int> inquire;
	for (int i = 0; i < n; ++i)
	{
		inquire.push_back(0);
	}
	// Keeping track of every processes circle of votes
	vector<vector<int> > quorums;
	for(int i =0;i<n;i++){
		vector<int> temp;
		temp.push_back((i+1)%n);
		temp.push_back((i+2)%n);
		quorums.push_back(temp);
	}
	#pragma omp parallel num_threads(n) shared(process,n,flag,quorums,p,count) 
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
				printf("Asking for acknowledgement from other processes in its own quorum %d\n",p);
				flag=1;
				
			}
			vector<int>::iterator it;
  			it = find (quorums[p].begin(), quorums[p].end(), num);
			if(it!=quorums[p].end()){
				if(inquire[num] !=1 ){
					printf("Send reply to %d from %d\n",num,p);
					flag++;
					inquire[num]=1;
				}
				else{
					printf("Some other process has asked for vote from %d\n",num);
				}

				

			}
			
			if(process.front()==0){
				process.pop();
				process.pop();
			}
			
			if(process.front()==p){
				#pragma omp barrier
				{
				#pragma omp single
				{
				if(count==1){
					
					printf("Process %d has entered critical section\n",p );
					printf("acknowledgment sent to all its quorum processes\n");
					process.pop();
					inquire[p]=0;
					for(int i=0;i<quorums[p].size();i++){
						inquire[quorums[p][i]]=0;
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