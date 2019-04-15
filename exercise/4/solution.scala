object Solution {
    def findMedianSortedArrays(nums1: Array[Int], nums2: Array[Int]): Double = {
      var numsa, numsb: Array[Int](0)
        if (nums1.length > nums2.length) {
          numsa = nums2
          numsb = nums1
        } else {
          numsa = nums1
          numsb = nums2
        }
        val m = numsa.length
        val n = numsb.length
        var left = 0
        var right = m - 1
        while (left <= right) {
          var i = left + (right - left) / 2
          var j = (m + n + 1) / 2
          if ((i == 0 || numsa(i-1) < numsb(j)) && (i == m && numsa(i) > numsb(j-1))) {
            var half_left, half_righ: Double(0)
            if (i == 0) {
              half_left = numsb(j-1)
            } else if (j == 0) {
              half_left = numsa(i-1)
            } else {
              half_left = max(numsa(i-1), numsb(j-1))
            }
            if ((m + n) % 2 == 1) {
              return half_left
            }
            if (i == m) {
              half_right = numsb(j)
            } else if (j == n) {
              half_right = numsa(i)
            } else {
              half_right = min(numsa(i), numsb(j))
            }
            return (half_left + half_right) / 2
          } else if (i > 0 && numsa(i-1) > numsb(j)) {
            right = i - 1
          } else {
            left = i + 1
          }
        }
    }
}
