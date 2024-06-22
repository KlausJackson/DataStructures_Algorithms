#include <iostream>
using namespace std;

// First In First Out - FIFO

class Node {
    public: 
        int val;
        Node* next;

        Node(int val) {
            this->val = val;
            next = NULL;
        }
};


class Queue {
    private:
        Node* first; Node* last;
        int length;

    public:
        Queue(int val) {
            Node* newnode = new Node(val);
            first = last = newnode;
            length = 1;
        }

        ~Queue() {
            while (first) {
                Node* temp = first;
                first = first->next;
                delete temp;
            }
        }

        void enqueue(int val) {
            Node* newnode = new Node(val);
            if (length == 0) first = last = newnode;
            else {
                last->next = newnode;
                last = newnode;
            }
            length++;
        }

        int dequeue(int val) {
            if (length == 0) return INT_MIN;
            Node* temp = first;
            int dequeued = temp->val;
            first = first->next;
            delete temp;
            if (length == 1) last = NULL;
            length--;
            return dequeued;
        }










};


int main() {




    return 0;
}
