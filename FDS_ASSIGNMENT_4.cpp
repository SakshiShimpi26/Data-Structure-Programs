#include "iostream"
using namespace std;
#include<string>
string stack1;

char PUNCTUATION[20]="!@#$%^&*;:\",%";
class Demo
{
    string line,temp="",newStr="",str="",finalStr="";
    int i=0,strLength=0,top=-1;
    int result=0;

    public:
    void operation()
    {
        cout<<"\n Enter a String:";
        getline(cin,line);

        for(int i=0;i<line.size();i++)
        {
            if((line[i]>='a' && line[i]<='z')|| (line[i]>='A' && line[i]<='Z'))
                temp=temp+line[i];
        }
        line=temp;
        //cout<<line;

        for(int i=0; i<line.size();i++)
        {
            if(line[i]>=65 && line[i]<=92)
                line[i]=line[i]+32;
        }
        //cout<<line<<"\n";
        strLength=line.size();
        //cout<<strLength<<"\n";
        pushToStack();
    }

    void pushToStack()
    {
        if(top==strLength-1)
            cout<<"\nOVERFLOW";
        else
        {
            for(i=0;i<=strLength;i++)
            {
                top++;
                stack1[top]=line[i];
                newStr=newStr+stack1[top];
                //cout<<stack1[top]<<"\n";
            }
            //cout<<newStr;
        }
        popFromStack();
    }

    void popFromStack()
    {
        if(top==-1)
            cout<<"\nUNDERFLOW";
        else{
            for(i=strLength;i>=0;i--){
            str = stack1[top];
            finalStr=finalStr+str;
            top--;
            }
            //cout<<"\n"<<finalStr;
        }

        cout<<"\n####################################";
        cout<<"\nReversed String: "<<finalStr;
        cout<<"\nOriginal String: "<<line;
        cout<<"\n####################################";

        for(i=0;i<strLength/2;i++)
        {
            if(finalStr[i]==line[strLength-i-1])
                result++;
        }

        if(result==i-1)
            cout<<"\nPallindrome";
        else
            cout<<"\nNOT Pallindrome";

        /*cout<<newStr;

        result=finalStr.compare(line)==0;
        if(result==0)
            cout<<"\n\n String Is Pallindrome";
        else
            cout<<"\n\n String Is NOT Pallindrome";*/
    }
};

int main()
{
    Demo d1;
    d1.operation();
}
