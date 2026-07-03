class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = set(list1) & set(list2)
        common = list(common)
        indices = []
        for x in common:
            indices.append([sum([list1.index(x), list2.index(x)]), x])

        mn = min(y[0] for y in indices)
        answer = []
        for m in indices:
            if m[0] == mn:
                answer.append(m[1])

        return answer 
