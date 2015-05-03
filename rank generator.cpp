#include <bits/stdc++.h>
using namespace std;
const int mod = 1e9+7;
int main(void)
{
#ifndef OJ
	freopen("sample.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif
	ios::sync_with_stdio(false);
	int T = 0;
	vector < pair <string,pair <string,string > > > collector;
	vector < pair <string,pair <string,string > > >::iterator k;
	string s;
	while(getline(cin,s))
	{
		T++;
		if(T%2)
			continue;
		string name="",roll="",branch="",sgpa="",foo;
		bool ff = true;
		while(true)
		{
			cin >> foo;
			if(ff)
			{
				if(isupper(foo[0]))
				{
					name += foo + " ";
				}
				if(isdigit(foo[0]))
				{
					roll += foo;
					ff = false;
				}
			}
			else
			{
				if(!isdigit(foo[0]))
					branch += foo + " ";
				if(branch[0] == 'B' or branch[0] == 'F')
				{
					// cout<<roll<<",";
					for(int i = 0; i < 4; i++)
						cin >> foo;
					break;
				}
				if(branch[0] == 'T')
				{
					// cout<<roll<<",";
					for(int i = 0; i < 6; i++)
						cin >> foo;
					break;
				}
				if(isdigit(foo[0]))
				{
					sgpa = foo;
					if(branch == "ELECTRICAL ENGINEERING ") // change here
					{
						collector.push_back(make_pair((sgpa),make_pair(name,roll)));
					}
					break;
				}
			}
		}
		// cout << name << " " << branch << " " << roll << " " << sgpa << endl;
	}
	sort(collector.begin(),collector.end(),greater<pair <string,pair <string,string > > >());
	for(k = collector.begin(); k != collector.end(); ++k)
		cout <<k-collector.begin()+1 <<" "<< k->first <<" "<< k->second.second <<" "<< k->second.first << '\n';
	return 0;
}
