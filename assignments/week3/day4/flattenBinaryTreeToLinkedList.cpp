class Solution {
private:
    TreeNode* prev = nullptr;
public:
    void flatten(TreeNode* root) {
        if (root == nullptr) return;
        
        flatten(root->right);
        flatten(root->left);
        
        root->left = nullptr;
        root->right = this->prev;
        this->prev = root;
        
    }
};
