import java.util.*;

class Solution {
    public long maxScore(int[] nums1, int[] nums2, int k) {
        int n = nums1.length;
        int[][] pairs = new int[n][2];
        for (int i = 0; i < n; i++) {
            pairs[i] = new int[]{nums1[i], nums2[i]};
        }
        // reverse order. comparator 내부 식이 양수가 되면 자리를 바꾼다.
        // nums2 원소들이 있는 a[1],b[1]을 비교하는데 b[1] - a[1]은 뒤의 원소가 더 크면 자리를 바꾸므로 역순
        Arrays.sort(pairs, (a,b) -> b[1] - a[1]); 
        
        // Top-k개의 원소를 유지해야하면 size가 k인 heap을 떠올리자.
        // 가장 큰 k개를 유지해야하는데, 그러려면 max-heap이 아니라 min-heap을 사용해야한다.
        // min-heap으로 k개가 남을 때까지 최솟값들을 계속 제거해나가면 힙에는 최대값들만 남기 때문.
        PriorityQueue<Integer> topKHeap = new PriorityQueue<>(k, (a,b) -> a - b); // min heap
        long topKSum = 0;
        for (int i =0; i< k; i++){
            topKSum += pairs[i][0];
            topKHeap.add(pairs[i][0]);
        }

        // The score of the first k pairs
        long answer = topKSum * pairs[k - 1][1]; // nums2를 역순 정렬했으므로 min(nums2)는 가장 마지막 원소
        
        // 모든 nums2[i]에 대해 
        for (int i = k; i<n; i++){
            topKSum += pairs[i][0] - topKHeap.poll(); // 최솟값 제거 후 nums1[i] 합산
            topKHeap.add(pairs[i][0]);

            answer = Math.max(answer, topKSum * pairs[i][1]);
        }
        
        return answer;
    }
}