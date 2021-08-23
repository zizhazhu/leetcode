class NumArray {
public:
    vector<int> seg;
    int align_n;

    void update(int i, int val) {
        int k = i + align_n - 1;
        seg[k] = val;
        while (k > 0) {
            k = (k - 1) >> 1;
            seg[k] = seg[(k << 1) + 1] + seg[(k << 1) + 2];
        }
    }

    NumArray(vector<int>& nums) {
        if (nums.empty()) return;
        int n = nums.size() - 1;
        align_n = 1;
        while (n > 0) {
            n >>= 1;
            align_n <<= 1;
        }
        for (int i = 0; i < 2 * align_n - 1; i++) {
            seg.push_back(0);
        }
        for (int i = 0; i < nums.size(); i++)
            update(i, nums[i]);
    }
    
    int sumRangePart(int i, int j, int node, int l, int r) {
        if (node >= seg.size()) return 0;
        if (j < l || r < i) return 0;
        if (i <= l && j >= r) return seg[node];
        return sumRangePart(i, j, (node << 1) + 1, l, (l + r) >> 1) + \
            sumRangePart(i, j, (node << 1) + 2, ((l + r) >> 1) + 1, r);
    }
    
    int sumRange(int i, int j) {
        return sumRangePart(i, j, 0, 0, align_n - 1);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */
