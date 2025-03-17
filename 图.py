邻接矩阵
#define MaxVertexNum 100
#define INFINITY 65535
typedef char VertexType;
typedef int EdgeType;
typedef struct{
    VertexType Vex[MaxVertexNum];
    EdgeType Edge[MaxVertexNum][MaxVertexNum];
    int vexnum,arcnum;
} MGraph;

邻接表
typedef struct VNode{
    VertexType data;
    struct ArcNode *first;
} VNode,AdjList[MaxVertexNum];
typedef struct{
    AdjList vertices;
    int vexnum,arcnum;
} ALGraph;
typedef struct ArcNode{
    int adjvex;
    struct ArcNode *next;
} ArcNode;

广度优先搜索
bool visited[MaxVertexNum];
void BFSTraverse(Graph G){
    for(i=0;i<G.vexnum;i++)
        visited[i]=false;
    InitQueue(Q);
    for(i=0;i<G.vexnum;i++)
        if(!visited[i])
            BFS(G,i);
}

void BFS(Graph G,int v){
    visit(v);
    visited[v]=true;
    Enqueue(v,Q);
    while(!IsEmpty(Q)){
        Dequeue(Q,v);
        for(w=FirstNeighbor(G,v);w>=0;w=NextNeighbor(G,v,w))
            if(!visited[w]){
                visit(w);
                visited[w]=true;
                Enqueue(w,Q);
            }
    }
}

void BFS_MIN_Distance(Graph G,int u){
    for(i=0;i<G.vexnum;i++){
        d[i]=INF;
        path[i]=-1;
    }
    d[u]=0;
    visited[u]=True
    Enqueue(u,Q)
    while(!IsEmpty(Q)){
        Dequeue(Q,u)
        for(w=FirstNeighbor(G,u);w>=0;w=NextNeighbor(G,u,w))
            if(!visited[w]){
                d[w]=d[u]+1
                path[w]=u
                visited[w]=True
                Enqueue(w,Q)
            }
    }
}

深度优先搜索
类似于树的先根遍历
void PreOrder(TreeNode *R){
    if(R!=NULL){
    visit(R);
    while(R还有下一个子树T)
        PreOrder(T);
    }
}
bool visited[MaxVertexNum];
void DFSTraverse(Graph G){
    for(v=0;v<G.vexnum;v++)
        visited[v]=false;
    for(v=0;v<G.vexnum;v++)
        if(!visited[v])
            DFS(G,v);
}

void DFS(Graph G,int v){
    visit(v);
    visited[v]=true;
    for(w=FirstNeighbor(G,v);w>=0;w=NextNeighbor(G,v,w))
        if(!visited[w])
            DFS(G,w);
}

拓扑排序
#define MAX_VERTEX_NUM 100
typedef struct ArcNode{
    int adjvex;
    struct ArcNode *nextarc;
} ArcNode;
typedef struct VNode{
    VertexType data;
    ArcNode *firstarc;
} VNode,AdjList[MAX_VERTEX_NUM];
typedef struct{
    AdjList vertices;
    int vexnum,arcnum;
} Graph;

bool TopologicalSort(Graph G){
    InitStack(S);
    for(i=0;i<G.vexnum;i++)
        if(indegree[i]==0)
            Push(S,i);
    int count=0;
    while(!IsEmpty(S)){
        Pop(S,i);
        print[count++]=i
        for(p=G.vertices[i].firstarc;p;p=p->nextarc){
            v=p->adjvex;
            if(!(--indegree[v]))
                Push(S,v);
        }
    }
    if(count<G.vexnum)
        return false;
    else
        return true;
}

DFS实现逆拓扑排序
void DFSTraverse(Graph G){
    for(i=0;i<G.vexnum;i++)
        visited[i]=false;
    for(i=0;i<G.vexnum;i++)
        if(!visited[i])
            DFS(G,i);
}
void DFS(Graph G,int v){
    visited[v]=true;
    for(w=FirstNeighbor(G,v);w>=0;w=NextNeighbor(G,v,w))
        if(!visited[w])
            DFS(G,w);
    print[v];
}