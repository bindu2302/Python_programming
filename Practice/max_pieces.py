def max_pieces(rope_length,total_length):
    left = 1
    right = max(rope_length)
    max_pieces = 0

    while left <= right:
        mid = (left+right)//2
        pieces = sum(length//mid for length in rope_length)

        if pieces >= total_length:
            max_pieces = mid
            left = mid+1
        else:
            right = mid-1
    return max_pieces

rope_length = [9,7,5,11]
required_length = 6
print(max_pieces(rope_length,required_length))
       