def find_pairs(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                continue
            if nums[i] + nums[j] == target:
                yield [i, j]
            
myList = [1, 2, 3, 2, 3, 4, 5, 6]
for pair in find_pairs(myList, 6):
    print(pair)
    print("{} + {} = {}".format(myList[pair[0]], myList[pair[1]], sum([myList[i] for i in pair])))