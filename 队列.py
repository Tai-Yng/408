#define MaxSize 50
typedef struct {
    ElemType data[MaxSize];
    int front, rear;
} SqQueue

bool InitQueue(SqQueue &Q){
    Q.front = Q.rear = 0;
}

bool QueueEmpty(SqQueue Q){
    return Q.front == Q.rear;
}
!普通队列
bool EnQueue(SqQueue &Q, ElemType x){
    if(Q.rear == MaxSize - 1) return false;
    Q.data[Q.rear] = x;
    Q.rear++;
    return true;
}

bool DeQueue(SqQueue &Q, ElemType &x){
    if(Q.front == Q.rear) return false;
    x = Q.data[Q.front];
    Q.front++;
    return true;
}

!循环队列
bool EnQueue(SqQueue &Q, ElemType x){
    if((Q.rear + 1) % MaxSize == Q.front) return false;
    Q.data[Q.rear] = x;
    Q.rear = (Q.rear + 1) % MaxSize;
    return true;
}

bool DeQueue(SqQueue &Q, ElemType &x){
    if(Q.front == Q.rear) return false;
    x = Q.data[Q.front];
    Q.front = (Q.front + 1) % MaxSize;
    return true;
}

bool GetHead(SqQueue Q, ElemType &x){
    if(Q.front == Q.rear) return false;
    x = Q.data[Q.front];
    return true;
}

!!第二种方案
#define MaxSize 50
typedef struct {
    ElemType data[MaxSize];
    int front, rear;
    int size;  //size==0表示队空，size==MaxSize表示队满
} SqQueue

!!第三种方案
#define MaxSize 50
typedef struct {
    ElemType data[MaxSize];
    int front, rear;
    int tag;  //tag==1表示队满，tag==0表示队空
} SqQueue

!链式队列
#define MaxSize 50
typedef struct LinkNode{
    ElemType data;
    struct QNode *next;
} LinkNode;

typedef struct{
    LinkNode *front, *rear;
} LinkQueue;

!!带头结点
void InitQueue(LinkQueue &Q){
    Q.front = Q.rear = (LinkNode *)malloc(sizeof(LinkNode));
    Q.front -> next = NULL;
}

bool IsEmpty(LinkQueue Q){
    return Q.front == Q.rear;
}

void EnQueue(LinkQueue &Q, ElemType x){
    LinkNode *s = (LinkNode *)malloc(sizeof(LinkNode));
    s -> data = x;
    s -> next = NULL;
    Q.rear -> next = s;
    Q.rear = s;
}

bool DeQueue(LinkQueue &Q, ElemType &x){
    if(Q.front == Q.rear) return false;
    LinkNode *p = Q.front -> next;
    x = p -> data;
    Q.front -> next = p -> next;
    if(Q.rear == p) Q.rear = Q.front;
    free(p);
    return true;
}

!!不带头结点
void InitQueue(LinkQueue &Q){
    Q.front = Q.rear = NULL;
}

bool IsEmpty(LinkQueue Q){
    return Q.front == NULL;
}

void EnQueue(LinkQueue &Q, ElemType x){
    LinkNode *s = (LinkNode *)malloc(sizeof(LinkNode));
    s -> data = x;
    s -> next = NULL;
    if(Q.front == NULL) Q.front = Q.rear = s;
    else{
        Q.rear -> next = s;
        Q.rear = s;
    }
}

bool DeQueue(LinkQueue &Q, ElemType &x){
    if(Q.front == NULL) return false;
    LinkNode *p = Q.front;
    x = p -> data;
    Q.front = p -> next;
    if(Q.rear == p){
        Q.rear = NULL;
        Q.front = NULL;
    }
    free(p);
    return true;
}

!双端队列
