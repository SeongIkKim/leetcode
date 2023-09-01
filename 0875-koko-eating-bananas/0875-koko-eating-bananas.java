import java.util.*;

/*
 * Binary search from 1 to m(max in piles) to find minimum workable speed
 */
class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1;
        int right = Arrays.stream(piles).max().getAsInt();
        
        while (left < right) {
            int mid = (left + right) / 2;
            int hourSpent = 0;

            for (int pile : piles){
                hourSpent += Math.ceil((double) pile / mid);
            }

            // workable. Lower speed.
            if (hourSpent <= h){
                right = mid;
            } else{ // not workable. Higher speed.
                left = mid+1;
            }
        }
        return right; // or left
    }
}