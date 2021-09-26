#include <iostream>
#include <stack>
#include <list>


using namespace std;

class Stack {
public:
    stack<int> myStack;

    void push(int item) {
        myStack.push(item);
    }

    void pop() {
        myStack.pop();
    }

    void peek() {
        cout << "The first element is: " << myStack.top() << endl;
    }

    bool isEmpty() {
        if (myStack.empty()) {
            return true;
        return false;
        }
    }

    int size() {
        cout << "The size of the array is: " << myStack.size() << endl;
    }

    // constructor
    Stack(stack<int []> mystack) {
        myStack = mystack;
    }

};

int main()
{
    Stack test1 = Stack();

    test1.push(10);

}