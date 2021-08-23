class NumArray {
public:
    vector<int> bit;
    int n;

    int sumRange(int i) {
        int sum = 0;
        while (i > 0) {
            sum += bit[i];
            i = i & (i - 1);
        }
        return sum;
    }

    int sumRangeIn(int i, int j) {
        return sumRange(j) - sumRange(i);
    }

    int sumRange(int i, int j) {
        return sumRangeIn(i, j + 1);
    }

    void update(int i, int val) {
        int ori = sumRange(i, i);
        int delta = val - ori;
        i += 1;
        while (i <= n) {
            bit[i] += delta;
            i += i & -i;
        }
    }

    NumArray(vector<int>& nums) {
        n = nums.size();
        if (n == 0) return;
        bit.push_back(0);
        for (int i = 1; i <= n; i++)
            bit.push_back(0);
        for (int i = 0; i < n; i++)
            update(i + 1, nums[i]);
    }
    
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */
