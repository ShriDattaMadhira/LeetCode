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
#include<algorithm>
class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> v;
        stack<TreeNode*> s;
        if(root) { s.push(root); }
        while(!s.empty())
        {
            auto p = s.top();
            s.pop();
            v.push_back(p->val);
            if(p->left) s.push(p->left);
            if(p->right) s.push(p->right);
        }
        std::reverse(v.begin(), v.end());
        return v;
    }
};