#测试脚本

v = [
    {'tid': 1, 'name': '日天', 'title': '全栈55期'},
    {'tid': 1, 'name': '日天', 'title': '全栈666期'},
    {'tid': 2, 'name': '日地', 'title': '黑客来了'},
    {'tid': 2, 'name': '日地', 'title': '全栈100期'},
    {'tid': 3, 'name': '方少伟', 'title': '全栈55期'},
    {'tid': 3, 'name': '方少伟', 'title': '全栈666期'},
    {'tid': 3, 'name': '方少伟', 'title': '黑客来了'}
]

result = {
    # 1: {'tid': 1, 'name': '日天', 'titles': ['全栈55期','全栈666期']},
    # 2: {'tid': 2, 'name': '日地', 'titles': ['黑客来了','全栈100期']},
    # 3: {'tid': 3, 'name': '方少伟', 'title': ['全栈55期','全栈666期','黑客来了']}
}

for row in v:
    tid = row['tid']
    if tid in result:
        result[tid]['titles'].append(row['title'])
    else:
        result[tid] = {'tid':row['tid'],'name':row['name'],'titles':[row['title'],]}

for item in result.values():
    print(item)


teacher_info = [{'id': 4, 'name': '李杰'}]
print(teacher_info[0].name)