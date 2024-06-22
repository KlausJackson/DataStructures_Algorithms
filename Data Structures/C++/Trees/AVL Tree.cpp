#include <iostream>
using namespace std;

class Node {
    public:
        int val; int height;
        Node* left;
        Node* right;

        Node(int val, int height) {
            this->val = val;
            left = right = NULL;
            this->height = height;
        }
};


class AVL {
    private:
        Node* root;
        int height;

    public:
        AVL() {
            root = NULL;
            height = 0;
        }

        ~AVL() { destroy(root); }

        void destroy(Node* currentNode) {
            if (currentNode->left) destroy(currentNode->left);
            if (currentNode->right) destroy(currentNode->right);
            delete currentNode;
        }

        int getHeight(Node* node) { return node == NULL ? -1 : node->height; }
        Node* getRoot() { return root; }

        void leftRotate(Node* &k2) {
            Node* k1 = k2->left;
            k2->left = k1->right;
            k1->right = k2;
            k2->height = max(getHeight(k2->left), getHeight(k2->right)) + 1;
            k1->height = max(getHeight(k1->left), k2->height) + 1;
            k2 = k1;
        }

        void rightRotate(Node* k1) {
            Node* k2 = k1->right;
            k1->right = k2->left;
            k2->left = k1;
            k1->height = max(getHeight(k1->left), getHeight(k1->right)) + 1;
            k2->height = max(getHeight(k2->right), k1->height) + 1;
            k1 = k2;
        }

        void doubleRightRotate(Node* &k1) {
            leftRotate(k1->right);
            rightRotate(k1);
        }
        void doubleLeftRotate(Node* &k3) {
            rightRotate(k3->left);
            leftRotate(k3);
        }

        void insert(int val, Node* &node) {
            if (root == NULL) root = new Node(val, 0);
            else if (val < node->val) insert(val, node->left);
            else if (val > node->val) insert(val, node->right);
            balance();
        }

        void balance() {
            if (root == NULL) return;
            if (getHeight(root->left) - getHeight(root->right) > 1) {
                if (getHeight(root->left->left) >= getHeight(root->left->right))
                    leftRotate(root); 
                else 
                    doubleLeftRotate(root); 
            } else if (getHeight(root->right) - getHeight(root->left) > 1) {
                if (getHeight(root->right->right) >= getHeight(root->right->left))
                    rightRotate(root);
                else
                    doubleRightRotate(root);
            }
            root->height = max(getHeight(root->left), getHeight(root->right)) + 1;
        }

        void printLeaves(Node* node) {
            // printing in the order of left, root, right.
            if (node == NULL) return;
            printLeaves(node->left);
            cout << node->val << " ";
            printLeaves(node->right);
        }

        void remove(int val, Node* &node) {
            if (node == NULL) return;
            if (val < node->val) remove(val, node->left);
            else if (val > node->val) remove(val, node->right);
            else if (node->left != NULL && node->right != NULL) {
                node->val = findMin(node->right)->val;
                remove(node->val, node->right);
            } else {
                Node* temp = node;
                node = (node->left != NULL) ? node->left : node->right;
                delete temp;
            }
        }

        Node* findMin(Node* node) {
            while (node->left) node = node->left;
            return node;
        }

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