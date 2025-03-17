void InsertSort(int A[],int n){
    int i,j;
    for(i=1;i<n;i++){
        if(A[i]<A[i-1]){
            temp=A[i];
            for(j=i-1;j>=0&&temp<A[j];--j)
                A[j+1]=A[j];
            A[j+1]=temp;
        }
    }
}

void InsertSort(int A[],int n){
    int i,j;
    for(i=2;i<=n;i++){
        if(A[i]<A[i-1]){
            A[0]=A[i];
            for(j=i-1;A[0]<A[j];--j)
                A[j+1]=A[j];
            A[j+1]=A[0];
        }
    }
}

void InsertSort(int A[],int n){
    int i,j,low,high,mid;
    for(i=2;i<=n;i++){
        A[0]=A[i];
        low=1;
        high=i-1;
        while(low<=high){
            mid=(low+high)/2;
            if(A[mid]>A[0])
                high=mid-1;
            else
                low=mid+1;
        }
        for(j=i-1;j>=high+1;--j)
            A[j+1]=A[j];
        A[high+1]=A[0];
    }
}

void ShellSort(int A[],int n){
    int d,i,j;
    for(d=n/2;d>=1;d/=2)
        for(i=d+1;i<=n;++i)
            if(A[i]<A[i-d]){
                A[0]=A[i];
                for(j=i-d;j>0&&A[0]<A[j];j-=d)
                    A[j+d]=A[j];
                A[j+d]=A[0];
            }
}

void swap(int &a,int &b){
    int temp=a;
    a=b;
    b=temp;
}

void BubbleSort(int A[],int n){
    int i,j;
    for(i=0;i<n-1;++i){
        bool flag=false;
        for(j=n-1;j>i;--j){
            if(A[j-1]>A[j])
                swap(A[j-1],A[j]);
                flag=true;
        }
        if(!flag)
            return;
    }
}

void QuickSort(int A[],int low,int high){
    if(low<high){
        int pivotpos=Partition(A,low,high);
        QuickSort(A,low,pivotpos-1);
        QuickSort(A,pivotpos+1,high);
    }
}

int Partition(int A[],int low,int high){
    int pivot=A[low];
    while(low<high){
        while(low<high&&A[high]>=pivot)
            --high;
        A[low]=A[high];
        while(low<high&&A[low]<=pivot)
            ++low;
        A[high]=A[low];
    }
    A[low]=pivot;
    return low;
}

void SelectionSort(int A[],int n){
    for(int i=0;i<n-1;++i){
        int min=i;
        for(int j=i+1;j<n;++j)
            if(A[j]<A[min])
                min=j;
        if(min!=i)
            swap(A[min],A[i]);
    }
}

void BuildMaxHeap(int A[],int len){
    for(int i=len/2;i>0;--i)
        HeadAdjust(A,i,len);
}

void HeadAdjust(int A[],int k,int len){
    A[0]=A[k];
    for(int i=2*k;i<=len;i*=2){
        if(i<len&&A[i]<A[i+1])
            ++i;
        if(A[0]>=A[i])
            break;
        else{
            A[k]=A[i];
            k=i;
        }
    }
    A[k]=A[0];
}

void HeapSort(int A[],int len){
    BuildMaxHeap(A,len);
    for(int i=len;i>1;--i){
        swap(A[i],A[1]);
        HeadAdjust(A,1,i-1);
    }
}

归并排序
int *B=(int *)malloc(n*sizeof(int));

void Merge(int A[],int low,int mid,int high){
    int i,j,k;
    for(k=low;k<=high;k++)
        B[K]=A[K]
    for(i=low,j=mid+1,k=i;i<=mid&&j<=high;k++){
        if(B[i]<=B[j])
            A[k]=B[i++];
        else
            A[k]=B[j++];
    }
    while(j<=mid)
        A[k++]=B[i++];
    while(j<=high)
        A[k++]=B[j++];
}

void MergeSort(int A[],int low,int high){
    if(low<high){
    int mid=(low+high)/2;
    MergeSort(A,low,mid);
    MergeSort(A,mid+1,high);
    Merge(A,low,mid,high);
    }
}