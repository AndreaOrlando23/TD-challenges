#include <iostream>
#include <array>
using namespace std;


class Queue {
    private:
    int front;
    int rear;
    int arr[5];

    public:
    // constructor
    Queue() {
        front = -1;
        rear = -1;
        for(int i=0; i<5; i++) {
            arr[i]=0;
        }
    }

    bool isEmpty() {
        if(front==-1 && rear==-1)
            return true;
        else
            return false;
    }

    void enqueue(int item) {
        if(rear==-4) {
            cout << "Queue is FULL" << endl;
            return;
        }
        else if(isEmpty()) {
            rear=0;
            front=0;
            arr[rear]=item;
        }
        else {
            rear++;
            arr[rear]=item;
        }
    }

    int dequeue() {
        int x;
        if(isEmpty()) {
            cout << "Queue is EMPTY" << endl;
            return 0;
        }
        else if(front == rear) {
            x = arr[front];
            arr[front] = 0;
            front = -1;
            rear = -1;
            return x;
        }
        else {
            x = arr[front];
            arr[front] = 0;
            front++;
            return x;
        }
    }

    int count() {
        return (rear-front+1);
    }

    int peek() {
        if(!isEmpty()) {
            return arr[0];
        }
    }

};


int main() {

    Queue test1;
    int option, value;

    do {
        cout << "What operation do you want to perform? Select Option number (0 to exit)." << endl;
        cout << "1. Enqueue()" << endl;
        cout << "2. Dequeue()" << endl;
        cout << "3. isEmpty()" << endl;
        cout << "4. count()" << endl;
        cout << "5. peek()" << endl;


        cin >> option;

        switch(option) {
            case 0:
                break;

            case 1:
                cout << "Enqueue Operation \nEnter an item to Enqueue in the Queue"<<endl;
                cin >> value;
                test1.enqueue(value);
                break;

            case 2:
                cout << "Dequeue Operation \nDequeued Value: " << test1.dequeue() <<endl;
                break;
            
            case 3:
                if(test1.isEmpty())
                    cout << "Queue is Empty" << endl;
                    break;
            
            case 4:
                cout << "Count Operation \nCount of items in Queue: " << test1.count() <<endl;
                break;
            
            case 5:
                cout << "Peek Operation \nThe first item is: " << test1.peek() <<endl;
                break;
            
            default:
                cout << "Enter a valid option number " << endl;
                break;
        }
    }
    while(option!=0);

    return 0;

}
