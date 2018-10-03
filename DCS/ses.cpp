
#include <bits/stdc++.h>
using namespace std;
#include <omp.h>
#include <stdio.h>
int main(){
	int n;
	cin>>n;
	int send,rec,th_wait,th_send;
	send=-1;
	int wait;
	vector<vector<pair<int,int> > >each_vectors;
	for(int i=0;i<n;i++){
		vector<pair<int,int> > v;
		each_vectors.push_back(v);
		}
	
	#pragma omp parallel num_threads(n) shared(each_vectors) 
	{
	
		for(int i=0;i<5;i++){


			#pragma omp single 
			{


			printf("Enter the sending process number\n");
			cin>>send;
			printf("Enter the receiving process id\n");
			cin>>rec;
			}
			int th_num = omp_get_thread_num();
			if(send!= -1 && th_num==send){
				if(th_send==send){
					printf("Process %d has been sent by %d\n", wait, th_send);
					th_send= th_wait;
				}
			
				int flag=0;
				for(int i=0;i<each_vectors[send].size();i++){
					if(each_vectors[send][i].first == rec){
						flag=1;
						wait = rec;
						th_wait = send;
						th_send = each_vectors[send][i].second;
						printf("Process %d is yet to be sent by process %d\n",rec,send );
					}
				}
				if(flag==0){
					vector<pair<int,int> > v = each_vectors[send];
					pair<int,int> p;
					p.first=rec;
					p.second= send;
					v.push_back(p);
					printf("Process %d is  sent to process %d\n",send ,rec);

				}
			
			}	
	}	
	}

	
}