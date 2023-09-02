import java.util.*;

class Solution {
    public long totalCost(int[] costs, int k, int candidates) {
        PriorityQueue<Integer> heapFirst = new PriorityQueue<>();
        PriorityQueue<Integer> heapLast = new PriorityQueue<>();
        for (int i=0; i<candidates; i++){
            heapFirst.add(costs[i]);
        }
        // heapLast size is AT MOST candidates
        for (int i = Math.max(candidates, costs.length - candidates); i< costs.length; i++){
            heapLast.add(costs[i]);
        }
        
        long total_cost = 0;
        int l = candidates;
        int r = costs.length - 1 - candidates; // anyway, we considered r to this point regardless of heapLast size
        while (k > 0){
            if (heapLast.isEmpty() ||
             (!heapFirst.isEmpty() && heapFirst.peek() <= heapLast.peek())){
                 total_cost += heapFirst.poll();
                 if (l <= r) {
                     heapFirst.add(costs[l++]);
                 }
             } else {
                 total_cost += heapLast.poll();
                 if (l <= r) {
                     heapLast.add(costs[r--]);
                 }
             }
             k--;
        }
        
        return total_cost;
    }
}