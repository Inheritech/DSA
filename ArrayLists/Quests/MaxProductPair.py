def find_max_product(nums, target):
    max_product = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            current_product = nums[i] * nums[j]
            if current_product > max_product:
                max_product = current_product
    return max_product