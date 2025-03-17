#define MAZLEN 255
typedef struct{
    char ch[MAXLEN];
    int length;
} SString;

typedef struct{
    char *ch;
    int length;
} HString;

HString S;
S.ch=(char *) malloc(MAxLEN * sizeof(char));
S.length=0;

typedef struct StringNode{
    char ch[4];
    struct StringNode *next;
} StringNode,*String;

S.ch="wangdao";
S.length=7;

bool SubString(SString &Sub,SString S,int pos,int len){
    if(pos+len-1>S.length)
        return false;
    for(int i=pos;i<pos+len;i++)
        Sub.ch[i-pos+1]=S.ch[i];
    Sub.length=len;
    return true;
}

int StrCompare(SString S,SString T){
    for(int i=1;i<=S.length&&i<=T.length;i++)
        if(S.ch[i]!=T.ch[i])
            return S.ch[i]-T.ch[i];
    return S.length-T.length;
}
//朴素模式匹配算法
int Index(SString S,SString T){
    int i=1,n=StrLength(S),m=StrLength(T);
    SString sub;
    while(i<=n-m+1){
        SubString(sub,S,i,m);
        if(StrCompare(sub,T)!=0)
            ++i;
        else
            return i;
    }
    return 0;
}
//通过数组下标实现朴素模式匹配算法
int Index(SString S,SString T){
    int i=1,j=1;
    while(i<=S.length&&j<=T.length){
        if(S.ch[i]==T.ch[j]){
            ++i;
            ++j;
        }else{
            i=i-j+2;
            j=1;
        }
    }
    if(j>T.length)
        return i-T.length;
    else
        return 0;
}
//最坏O(nm)
!KMP
int Index_KMP(SString S,SString T,int next[]){
    int i=1,j=1;
    while(i<=S.length&&j<=T.length){
        if(j==0||S.ch[i]==T.ch[j]){
            ++i;
            ++j;
        }else
            j=next[j];
    }
    if(j>T.length)
        return i-T.length;
    else
        return 0;
}
void get_next(SString T,int next[]){
    int i=1,j=0;
    next[1]=0;
    while(i<T.length){
        if(j==0||T.ch[i]==T.ch[j]){
            ++i;
            ++j;
            next[i]=j;
        }else
            j=next[j];
    }
}

int Index_KMP(SString S,SString T){
    int i=1,j=1;
    int next[T.length+1];
    get_next(T,next);
    while(i<=S.length&&j<=T.length){
        if(j==0||S.ch[i]==T.ch[j]){
            ++i;
            ++j;
        }else
            j=next[j];
    }
    if(j>T.length)
        return i-T.length;
    else
        return 0;
}
//O(n+m)

!优化nextval
nextval[1]=0
for (int j=2; j<=T.length; j++){
    if(T.ch[j]!=T.ch[next[j]])
        nextval[j]=next[j];
    else
        nextval[j]=nextval[next[j]];
    }

void get_nextval(SString T,int nextval[]){
    int i=1,j=0;
    nextval[1]=0;
    while(i<T.length){
        if(j==0||T.ch[i]==T.ch[j]){
            ++i;
            ++j;
            if(T.ch[i]!=T.ch[j])
                nextval[i]=j;
            else
                nextval[i]=nextval[j];
        }else
            j=nextval[j];
    }
}