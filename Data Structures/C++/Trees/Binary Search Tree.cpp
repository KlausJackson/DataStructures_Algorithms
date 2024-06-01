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

class BST {
    private:
        Node* root;

    public:
        // Way 1: create new node as the root.
        // BST(int val) {
        //     Node* newnode = new Node(val);
        //     root = newnode;
        // }

        // Way 2: create an empty tree, add new nodes later 
        // using insert function.
        BST() { root = NULL; }

        ~BST() { destroy(root); }

        void destroy(Node* currentNode) {
            if (currentNode->left) destroy(currentNode->left);
            if (currentNode->right) destroy(currentNode->right);
            delete currentNode;
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
    BST* tree = new BST();
    tree->insert(5);
    tree->insert(3);
    tree->insert(7);
    tree->insert(2);
    tree->insert(4);
    
    tree->print(tree->getRoot());

    return 0;
}

