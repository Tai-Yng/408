#define MaxSize 50
typedef struct {
    ElemType data[MaxSize];
    int top;
} SqStack;

void InitStack(SqStack &S){
    S.top = -1;
}

bool Push(SqStack &S, ElemType x){
    if(S.top == MaxSize - 1) return false;
    S.data[++S.top] = x;//top先加1，再入栈
    return true;
}

bool Pop(SqStack &S, ElemType &x){
    if(S.top == -1) return false;
    x = S.data[S.top--];//先出栈，top再减1
    return true;
}

bool GetTop(SqStack S, ElemType &x){
    if(S.top == -1) return false;
    x = S.data[S.top];
    return true;
}
//top指针初始为0时相反
判空?
if(S.top == -1) return false;
判满?
if(S.top == MaxSize - 1) return false;
void test(){
    SqStack S;
    InitStack(S);
    Push(S, 3);
    Push(S, 5);
    Push(S, 7);
    int x;
    Pop(S, x);
    GetTop(S, x);
}

共享栈
#define MaxSize 50
typedef struct {
    ElemType data[MaxSize];
    int top1, top2;
} SqDoubleStack;

void InitStack(SqDoubleStack &S){
    S.top1 = -1;
    S.top2 = MaxSize;
}

bool Push(SqDoubleStack &S, ElemType x, int i){
    if(S.top1 + 1 == S.top2) return false;
    if(i == 1) S.data[++S.top1] = x;
    else if(i == 2) S.data[--S.top2] = x;
    return true;
}

链栈
typedef struct Linknode{
    ElemType data;
    struct Linknode *next;
} *LiStack;

void InitStack(LiStack &S){
    S = (Linknode *)malloc(sizeof(Linknode));
    S -> next = NULL;
}

bool StackEmpty(LiStack S){
    return S -> next == NULL;
}

bool Push(LiStack &S, ElemType x){
    Linknode *p = (Linknode *)malloc(sizeof(Linknode));
    p -> data = x;
    p -> next = S -> next;
    S -> next = p;
    return true;
}

bool Pop(LiStack &S, ElemType &x){
    if(S -> next == NULL) return false;
    Linknode *p = S -> next;
    x = p -> data;
    S -> next = p -> next;
    free(p);
    return true;
}

bool GetTop(LiStack S, ElemType &x){
    if(S -> next == NULL) return false;
    x = S -> next -> data;
    return true;
}

判空?
S -> next == NULL

