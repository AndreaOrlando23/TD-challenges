#include <iostream>
#include <string>

using namespace std;


class Stack {
    private:
    int top;
    int arr[5];

    public:
    // constructor
    Stack() {
        top = -1;
        for(int i=0; i<5; i++) {
            arr[i] = 0;
        }
    }

    void push(int item) {
        if(isFull()) {
            cout<<"Stack is FULL."<<endl;
        }
        else {
            top++;
            arr[top] = item;
        }
    }

     int pop() {
        if(isEmpty()) {
            cout<<"Stack is EMPTY."<<endl;
            return 0;  // I must return some value couse of the int function
        }
        else {
            int popItem = arr[top];
            arr[top] = 0;  // Replace the top value with a 0 placeholder
            top--;
            return popItem;
        }
    }

    int peek() {
        if(isEmpty()) {
            cout<<"Stack is EMPTY."<<endl;
            return 0;
        }
        else {
            return arr[top];
        }
    }

    bool isEmpty() {
        if(top==-1) 
            return true;
        else
            return false;
    }

    bool isFull() {
        if (top==4)
            return true;
        else
            return false;
    }

    int size() {
        return (top+1);
    }

    void display() {
        cout<<"All items in the Stack are: "<<endl;
        for(int i=4; i>0; i--) {  // in order to display it in the stack manner
            cout<<arr[i]<<endl;
        }
    }
};

/*
- push(item) - Add an item to the top of the stack.
- pop() - Remove the top item from the stack.
- peek() - Returns a copy of the top item in the stack.
- isEmpty() - Return a boolean indicating whether or not the stack is empty.
- size() - Return the number of items in the stack.
*/

int main() {

    Stack test1;
    int option, value;

    do {
        cout << "\n\nWhat operation do you want to perform? Select Option number (0 to exit)." << endl;
        cout << "1. Enqueue(item)" << endl;
        cout << "2. Dequeue()" << endl;
        cout << "3. peek()" << endl;
        cout << "4. isEmpty()" << endl;
        cout << "5. size()" << endl;
        cout << "6. isFull()" << endl;
        cout << "7. display()" << endl;
        

        cin >> option;

        switch(option) {
            case 0:
                break;

            case 1:
                cout << "*** Enqueue Operation 1*** \nPlease enter an item to Enqueue in the Queue:"<<endl;
                cin >> value;
                test1.enqueue(value);
                break;

            case 2:
                cout << "*** Dequeue Operation *** \nDequeued Value: " << test1.dequeue() <<endl;
                break;
            
            case 3:
                cout << "*** Peek Operation *** \nThe first item is: " << test1.peek() <<endl;
                break;
            
            case 4:
                if(test1.isEmpty())
                    cout << "Queue is Empty." << endl;
                else
                    cout << "Queue is NOT Empty." << endl;
                break;
            
            case 5:
                cout << "*** Count Operation *** \nCount of items in Queue: " << test1.size() <<endl;
                break;
            
            case 6:
                if(test1.isFull())
                    cout << "Queue is Full." << endl;
                else
                    cout << "Queue is NOT Full." << endl;
                break;
            
            case 7:
                cout << "*** Display Function Called *** \nAll values in the Queue are: ";
                test1.display();
                break;
            
            default:
                cout << "Please enter a valid option number. " << endl;
                break;
        }
    }
    while(option!=0);

    return 0;
}







/* #include <iostream>
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
*/