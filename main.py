from pathlib import Path

def search_notes(question):

    results = []

    keywords = question.split()

    for file_path in Path("data").glob("*.txt"):

        with open(file_path,"r",encoding="utf-8") as f:
            content = f.read()

        for number,line in enumerate(content.splitlines(),start = 1):

            times = 0

            for keyword in keywords:
                if keyword.lower() in line.lower():
                    times += 1

            if times > 0:
                note1 = {
			"file":file_path.name,
			"line":number,
			"content":line,
			"得分":times
                        }
                results.append(note1)
    results = sorted(
        results,
        key = lambda item: item["得分"],
        reverse = True
        )

    return results

word = input("请输入问题:")
results = search_notes(word)

if results:
    print("找到以下内容：")

    for item in results:
        print(
	    f"{item['file']} 第{item['line']}行:"
	    f"{item['content']}  得分：{item['得分']}"
	    )

else:
    print("没有找到相关内容")

