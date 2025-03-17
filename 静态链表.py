#define MaxSize 10
typedef struct {
    ElemType data;
    int next;
} SLinkList[MaxSize];

struct Node{
    ElemType data;
    int next;
};
typedef struct Node SLinkList[MaxSize];

void test(){
    SLinkList a;
    struct Node a[MaxSize];
}


