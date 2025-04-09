import ast


def is_final(nums: list):
    position = 0
    jumps = nums[0]
    while True:
        jumps = max(jumps, nums[position])
        if jumps <= 0:
            return False
        elif jumps >= (len(nums) - 1 - position):
            return True
        else:
            position += 1
            jumps -= 1


s = input()
nums: list = ast.literal_eval(s)  #преобразование строки в список
if not nums:
    print(False)  # пустой список
else:
    print(is_final(nums))
