#include<iostream>
using namespace std;
int top=-1;
int stack[5];
void push(char c)
{
    if(top==4)
    {
        cout<<"Stack overflow"<<endl;
    }
    else
    {
        top=top+1;
        stack[top]=c;
    }
}
void pop()
{
    if(top==-1)
    {
        cout<<"Stack underflow"<<endl;
    }
    else
    {
        top=top-1;
    }
}

int main()
{
    string s;
    cout<<"Enter your input: ";
    cin>>s;

    for(int i=0;i<s.length();i++)
    {
        char c=s.at(i);
        if(c=='('||c=='{'||c=='[')
            {
                push(c);
            }
        else if (c==')'&&stack[top]=='(')
        {
            pop();
        }
        else if (c=='}'&&stack[top]=='{')
        {
            pop();
        }
        else if (c==']'&&stack[top]=='[')
        {
            pop();
        }
    }

        if(top==-1)
        {
            cout<<"Parenthesis is balanced"<<endl;
        }
        else
        {
            cout<<"Parenthesis is unbalanced"<<endl;
        }
        return 0;

    }

