#include <iostream>
using namespace std;

// Last In First Out - LIFO
// two ways to make a stack:
// vector, linked list
// I'll use linked list in this file.


class Node {
	public:
		int val;
		Node* next;
		
		Node (int val) {
			this->val = val;
			next = NULL;
		}		
};


class Stack {
	private:
		Node* top;
		int height;
		
	public:
		Stack(int val) {
			Node* newnode = new Node(val);
			top = newnode;
			height = 1;
		}
		
		void print() {
			Node* temp = top;
			while (temp) {
				cout << " " << temp->val;
				temp = temp->next;
			}
		}

		int getHeight() { return height; }
		int getTop() { return top->val; }
		
		void push(int val) {
			Node* newnode = new Node(val);
			newnode->next = top;
			top = newnode;
			height++;
		}
	
		int pop() {
			if (height == 0) return INT_MIN;
			Node* temp = top;
			int poppedValue = top->val;
			top = top->next;
			delete temp;
			height--;
			return poppedValue;
		}
	
	
	
	
};


int main() {
	
	Stack* stk = new Stack(4);
	stk->push(2); stk->push(8); 
	stk->push(3); stk->push(12); 
	stk->push(7); stk->push(5); 	
		
	cout << stk->getHeight() << "\n";
	cout << stk->getTop() << "\n";
	cout << "Stack:"; stk->print();
	
	return 0;
}
