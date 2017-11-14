def twoSum(nums, target):
    """
    :type nums List[int]
    :type target int
    :rtype List[int]
    """
    for i, e in enumerate(nums):
        for j, k in enumerate(nums):
            if j == k:
                continue
            if e + k == target:
                return [i,j]

    return []

def main():
    nums = [int(x) for x in raw_input('Please input a line of numbers:').split()]
    target = input('Please input a target sum:')

    print twoSum(nums, target)

if __name__ == '__main__':
    main()
