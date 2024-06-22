// 2 types of Heap: Max Heap and Min Heap
// Max Heap: Parent node is always greater than its child nodes.
// Min Heap: Parent node is always smaller than its child nodes.

// The root element will be at Arr[1].
// Left child of Arr[i] will be at Arr[2*i].
// Right child of Arr[i] will be at Arr[2*i+1].
// Parent of Arr[i] will be at Arr[i/2] (i/2 is the floor value of i/2).

// Insertion: Insert at the end (to keep the tree complete) 
// then keep comparing it to its parent node.


#include <iostream>
#include <vector>
#include <limits>
using namespace std;

// This is a Max Heap.
class Heap {
    private:
        vector<int> heap;
        
        int leftChild(int i) { return 2 * i;}
        int rightChild(int i) { return 2 * i + 1;}
        int parent(int i) { return (i) / 2; }

        void swap(int i, int j) {
            int temp = heap[i];
            heap[i] = heap[j];
            heap[j] = temp;
        }

    public:
        Heap() {
            heap.push_back(INT_MAX); // to make the index start from 1.
        }

        void insert(int val) {
            heap.push_back(val);
            int current = heap.size() - 1;
            while (current > 1 && heap[current] > heap[parent(current)]) {
                swap(current, parent(current));
                current = parent(current); // update the current index.
            }
        }

        void print() {
            for (int i = 1; i < heap.size(); i++) {
                cout << " " << heap[i];
            }
        }

        int remove() {
            // remove the root by swapping it with the last element.
            // then comparing it with its children.
            if (heap.size() == 1) return INT_MIN;
            int root = heap[1];  // max value.
            if (heap.size() == 2) {
                heap.pop_back();
            } else {
                heap[1] = heap.back(); // swap the root with the last element.
                heap.pop_back(); // remove the last element.
                sinkdown(1); // sink down the root element to its appropriate place.
            }
            return root; // return old max value.
        }

        void sinkdown(int i) {
            int greaterVal = i;
            while (1) {
                int leftIndex = leftChild(greaterVal);
                int rightIndex = rightChild(greaterVal);

                // check for index value to avoid out of bound error.
                if (leftIndex < heap.size() && heap[leftIndex] > heap[greaterVal])
                    greaterVal = leftIndex;
                if (rightIndex < heap.size() && heap[rightIndex] > heap[greaterVal])
                    greaterVal = rightIndex;

                // if the greaterVal index is not the same as the parent index.
                if (greaterVal != i) {
                    swap(i, greaterVal);
                    i = greaterVal;
                } else { return; }
            }
        }
};


int main() {

    Heap* h = new Heap();
    h->insert(99);
    h->insert(72);
    h->insert(61);
    h->insert(58);
    h->insert(100);
    h->insert(75);

    h->print(); // 100 99 75 99 58 72 61

    return 0;
}

