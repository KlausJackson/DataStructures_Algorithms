#include <iostream>
using namespace std;

class Node {
    public:
        int val;
        Node* left;
        Node* right;

        Node(int val) {
            this->val = val;
            left = right = NULL;
        }
};


class AVL {
    private:
        Node* root;
        int height;
        int balance;

    public:
        AVL() {
            root = NULL;
            height = 0;
            balance = 0;
        }

        ~AVL() { destroy(root); }

        void destroy(Node* currentNode) {
            if (currentNode->left) destroy(currentNode->left);
            if (currentNode->right) destroy(currentNode->right);
            delete currentNode;
        }

        int getHeight(Node* node) {
            if (node == NULL) return 0;
            return 1 + max(getHeight(node->left), getHeight(node->right));
        }

        int getBalance(Node* node) {
            if (node == NULL) return 0;
            return getHeight(node->left) - getHeight(node->right);
        }

        Node* rightRotate(Node* node) {
            Node* newroot = node->left;
            node->left = newroot->right;
            newroot->right = node;
            return newroot;
        }
        
        bool insert(int val) {
            Node* newnode = new Node(val);
            if (root == NULL) {
                root = newnode;
                return true;
            }
            Node* temp = root;
            while (true) {
                if (newnode->val == temp->val) return false;
                if (newnode->val < temp->val) {
                    if (temp->left == NULL) {
                        temp->left = newnode;
                        return true;
                    }
                    temp = temp->left;
                } else {
                    if (temp->right == NULL) {
                        temp->right = newnode;
                        return true;
                    }
                    temp = temp->right;
                }
            }
        }

        void print(Node* node) {
            // printing in the order of left, root, right.
            if (node == NULL) return;
            print(node->left);
            cout << node->val << " ";
            print(node->right);
        }

        Node* getRoot() { return root; }

        bool contains(int val) {
            Node* temp = root;
            while (temp) {
                if (val < temp->val) {
                    temp = temp->left;
                } else if (val > temp->val){
                    temp = temp->right;
                } else return true;
            }
            return false;
        }
};


int main() {




    return 0;
}