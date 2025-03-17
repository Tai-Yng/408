bool InitList(LinkList &L){ //初始化一个空的单链表
    L = (LNode *)malloc(sizeof(LNode));
    if(L == NULL) return false;
    L -> next = L;//NULL->L
    return true;
}

bool InitDList(DLinklist &L){ //初始化一个空的双链表
    L = (DNode *)malloc(sizeof(DNode));
    if(L == NULL) return false;
    L -> prior = L;//NULL->L
    L -> next = L;//NULL->L
    return true;
}

bool Empty(LinkList L){ //判断单链表是否为空
    return L -> next == L;
}

bool isTail(LinkList L, LNode *p){ //判断结点p是否为尾结点
    return p -> next == L;
}

bool Empty(DLinklist L){ //判断双链表是否为空
    return L -> next == L;
}

bool isTail(DLinklist L, DNode *p){ //判断结点p是否为尾结点
    return p -> next == L;
}


