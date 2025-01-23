import heapq

nums = [4, 10, 3, 5, 1]
heapq.heapify(nums)
print(nums)

heapq.heappush(nums, 0)
print(nums)

min_elem = heapq.heappop(nums)
print(min_elem)
print(nums)

min_elem = heapq.heappushpop(nums, 2)
print(min_elem)
print(nums)

min_elem = heapq.heapreplace(nums, 0)
print(min_elem)
print(nums)

largest_three = heapq.nlargest(3, nums) 
smallest_three = heapq.nsmallest(3, nums)
print(largest_three)
print(smallest_three)
print(nums)