#include<iostream>
#include<string>
using namespace std;
int main() {
string s;
int countt=0;
int fin=0;
cin>>s;
for(int i=0;i<s.size();i++){
    for(int j=i+1;j<s.size();j++){
        if(s[i]!='0'){
            if(s[i]==s[j]){
                countt+=1;
                s[j]='0';
            }
        }
    }
}
fin= s.size()-countt;
if(fin%2==0){
    cout<<"CHAT WITH HER!";
}else{
cout<<"IGNORE HIM!";
}
return 0;
}
