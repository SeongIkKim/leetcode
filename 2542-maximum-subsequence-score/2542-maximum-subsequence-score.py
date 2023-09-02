import heapq

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = list(zip(nums1,nums2))
        nums.sort(key=lambda x: -x[1])
        
        # 일단 k개 꽉 채우기
        topk_heap = [x[0] for x in nums[:k]]
        heapq.heapify(topk_heap)
        topk_sum = sum(topk_heap)
        
        ans = topk_sum * nums[k-1][1] # 최초 answer(앞의 k개 모두 더한값 * k번째로 큰 nums[i])

        # k개 유지하면서 nums2[i](min)값 줄여나가며 최대 product 찾기
        for i in range(k, len(nums)):
            topk_sum += (nums[i][0] - heapq.heappop(topk_heap)) # 더해지는 값 - 제거할 최솟값
            heapq.heappush(topk_heap, nums[i][0])

            ans = max(ans, topk_sum * nums[i][1])

        return ans
        