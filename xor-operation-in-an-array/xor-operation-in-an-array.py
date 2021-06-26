class Solution:
    def xorOperation(self, n: int, start: int) -> int:

        def is_even(i):
            return i % 2 == 0

        def is_odd(i):
            return i % 2 == 1

        ans = 0

        # if n is odd and start is odd, then the last bit of ans will be 1
        # otherwise, the last bit of ans is 0
        ans ^= is_odd(n) and is_odd(start)

        # now we can only consider the right-shifted number sequence
        # consider the case 5, 6, 7, 8, 9, 10
        # (6, 7) is a pair which produces a 1, same as (8, 9)

        # thus, we need to take care of the 5
        new_start = start // 2
        ans ^= new_start << 1 if is_odd(new_start) else 0

        # and we have to take care of the 10
        new_end = new_start + n - 1
        ans ^= new_end << 1 if is_even(new_end) else 0

        # finally we have to calculate how many pairs
        num_pairs = n // 2 - int(is_even(n) and is_odd(new_start))
        ans ^= is_odd(num_pairs) << 1

        return ans