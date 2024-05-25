# DataStructures_Algorithms
[![Python version](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://shields.io/) 
![License](https://img.shields.io/badge/License-MIT-blue.svg)
[![GitHub top language](https://img.shields.io/github/languages/top/KlausJackson/DataStructures_Algorithms?logo=github)](https://github.com/KlausJackson/DataStructures_Algorithms) 
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/KlausJackson/DataStructures_Algorithms?logo=github)](https://github.com/KlausJackson/DataStructures_Algorithms) 
[![GitHub issues](https://img.shields.io/github/issues/KlausJackson/DataStructures_Algorithms?logo=github)](https://github.com/KlausJackson/DataStructures_Algorithms)
[![GitHub issues](https://img.shields.io/github/issues-closed/KlausJackson/DataStructures_Algorithms?logo=github)](https://github.com/KlausJackson/DataStructures_Algorithms)
[![GitHub issues](https://img.shields.io/github/issues-pr/KlausJackson/DataStructures_Algorithms?logo=github)](https://github.com/KlausJackson/DataStructures_Algorithms)
[![GitHub issues](https://img.shields.io/github/issues-pr-closed/KlausJackson/DataStructures_Algorithms?logo=github)](https://github.com/KlausJackson/DataStructures_Algorithms)

![](https://img.shields.io/github/forks/KlausJackson/DataStructures_Algorithms.svg)
![](https://img.shields.io/github/stars/KlausJackson/DataStructures_Algorithms.svg)
![](https://img.shields.io/github/watchers/KlausJackson/DataStructures_Algorithms.svg)

My Python, C++ code and notes while learning about Data Structures and Algorithms. <br>

## Credits
Most of my code are from the following source on Udemy:
- [Python Data Structures & Algorithms + LEETCODE Exercises](https://ascend.udemy.com/course/data-structures-algorithms-python)
- [C++ Data Structures & Algorithms + LEETCODE Exercises](https://ascend.udemy.com/course/data-structures-algorithms-cpp)

The instructor: [Scott Barrett](https://ascend.udemy.com/user/scott-barrett-16/) <br>
The rest of my code are solutions to some problems on [LeetCode](https://leetcode.com/). <br>

## How To Contact Me
[![Patreon](https://img.shields.io/badge/Patreon-AC7AC2?style=for-the-badge&logo=patreon&logoColor=white)](patreon.com/KlausJackson)
[![Buy Me A Coffee](https://img.shields.io/badge/BuyCoffee-FFFF00?style=for-the-badge&logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/klausjackson)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/KlausJackson/) 
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:KlausJackson2@gmail.com)
[![Steam](https://img.shields.io/badge/Steam-000050?style=for-the-badge&logo=steam&logoColor=white)](https://steamcommunity.com/id/KlausJackson/)
[![Twitter](https://img.shields.io/badge/Twitter-0044BB?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/Klaus_Jackson2)

## Data Structures
I left a #LEETCODE next to every leetcode problem. <br>

### Singly linked list (25 LEETCODE problems) : a linear data structure where each node contains a data element and a reference (or pointer) to the next node in the list. <br>

* Common Algorithms and Problems
    - Reversal: Reversing the order of the nodes in the list.
    - Merge/Split: Combining or dividing linked lists.
    - Cycle Detection: Detecting if the list contains a cycle (a node that points to a previous node).

* Pro
    - Efficient insertion and deletion at the beginning of the list (O(1) time complexity).
    - Dynamic size - the list can grow or shrink as needed.
    - Memory efficient - only the necessary memory is allocated for each node.

* Cons
    - Accessing an element at a specific index is less efficient (O(n) time complexity).
    - Reversal and other operations can be more complex to implement.
    - Traversing the list can be slower than accessing elements in an array.    

* Use Cases
    - Implementing stacks and queues
    - Representing sparse matrices
    - Managing memory allocation and deallocation
    - Implementing undo/redo functionality


### Doubly linked list : a variation of the singly linked list, where each node contains a data element and two references (or pointers) - one to the next node and one to the previous node.
  
* Common Algorithms and Problems
    - Bi-directional Traversal: Iterating through the list in both forward and backward directions.
    - Merge/Split: Combining or dividing doubly linked lists.

* Pro
    - Bi-directional traversal: Allows for efficient navigation in both forward and backward directions.
    - Efficient deletion of a node: The previous and next nodes can be easily updated to bypass the deleted node.

* Cons
    - Additional memory overhead: Each node must store two pointers instead of one.
    - Slightly more complex to implement compared to singly linked lists.

* Use Cases
    - Implementing undo/redo functionality.
    - Maintaining a history of user actions.
    - Implementing text editors and music player playlists.
    - Representing two-way relationships in databases.


### Stack : a linear data structure that follows the Last-In-First-Out (LIFO) principle, where elements are added and removed from the top of the stack.

* Common Algorithms and Problems
    - Push: Adding an element to the top of the stack.
    - Pop: Removing the top element from the stack.
    - Peek: Accessing the top element without removing it.
    - Checking emptiness: Determining if the stack is empty.

* Pro
    - Simple and intuitive data structure.
    - Efficient insertion and deletion at the top (O(1) time complexity).
    - Useful for function call management and undo/redo operations.

* Cons
    - Limited access: Only the top element can be accessed and manipulated.
    - Fixed or limited size if implemented using an array.

* Use Cases
    - Function call management (e.g., call stack).
    - Expression evaluation and syntax parsing.
    - Undo/redo operations in text editors or design software.
    - Depth-first search (DFS) in graph algorithms.


### Queues : a linear data structure that follows the First-In-First-Out (FIFO) principle, where elements are added at the rear (enqueue) and removed from the front (dequeue) of the queue.

* Common Algorithms and Problems
    - Enqueue: Adding an element to the rear of the queue.
    - Dequeue: Removing an element from the front of the queue.
    - Peek: Accessing the front element without removing it.
    - Checking emptiness: Determining if the queue is empty.

* Pro
    - Efficient insertion at the rear and deletion from the front (O(1) time complexity).
    - Useful for job scheduling, event handling, and breadth-first search (BFS) algorithms.

* Cons
    - Limited access: Only the front and rear elements can be accessed and manipulated.
    - Fixed or limited size if implemented using an array.

* Use Cases
    - Job scheduling and processing.
    - Breadth-first search (BFS) in graph algorithms.
    - Event handling and message queues.
    - Buffering and flow control in computer systems.


### Hash Table : a data structure that uses a hash function to map keys to their corresponding values, allowing for efficient lookup, insertion, and deletion of data.

* Common Algorithms and Problems
    - Hash function: Mapping keys to unique indices in the hash table.
    - Collision handling: Dealing with situations where two keys hash to the same index.
    - Insertion: Adding a key-value pair to the hash table.
    - Lookup: Retrieving the value associated with a given key.
    - Deletion: Removing a key-value pair from the hash table.

* Pro
    - Efficient lookup, insertion, and deletion operations (average case O(1) time complexity).
    - Flexible and adaptable to various data types as keys.
    - Useful for implementing caches, dictionaries, and other data-intensive applications.

* Cons
    - Collisions can degrade performance if not handled properly.
    - Hash table size must be predetermined or dynamically resized, which can be costly.
    - Hash function design can significantly impact performance.

* Use Cases
    - Caching and memoization.
    - Implementing dictionaries and associative arrays.
    - Deduplication and data compression.
    - Solving problems that require fast lookups, such as frequency counting and unique element identification.


### Graph : a non-linear data structure consisting of a set of nodes (or vertices) and a set of edges that connect these nodes, representing relationships between them.

* Common Algorithms and Problems
    - Graph representation: Adjacency list, adjacency matrix.
    - Traversal: Depth-first search (DFS), breadth-first search (BFS).
    - Shortest path: Dijkstra's algorithm, Bellman-Ford algorithm.
    - Connectivity: Finding connected components, detecting cycles.
    - Topological sorting: Ordering nodes in a directed acyclic graph.

* Pros:
    - Flexible and versatile for modeling real-world relationships and networks.
    - Efficient for representing and solving complex problems, such as route planning and social network analysis.
    
* Cons:
    - Potentially high memory consumption for dense graphs.
    - Traversal and shortest path algorithms can be - computationally expensive for large graphs.

* Use Cases
    - Social network analysis.
    - Recommendation systems.
    - Route planning and navigation.
    - Modeling dependencies and connections in software systems.
    - Analyzing network traffic and detecting anomalies.


### Tree : a hierarchical data structure that consists of a root node, parent nodes, and child nodes, with each node having zero or more child nodes.

* Common Algorithms and Problems
    - Tree traversal: Preorder, inorder, postorder, level-order.
    - Insertion and deletion: Adding or removing nodes in the tree.
    - Searching: Finding a specific node or value in the tree.
    - Balancing: Maintaining the tree's balance for efficient operations (e.g., AVL trees, red-black trees).

* Pros:
    - Efficient for hierarchical data organization and navigation.
    - Provide logarithmic time complexity for common operations like search, insertion, and deletion.
    - Useful for representing and solving problems with inherent hierarchical structures.

* Cons:
    - Potential for unbalanced trees, leading to degraded performance.
    - Maintaining balanced trees can add complexity to the implementation.

* Use Cases
    - File system organization.
    - Representing hierarchical data (e.g., organizational structures).
    - Implementing expression parsers and compilers.
    - Searching and sorting algorithms (e.g., binary search trees).
    - Decision-making processes and expert systems.


### Heap 




## Algorithms
* Backtracking : recursively exploring all possible solutions until a valid solution is found. <br>

## Note
I added comments in the code, they're explainations based on my understanding. <br>

