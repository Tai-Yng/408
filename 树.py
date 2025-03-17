#define MaxSize 100
顺序存储
struct TreeNode{
    ElemType value;
    bool isEmpty;
};

TreeNode t[MaxSize];

链式存储
struct ElemType{
    int value;
};

typedef struct BiTNode{
    ElemType data;
    struct BiTNode *lchild,*rchild;
} BiTNode,*BiTree;

BiTree root=NULL;

typedef struct BiTNode{
    ElemType data;
    struct BiTNode *lchild,*rchild;
    struct BiTNode *parent;
} BiTNode,*BiTree;

先序遍历
void PreOrder(BiTree T){
    if(T!=NULL){
        visit(T);
        PreOrder(T->lchild);
        PreOrder(T->rchild);
    }
}

void InOrder(BiTree T){
    if(T!=NULL){
        InOrder(T->lchild);
        visit(T);
        InOrder(T->rchild);
    }
}

void PostOrder(BiTree T){
    if(T!=NULL){
        PostOrder(T->lchild);
        PostOrder(T->rchild);
        visit(T);
    }
}

int treeDepth(BiTree T){
    if(T==NULL)
        return 0;
    int l=treeDepth(T->lchild);
    int r=treeDepth(T->rchild);
    return l>r?l+1:r+1;
}

typedef struct LinkNode{
    BiTNode *data;//存指针而不是结点
    struct LinkNode *next;
} LinkNode;

typedef struct{
    LinkNode *front,*rear;
} LinkQueue;

!层序遍历
void LevelOrder(BiTree T){
    LinkQueue Q;
    InitQueue(Q);
    BiTree p;
    EnQueue(Q,T);
    while(!QueueEmpty(Q)){
        DeQueue(Q,p);
        visit(p);
        if(p->lchild!=NULL)
            EnQueue(Q,p->lchild);
        if(p->rchild!=NULL)
            EnQueue(Q,p->rchild);
    }
}

!线索二叉树
typedef struct ThreadNode{
    ElemType data;
    struct ThreadNode *lchild,*rchild;
    int ltag,rtag;
} ThreadNode,*ThreadTree;
//tag==0指向孩子，tag==1指向前驱或后继,表示线索

找中序前驱
void visit(BiTNode *q){
    if (q==p)
        final=pre;
    else
        pre=q;
}
void InOrder(BiTree T){
    if(T!=NULL){
        InOrder(T->lchild);
        visit(T);
        InOrder(T->rchild);
    }
}
BiTNode *p;
BiTNode *pre=NULL;
BiTNode *final=NULL;

中序线索化
ThreadNode *pre=NULL;
typedef struct ThreadNode{
    ElemType data;
    struct ThreadNode *lchild,*rchild;
    int ltag,rtag;
} ThreadNode,*ThreadTree;
void CreateInThread(ThreadTree T){
    pre=NULL;
    if(T!=NULL){
        InThread(T);
        if(pre->rchild==NULL)
            pre->rtag=1;
}
void InThread(ThreadTree T){
    if(T!=NULL){
        InThread(T->lchild);
        visit(T);
        InThread(T->rchild);
    }
}
void visit(ThreadNode *q){
    if(q->lchild==NULL){
        q->lchild=pre;
        q->ltag=1;
    }
    if(pre!=NULL&&pre->rchild==NULL){
        pre->rchild=q;
        pre->rtag=1;
    }
    pre=q;
}
王道书
void InThread(ThreadTree p,ThreadTree &pre){
    if(p!=NULL){
        InThread(T->lchild);
        if(p->lchild==NULL){
            p->lchild=pre;
            p->ltag=1;
        }
        if(pre!=NULL&&pre->rchild==NULL){
            pre->rchild=p;
            pre->rtag=1;
        }
        pre=p;
        InThread(T->rchild);
    }
}
void CreateInThread(ThreadTree T){
    ThreadTree pre=NULL;
    if(T!=NULL){
        InThread(T,pre);
        pre->rchild=NULL;
        pre->rtag=1;
    }
}

先序线索化
void PreThread(ThreadTree T){
    if(T!=NULL){
        visit(T);
        if  (p->ltag==0)
            PreThread(T->lchild);
        PreThread(T->rchild);
    }
}
后序线索化
void PostThread(ThreadTree T){
    if(T!=NULL){
        PostThread(T->lchild);
        PostThread(T->rchild);
        visit(T);
    }
}

线索化找前驱后继
中序后序
ThreadNode *Firstnode(ThreadNode *p){
    while(p->ltag==0)
        p=p->lchild;
    return p;
}
ThreadNode *Nextnode(ThreadNode *p){
    if(p->rtag==0)
        return Firstnode(p->rchild);
    else
        return p->rchild;
}
void Inorder(ThreadNode *T){
    for(ThreadNode *p=Firstnode(T);p!=NULL;p=Nextnode(p))
        visit(p);
}
空间O(1)
中序前驱
ThreadNode *Lastnode(ThreadNode *p){
    while(p->rtag==0)
        p=p->rchild;
    return p;
}
ThreadNode *Prenode(ThreadNode *p){
    if(p->ltag==0)
        return Lastnode(p->lchild);
    else
        return p->lchild;
}
void RevInorder(ThreadNode *T){
    for(ThreadNode *p=Lastnode(T);p!=NULL;p=Prenode(p))
        visit(p);
}

先序后继
