from pathlib import Path

def search_notes(keyword):
    found = False
    for file_path in Path("data").glob("*.txt"):
        with open(file_path,"r",encoding="utf-8") as f:
            content = f.read()

        for number,line in enumerate(content.splitlines(),start = 1):
            if keyword.lower() in line.lower():
                found = True
                print(f"{file_path.name},第{number}行:{line}")
    if not found:
        print("没有找到相关内容")
    return found
result1 = search_notes("Python")
result2 = search_notes("Java")

print("第一次搜索：",result1)
print(f"第二次搜索：{result2}")

#word = input("请输入关键词:")
#result = search_notes(word)
#print(f"搜索是否成功:{result}")
