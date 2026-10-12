from pathlib import Path

def search_notes(keyword):
    results = []
    for file_path in Path("data").glob("*.txt"):
        with open(file_path,"r",encoding="utf-8") as f:
            content = f.read()

        for number,line in enumerate(content.splitlines(),start = 1):
            if keyword.lower() in line.lower():
                note1 = {
			"file":file_path.name,
			"line":number,
			"content":line
                        }
                results.append(note1)
    return results
#result1 = search_notes("Python")
#result2 = search_notes("Java")

#print("第一次搜索：",result1)
#print(f"第二次搜索：{result2}")

word = input("请输入关键词:")
results = search_notes(word)
if results:
    print("找到以下内容：")

    for item in results:
        print(f"{item['file']} 第{item['line']}行:{item['content']}")

else:
    print("没有找到相关内容")
