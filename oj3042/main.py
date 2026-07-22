"""หารจำนวนที่ตัวเลขหาร10ลงตัว"""
def main():
    """คำนวณ"""
    num = int(input())
    newnum = ((num//10)*10)+10
    while newnum > 0:
        newnum -= 10
        print(newnum, end=" ")
main()
