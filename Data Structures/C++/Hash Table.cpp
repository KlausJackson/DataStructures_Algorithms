#include <iostream>
using namespace std;

class Node {
	public:
		string key;
		int val;
		Node* next;
		
		Node (string key, int val) {
			this->key = key;
			this->val = val;
			next = NULL;
		}
};


class HashTable {
	private:
		static const int SIZE = 7;
		Node* dataMap[SIZE];
//static: make the variable belong to the class.

	public:
		void print() {
			for (int i = 0; i < SIZE; i++) {
				cout << i << ":" << "\n";
				if (dataMap[i]) {
					Node* temp = dataMap[i];
					while (temp) {
						cout << " {" << temp->key << ", " << temp->val << "}" << "\n";
						temp = temp->next;
		} } } }
		
		int hash(string key) {
			int hash = 0;
			for (int i = 0; i < key.length(); i++) {
				// int(key[i]) to get the ASCII value of the character.
				hash = (hash + int(key[i]) * 23) % SIZE;
// 23 (prime number) to make the result more random.
			}
			return hash;
		}
	
		void set(string key, int val) {
			int index = hash(key);
			Node* newnode = new Node(key, val);
			if (dataMap[index] == NULL) {
				dataMap[index] = newnode;
			} else {
				Node* temp = dataMap[index];
				while (temp->next) {
					temp = temp->next;
				}
				temp->next = newnode;
			}
		}
	
};

int main() {
	HashTable* ht = new HashTable();
	ht->set("nails", 100);
	ht->set("tile", 50);
	ht->set("lumber", 80);
	ht->set("bolts", 200);
	ht->set("screws", 140);
	
	ht->print();	
	
	return 0;
}
