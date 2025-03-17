逻辑结构：集合关系
#define SIZE 100
int UFSets[SIZE];
void Initial(int S[]){
    for(int i=0;i<SIZE;i++)
        S[i]=-1;
}

int Find(int S[],int x){
    while(S[x]>=0)
        x=S[x];
    return x;
}

void Union(int S[],int Root1,int Root2){
    if(Root1==Root2)
        return;
    S[Root2]=Root1;
}

void Union(int S[],int Root1,int Root2){
    if(Root1==Root2)
        return;
    if(S[Root1]>S[Root2]){
        S[Root2]+=S[Root1];
        S[Root1]=Root2;
    }else{
        S[Root1]+=S[Root2];
        S[Root2]=Root1;
    }
}

int Find(int S[],int x){
    int root=x;
    while(S[root]>=0)
        root=S[root];
    while(x!=root){
        int t=S[x];
        S[x]=root;
        x=t;
    }
    return root;
}
