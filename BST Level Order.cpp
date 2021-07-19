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
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> a;
        vector<int> x;
        queue<TreeNode*> q;
        if(root)
        {
            q.push(root);
            q.push(NULL);
        }
        //vector<int> y;
        while(!q.empty())
        {
            auto p = q.front();
            q.pop();
            if(p == NULL)
            {
                a.push_back(x);
                x.resize(0);
                if(q.size()>0) q.push(NULL);
            }
            else
            {
                x.push_back(p->val);
                if(p->left) q.push(p->left);
                if(p->right) q.push(p->right);
            }
        }
        return a;
    }
};