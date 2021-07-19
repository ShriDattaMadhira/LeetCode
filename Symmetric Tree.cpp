/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        if(!root) return true;
        stack<TreeNode*> left, right;
        left.push(root->left);
        right.push(root->right);
        while(!left.empty())
        {
            auto leftptr = left.top();
            auto rightptr = right.top();

            left.pop();
            right.pop();

            if(leftptr == NULL && rightptr == NULL) continue;
            if((leftptr && rightptr == NULL) ||(leftptr == NULL && rightptr)) return false;
            if(leftptr->val != rightptr->val) return false;

            left.push(leftptr->left);
            left.push(rightptr->left);
            right.push(rightptr->right);
            right.push(leftptr->right);
        }
        return true;
    }
};