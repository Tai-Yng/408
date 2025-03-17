#define MaxSize 10
typedef struct {
    ElemType data[MaxSize];
    int length;
} SqList;

void InitList(SqList &L){
    for(int i = 0; i < MaxSize; i++){
        L.data[i] = 0;
    }
    L.length = 0;
}

bool ListInsert(SqList &L, int i, ElemType e){
    if(i < 1 || i > MaxSize) return false;
    if(L.length >= MaxSize) return false;
    for(int j = L.length; j >= i; j--){
        L.data[j] = L.data[j - 1];
    }
    L.data[i - 1] = e;
    L.length++;
    return true;
}

bool ListDesert(SqList &L, int i, ElemType &e){
    if(i < 1 || i > L.length) return false;
    e = L.data[i - 1];
    for(int j = i; j < L.length; j++){
        L.data[j - 1] = L.data[j];
    }
    L.length--;
    return true;
}

ElemType GetElem(SqList L, int i){
    return L.data[i - 1];
}


//动态分布
#define MaxSize 10
typedef struct {
    ElemType *data;
    int length, MaxSize;
} SeqList;

void InitList(SeqList &L){
    L.data = (ElemType *)malloc(MaxSize * sizeof(ElemType));//!!!!!
    L.length = 0;
    L.MaxSize = MaxSize;
}

void IncreaseSize(SeqList &L, int len){
    ElemType *p = L.data;
    L.data = (ElemType *)malloc((L.MaxSize + len) * sizeof(ElemType));
    for(int i = 0; i < L.length; i++){
        L.data[i] = p[i];
    }
    L.MaxSize += len;
    free(p);
}

ElemType GetElem(SeqList L, int i){
    return L.data[i - 1];
}//一样

int LocateElem(SeqList L, ElemType e){
    for(int i = 0; i < L.length; i++){
        if(L.data[i] == e) return i + 1;
    }
    return 0;
}

顺序表的特点：
①随机访问，即可以在O(1)时间内找到第i个元素。
②存储密度高，每个节点只存储数据元素
③拓展容量不方便（即便采用动态分配的方式实现，拓展长度的时间复杂度也比较高）
④插入、删除操作不方便,需要移动大量元素

