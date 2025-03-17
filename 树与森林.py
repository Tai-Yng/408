#define MAX_TREE_SIZE 100

双亲表示法
typedef struct{
    ElemType data;
    int parent;
} PTNode;
typedef struct{
    PTNode nodes[MAX_TREE_SIZE];
    int n;
} PTree;

孩子表示法
struct CTNode{
    int child;
    struct CTNode *next;
};
typedef struct{
    ElemType data;
    struct CTNode *firstchild;
} CTBox;
typedef struct{
    CTBox nodes[MAX_TREE_SIZE];
    int n,r;
} CTree;

孩子兄弟表示法
typedef struct CSNode{
    ElemType data;
    struct CSNode *firstchild,*nextsibling;
} CSNode,*CSTree;
typedef struct BiTNode{
    ElemType data;
    struct BiTNode *lchild,*rchild;
} BiTNode,*BiTree;

void PreOrder(TreeNode *T){
    if(T!=NULL){
        visit(T);
        while(T还有子树R)
            PreOrder(R)
    }
}

void PostOrder(TreeNode *T){
    if(T!=NULL){
        while(T还有子树R)
            PostOrder(R)
        visit(T);
    }
}

应用
