#include <iostream>
using namespace std;

struct node {
int key;
struct node *left, *right;
};

struct node *newNode(int item) {
struct node *temp = (struct node *)malloc(sizeof(struct node));
temp->key = item;
temp->left = temp->right = NULL;
return temp;
}

void inorder(struct node *root) {
if (root != NULL) {
inorder(root->left);
cout << root->key << " -> ";
inorder(root->right);
}
}

struct node *insert(struct node *node, int key) {
if (node == NULL) return newNode(key);
// wyruszamy na prwo i tworzymy ga³¹Ÿ
if (key < node->key)
node->left = insert(node->left, key);
else
node->right = insert(node->right, key);
return node;
}

struct node *minValueNode(struct node *node) {
struct node *current = node;
// szukamy liœcia wysuniêtego jak najbardziej na lewo
while (current && current->left != NULL)
current = current->left;
return current;
}

struct node *deleteNode(struct node *root, int key) {
if (root == NULL) return root;
// szukamy ga³êzi do usuniêcia
if (key < root->key)
root->left = deleteNode(root->left, key);
else if (key > root->key)
root->right = deleteNode(root->right, key);
else {
// 0/1
if (root->left == NULL) {
struct node *temp = root->right;
free(root);
return temp;
}
else if (root->right == NULL) {
struct node *temp = root->left;
free(root);
return temp;
}
// w przypypdku dwóch dzieci
struct node *temp = minValueNode(root->right);
// umieszczmy nastêpce w pozycji do usuniêcia
root->key = temp->key;
// usuwamy nastêpce
root->right = deleteNode(root->right, temp->key);
}
return root;
}

int main() {
struct node *root = NULL;
root = insert(root, 18);
root = insert(root, 11);
root = insert(root, 6);
root = insert(root, 30);
root = insert(root, 21);
root = insert(root, 19);
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 23);
root = insert(root, 5);
root = insert(root, 20);
root = insert(root, 26);
root = insert(root, 17);
inorder(root);
cout << "\n";
root = deleteNode(root, 8);
root = deleteNode(root, 30);
root = deleteNode(root, 18);
root = deleteNode(root, 11);
inorder(root);
}
