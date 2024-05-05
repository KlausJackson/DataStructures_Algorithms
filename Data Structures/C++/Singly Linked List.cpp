#include <iostream>
#include <string>

using namespace std;


class Node {
	public:
		int val;
		Node* next;
		
		Node(int val) {
			this->val = val;
			next = NULL;
		}
};


class SLL {
	private:
		Node* head;
		Node* tail;
		int length;
		
	public:
		SLL(int val) {
			// Constructor: has the same name as the class
			Node* newnode = new Node(val);
			head = newnode;
			tail = newnode;
			length = 1;
		}
		
		~SLL() {
			// Destructor
			
			/* If you don't write a destructor, the default destructor will be
			run when you delete an instance.
			
			This linked list has head, tail, length and and nodes.
			because there're two different classes: linked list, node. So the
			default destructor is going to delete head, tail and length,
			but all of the nodes will remain in memory.
			That's why we have to write a destructor for the linked list class.	*/	
			
			Node* temp = head;
			while (head) {
				head = head->next;
				delete temp;
				temp = head;
				// delete all the nodes, except for the tail, head, length.
			length = 0;
			}
		}
		
		void print() {
			Node* temp = head;
			while (temp) {
				cout << temp->val << endl;
				temp = temp->next;
			}
		}
		
		void append(int val) {
			Node* temp = new Node(val);
			if (head == NULL) {
				head = temp;
				tail = temp;
			} else {
				tail->next = temp;
				tail = temp;
			}
			length++;
		}
	
		void prepend(int val) {
			Node* newnode = new Node(val);
			newnode->next = head;
			head = newnode;
			if (length == 0) tail = newnode;
			length++;
		}
		
		void pop() {
			if (head == NULL)	return;
			if (length == 1) {
				head = NULL;
				tail = NULL;				
			}	else {
				Node* pre = head;
				Node* now = head;
				
				while (now->next) {
					pre = now;
					now = now->next;
				}
				tail = pre;
				tail->next = NULL;
				delete now;				
			}
			length--;
		}
	
		void pop_first() {
			if (length == 0) return;
			if (length == 1) tail = NULL;
			Node* temp = head;
			head = head->next;
			delete temp;
			length--;
		}
	
		Node* get(int index) {
			if (index < 0 || index >= length) return NULL;
			Node* temp = head;
			for (int i = 0; i < index; i++) {
				temp = temp->next;
			}
			return temp;
		}
	
		bool set(int index, int val) {
			Node* temp = get(index);
			if (temp) {
				temp->val = val;
				return true;
			}
			return false;
		}
	
		bool insert(int index, int val) {
			if (index < 0 || index > length) return false;
			if (index == 0) prepend(val);
			else if (index == length) append(val);
			else{
				Node* temp = get(index - 1);
				Node* newnode = new Node(val);
				newnode->next = temp->next;
				temp->next = newnode;
				length++;
			}
			return true;
		}
	
		void delete_at(int index) {
			if (index < 0 || index >= length) return;
			if (index == 0) return pop_first();
			if (index == length) return pop();
			Node* pre = get(index - 1);
			Node* temp = pre->next;
			pre->next = temp->next;
			delete temp;
			length--;
		}
	
		void reverse() {
			Node* temp = head;
			head = tail;
			tail = temp;
			
			Node* before = NULL;
			Node* after = temp->next;
			for (int i = 0; i < length; i++) {
				after = temp->next;
				temp->next = before;
				before = temp;
				temp = after;
			}
		}
	
	
	
	
	
	
	
	
	
	
	
};


int main() {
	
	SLL* ll = new SLL(4);
	ll->append(8);
	ll->append(0);
	ll->append(2);
	ll->append(5);
	ll->append(9);
	ll->append(3);	
	
	ll->insert(7, 99);
	//ll->reverse();
	//cout << "Index 5: " << ll->get(5)->val;
	
	cout << endl;
	ll->print();

	
	return 0;	
}
