def missing_number(arr,n):
    expected_sum = n * (n+1)//2
    actual_sum = 0

    for num in arr:
        actual_sum += num
    
    return expected_sum - actual_sum
print(missing_number([1,2,3,5],5))