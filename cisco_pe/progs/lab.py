digits = ['1111110',  # 0
          '0110000',  # 1
          '1101101',  # 2
          '1111001',  # 3
          '0110011',  # 4
          '1011011',  # 5
          '1011111',  # 6
          '1110000',  # 7
          '1111111',  # 8
          '1111011',  # 9
          ]

x="""
  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###
"""

# nums = [x[i:i+30] for i in range(0, len(x), 30)]
nums = x.split("\n")
nums = nums[1:-1]

for ind, line in enumerate(nums):
    nums[ind] = [line[i: i+3] for i in range(0,len(line), 4)]

#print(nums)
def print_number(num):
    for line in nums:
        res = ""
        for i in num:
            if int(i) == 0:
                res += line[-1] + " "
                continue
            res += line[int(i) - 1] + " "
        print(res)



print_number("1234564546545454654654848")

# print_number(int(input("Enter the number you wish to display: ")))
