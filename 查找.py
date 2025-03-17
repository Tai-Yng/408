顺序查找
typedef struct{
    ElemType *elem;
    int TableLen;
} SSTable;


int Search_Seq(SSTable ST,ElemType key){
    int i;
    for(i=0;i<ST.Tablen && ST.elem[i]!=key;i++);
    return i>=ST.TableLen?-1:i;
}

哨兵
int Search_Seq(SSTable ST,ElemType key){
    int i;
    ST.elem[0]=key;
    for(i=ST.TableLen;ST.elem[i]!=key;i--);
    return i;
}

int Binary_Search(SSTable ST,ElemType key){
    int low=0,high=ST.TableLen-1,mid;
    while(low<=high){
        mid=(low+high)/2;
        if(ST.elem[mid]==key)
            return mid;
        else if(ST.elem[mid]>key)
            high=mid-1;
        else
            low=mid+1;
    }
    return -1;
}

索引表
typedef struct{
    ElemType maxValue;
    int low,high;
}Index
ElemType List[100];

二叉排序树
typedef struct BSTNode{
    int key;
    struct BSTNode *lchild,*rchild;
}BSTNode,*BSTree;

BSTNode *BST_Search(BSTree T,int key){
    while(T!=NULL&&key!=T->key){
        if(key<T->key)
            T=T->lchild;
        else
            T=T->rchild;
    }
    return T;
}
递归
BSTNode *BSTSearch(BSTree T,int key){
    if(T==NULL)
        return NULL;
    if(key==T->key)
        return T;
    else if(key<T->key)
        return BSTSearch(T->lchild,key);
    else
        return BSTSearch(T->rchild,key);
}

int BST_Insert(BSTree &T,int key){
    if(T==NULL){
        T=(BSTNode *)malloc(sizeof(BSTNode));
        T->key=key;
        T->lchild=T->rchild=NULL;
        return 1;
    }else if(key==T->key)
        return 0;
    else if(key<T->key)
        return BST_Insert(T->lchild,key);
    else
        return BST_Insert(T->rchild,key);
}

void Create_BST(BSTree &T,ElemType str[],int n){
    T=NULL;
    int i=0;
    while(i<n){
        BST_Insert(T,str[i]);
        i++;
    }
}

int BST_Delete(BSTree &T,int key){
    if(T==NULL)
        return 0;
    else{
        if(key==T->key)
            return Delete(T);
        else if(key<T->key)
            return BST_Delete(T->lchild,key);
        else
            return BST_Delete(T->rchild,key);
    }
}

平衡二叉树
typedef struct AVLNode{
    int key;
    int balance;
    struct AVLNode *lchild,*rchild;
}AVLNode,*AVLTree;

红黑树
struct RBNode{
    int key;
    int color;
    RBNode *lchild,*rchild,*parent;
};

5叉查找树
struct Node{
    ElemType keys[4];
    struct Node *child[5];
    int num;
};