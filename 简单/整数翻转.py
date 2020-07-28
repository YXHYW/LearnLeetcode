class Solution:   
    def reverse(self, x: int) -> int:
        if -2147483648 < x < 2147483647:
            str_x = str(x)
            if str_x[0] != "-":
                x = int(str_x[::-1])
            else:
                x = int(str_x[:0:-1])
                x = -x
            if -2147483648 < x < 2147483647:
                return x
            else:
                return 0
        else:
            return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(1534236469))