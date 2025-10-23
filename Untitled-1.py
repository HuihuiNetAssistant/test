import sys

# /e:/github/test/test/Untitled-1.py

def add_numbers(values):
    total = 0.0
    for v in values:
        total += float(v)
    return total

def main():
    if len(sys.argv) > 1:
        try:
            result = add_numbers(sys.argv[1:])
        except ValueError:
            print("错误：所有参数必须是数字")
            sys.exit(1)
        print(result)
    else:
        try:
            s = input("请输入要相加的数字，用空格分隔：")
            if not s.strip():
                print("没有输入。")
                return
            result = add_numbers(s.split())
            print(result)
        except ValueError:
            print("错误：输入必须是数字")

if __name__ == "__main__":
    main()