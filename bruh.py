import random

def random_summing():
    nums = [random.randint(1, 100) for _ in range(10)]
    total = sum(nums)
    print("Numbers:", nums)
    print("Sum:", total)
    return total

def random_subtracting():
    a = random.randint(50, 150)
    b = random.randint(1, 50)
    result = a - b
    print(f"Subtracting {b} from {a} = {result}")
    return result

def random_multiplying():
    nums = [random.randint(1, 10) for _ in range(5)]
    product = 1
    for n in nums:
        product *= n
    print("Numbers:", nums)
    print("Product:", product)
    return product

if __name__ == "__main__":
    print("Running dummy math operations...\n")
    random_summing()
    print()
    random_subtracting()
    print()
    random_multiplying()

'''
bru hbruh burh burh ub h

hi

helo 
1 2 
4

'''
