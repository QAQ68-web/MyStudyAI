from pathlib import Path
keyword = input("请输入关键词：")
found = False

for file_path in Path("data").glob("*.txt"):
    
    with open(file_path,"r",encoding="utf-8") as f:
        content = f.read()

    for number,line in enumerate(content.splitlines(),start = 1):
        if(keyword.lower() in line.lower()):
            found = True
            print(f"{file_path.name},第{number}行：{line}")
if not found:
    print("没有找到相关内容")
