

def find_frequency_positions(transmissions, target_code):
    def helper(is_first):
        low = 0
        high = len(transmissions)-1
        result = -1

        while low <= high:
            mid = low + (high-low)//2

            if transmissions[mid] == target_code:
                result = mid
                if is_first:
                    high = mid -1
                else:
                    low = mid + 1
            elif transmissions[mid]>target_code:
                high = mid - 1
            else:
                low = mid + 1
        return result
    return (helper(True), helper(False))

print(find_frequency_positions([5,7,7,8,8,10], 8))
print(find_frequency_positions([5,7,7,8,8,10], 6))
print(find_frequency_positions([], 0))

