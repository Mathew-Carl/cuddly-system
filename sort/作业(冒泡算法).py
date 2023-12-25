#冒泡排序算法

def bubbling_sort(letters):
    letters = list(letters)
    for i in range(len(letters)-1):#总共需要的循环次数(可以认为每次比较出最大的数字)
        exchance = False#标志
        for n in range(len(letters)-1-i):#n是第N个数字,len(nums)-1-i是剩余多少个数字比较
            if ord(str(letters[n])) > ord(str(letters[n+1])):
                letters[n], letters[n+1] = letters[n+1], letters[n]
        if not exchance:#简化
            return letters
    return letters
def bulu_sort(nums):
    nums = list(map(int, nums))
    for i in range(len(nums)-1):#总共需要的循环次数(可以认为每次比较出最大的数字)
        exchance = False#标志
        for n in range(len(nums)-1-i):#n是第N个数字,len(nums)-1-i是剩余多少个数字比较
            if nums[n] > nums[n+1]:
                nums[n], nums[n+1] = nums[n+1], nums[n]
        if not exchance:#简化
            return nums
    return nums
select = input("请选择您要输入的项目(数字或英文,区分大小写)")
if select == "数字":
    nums = input("请输入您要输入的数字,请用空格隔开").split(" ")
    print(bulu_sort(nums))
elif select == "英文":
    letters = input("请输入您要输入的英文并用空格隔开").split(" ")
    print(bubbling_sort(letters))
else:
    print("请输入正确的格式")
        

        

