#include <iostream>
using namespace std;

// Define the Node structure for the linked list
struct Node {
    int data;
    Node* next;

    // Constructor to initialize a node with data
    Node(int data) {
        this->data = data;
        this->next = nullptr;
    }
};

// Function to insert a new node at the beginning of the list
void insertAtBeginning(Node*& head, int value) {
    Node* newNode = new Node(value);  // Create a new node with the given value
    newNode->next = head;             // Point it to the current head
    head = newNode;                   // Update head to the new node
}

// Function to delete the first 'd' nodes from the list
void deleteFromBeginning(Node*& head, int d) {
    Node* temp;
    while (d-- > 0 && head != nullptr) {
        temp = head;        // Store the current head
        head = head->next;  // Update head to the next node
        delete temp;        // Delete the old head node
    }
}

// Function to print the linked list
void printList(Node* head) {
    if (head == nullptr) {
        cout << "List is empty" << endl;
        return;
    }
    Node* temp = head;
    while (temp != nullptr) {
        cout << temp->data;
        if (temp->next != nullptr) cout << ", "; // Formatting for output
        temp = temp->next;
    }
    cout << endl;
}

int main() {
    int n, d;
    cin >> n;  // Read the number of elements in the linked list
    Node* head = nullptr;  // Initialize an empty linked list

    // Read n elements and insert them at the beginning
    for (int i = 0; i < n; ++i) {
        int value;
        cin >> value;
        insertAtBeginning(head, value);
    }

    cin >> d;  // Read the number of elements to delete from the beginning

    // Delete d elements from the beginning
    deleteFromBeginning(head, d);

    // Print the modified linked list
    printList(head);

    return 0;
}
