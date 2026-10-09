print("Hello,MyStudyAI!")
with open("data/notes.txt","r",encoding="utf-8") as f:
    content = f.read()
keyword = input("请输入关键词：")
found = False
for number,line in enumerate(content.splitlines(),start = 1):
    if(keyword.lower() in line.lower()):
        found = True
        print(f"第{number}行：{line}")
if(found == False):
    print("没有找到相关内容")
