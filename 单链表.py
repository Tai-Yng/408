typedef struct LNode{
    ElemType data;
    struct LNode *next;
}LNode, *LinkList;

LNode *p=(LNode *)malloc(sizeof(LNode));!!!!

bool InitList(LinkList &L){ //初始化一个空的单链表
    L = (LNode *)malloc(sizeof(LNode));
    if(L == NULL) return false;
    L -> next = NULL;
    return true;
}

bool ListInsert(LinkList &L, int i, ElemType e){ //在第i个位置插入元素e
    if(i < 1) return false;
    LNode *p;
    int j = 0;
    p = L;
    while(p != NULL && j < i - 1){
        p = p -> next;
        j++;
    }
    if(p == NULL) return false;
    LNode *s = (LNode *)malloc(sizeof(LNode));
    s -> data = e;
    s -> next = p -> next;
    p -> next = s;
    return true;
}

bool InsertNextNode(LNode *p, ElemType e){ //后插操作：在p结点之后插入元素e
    if(p == NULL) return false;
    LNode *s = (LNode *)malloc(sizeof(LNode));
    if(s == NULL) return false;
    s -> data = e;
    s -> next = p -> next;
    p -> next = s;
    return true;
}

LinkList List_TailInsert(LinkList &L){ //正向建立单链表，尾插法
    int x;
    L = (LNode *)malloc(sizeof(LNode));
    LNode *s,*r = L;
    scanf("%d", &x);
    while(x != 9999){
        s = (LNode *)malloc(sizeof(LNode));
        s -> data = x;
        r -> next = s;
        r = s;
        scanf("%d", &x);
    }
    r -> next = NULL;
    return L;
}

LinkList List_HeadInsert(LinkList &L){ //逆向建立单链表,头插法
    LNode *s;
    int x;
    L = (LNode *)malloc(sizeof(LNode));
    L -> next = NULL;
    scanf("%d", &x);
    while(x != 9999){
        s = (LNode *)malloc(sizeof(LNode));
        s -> data = x;
        s -> next = L -> next;
        L -> next = s;
        scanf("%d", &x);
    }
    return L;
}

//给你一个 LinkList L，如何逆置!!!!
LinkList Reverse(LinkList L){
    LinkList p, q;
    p = L -> next;
    L -> next = NULL;
    while(p){
        q = p;
        p = p -> next;
        q -> next = L -> next;
        L -> next = q;
    }
    return L;
}