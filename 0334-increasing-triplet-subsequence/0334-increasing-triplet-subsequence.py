import sys

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        크기순으로 담으려하지말고, 1st와 2nd를 따로 담을것
        [1,2,0,3]의 경우를 고려해보면 1st를 1에서 0으로 업데이트하더라도 2nd는 2로 고정
        생각해보면 매 순간 1st를 업데이트하고 그 다음 2nd를 업데이트하는데,
        이는 곧 2nd가 할당된 순간 1st, 2nd 쌍은 존재한다는 말이며
        1st가 업뎃되더라도 항상 같거나 더 작은 수로만 업데이트되므로 1st < 2nd 관계는 항상 성립한다.
        현재 할당된 1st와 2nd의 인덱스와 관계없이 3rd가 2nd보다 크기만 하다면
        1st(현재든 이전에 할당된 수든) < 2nd(현재든 이전에 할당된 수든) < 3rd 관계가 성립함.
        """
        first = second = sys.maxsize
        for n in nums:
            if n <= first: # eqaul 조건을 넣는 것은 동일한 숫자로 triplet을 완성하지 않도록 방지
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False