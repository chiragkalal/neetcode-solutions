class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        # print(people)
        left, right = 0, len(people) - 1
        
        boats_count = 0
        while left <= right:
            remain = limit - people[right]
            # print(f"Right -> {right} & TotalLen -> {len(people)}")
            right -= 1
            boats_count += 1
            
            if left <= right and remain >= people[left]:
                left += 1
                
        
        # print("Total boats required: ", boats_count)
        return boats_count