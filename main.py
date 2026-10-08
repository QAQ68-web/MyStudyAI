print("Hello,MyStudyAI!")
with open("data/notes.txt","r",encoding="utf-8") as f:
    content = f.read()
keyword = input("请输入关键词：")
for line in content.splitlines():
    if(keyword.lower() in line.lower()):
        print(line)
