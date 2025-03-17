!括号匹配问题

#define MaxSize 50
typedef struct {
    char data[MaxSize];
    int top;
} SqStack;

bool bracketCheck(char str[],int length){
    SqStack S;
    InitStack(S);
    for(int i = 0; i < length; i++){
        if(str[i] == '(' || str[i] == '[' || str[i] == '{'){
            Push(S, str[i]);
        }else{
            if(StackEmpty(S)) return false;
            char topElem;
            Pop(S, topElem);
            if(str[i] == ')' && topElem != '(') return false;
            if(str[i] == ']' && topElem != '[') return false;
            if(str[i] == '}' && topElem != '{') return false;
        }
    }
    return StackEmpty(S);
}
用数组和top
bool bracketCheck(char str[],int length){
    char stack[MaxSize];
    int top = -1;
    for(int i = 0; i < length; i++){
        if(str[i] == '(' || str[i] == '[' || str[i] == '{'){
            stack[++top] = str[i];
        }else{
            if(top == -1) return false;
            char topElem = stack[top--];
            if(str[i] == ')' && topElem != '(') return false;
            if(str[i] == ']' && topElem != '[') return false;
            if(str[i] == '}' && topElem != '{') return false;
        }
    }
    return top == -1;
}

！表达式求值问题
用栈实现
中缀转后缀+后缀求值=中缀求值

！栈在递归中的应用
