typedef struct DNode{
    ElemType data;
    struct DNode *prior, *next;
}

bool InitDList(DLinklist &L){ //初始化一个空的双链表
    L = (DNode *)malloc(sizeof(DNode));
    if(L == NULL) return false;
    L -> prior = NULL;
    L -> next = NULL;
    return true;
}

bool Empty(DLinklist L){ //判断双链表是否为空
    return L -> next == NULL;
}

bool InsertNextDNode(DNode *p, DNode *s){ //后插操作：在p结点之后插入结点s
    if(p == NULL || s == NULL) return false;
    s -> next = p -> next;
    if(p -> next != NULL) p -> next -> prior = s;
    s -> prior = p;
    p -> next = s;
    return true;
}

bool DeleteNextDNode(DNode *p){ //删除结点p的后继节点
    if(p == NULL) return false;
    DNode *q = p -> next;
    if(q == NULL) return false;
    p -> next = q -> next;
    if(q -> next != NULL) q -> next -> prior = p;
    free(q);
    return true;
}

void DestroyList(DLinklist &L){ //销毁双链表
    while(L -> next != NULL){
        DeleteNextDNode(L);
    }
    free(L);
    L = NULL;
}

后向遍历
void TraverseList(DLinklist L){
    DNode *p = L -> next;
    while(p != NULL){
        //对结点p的操作
        p = p -> next;
    }
}
前向遍历
void ReTraverseList(DLinklist L){
    DNode *p = L;
    while(p != L){
        //对结点p的操作
        p = p -> prior;
    }
}

# bool InsertPriorDNode(DNode *p, DNode *s){ //前插操作：在p结点之前插入结点s
#     if(p == NULL || s == NULL) return false;
#     s -> prior = p -> prior;
#     s -> next = p;
#     p -> prior -> next = s;
#     p -> prior = s;
#     return true;
# }