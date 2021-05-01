from django.shortcuts import render, redirect, HttpResponse
from app01 import sqlheper
import pymysql
import json

def classes(request):
    #创建连接
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
    #创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    #执行SQL，并返回受影响函数
    cursor.execute("select id, title from class")
    class_list = cursor.fetchall()
    #关闭游标
    cursor.close()
    #关闭连接
    conn.close()

    return render(request,'classes.html',{'class_list':class_list})

def add_class(request):
    if request.method == "GET":
        return render(request, 'add_class.html')
    else:
        print(request.POST)
        v = request.POST.get("title")
        if len(v) > 0:
            conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
            # 创建游标
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
            # 执行SQL，并返回受影响函数
            cursor.execute("insert into class(title) values(%s)", [v, ])
            conn.commit()
            # 关闭游标
            cursor.close()
            # 关闭连接
            conn.close()
            return redirect(' /classes/')
        else:
            return render(request, 'add_class.html',{'msg':'班级名称不能够为空'})

def del_class(request):
    nid = request.GET.get('nid')
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行SQL，并返回受影响函数
    cursor.execute("delete from class where id=%s",[nid,])
    conn.commit()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()
    return  redirect('/classes/')

def edit_class(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回受影响函数
        cursor.execute("select id, title from class where id = %s", [nid, ])
        result = cursor.fetchone()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        print(result)
        return render(request, 'edit_class.html',{'result':result})
    else:
        nid = request.GET.get('nid')
        title = request.POST.get('title')

        conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回受影响函数
        cursor.execute("update class set title = %s where id = %s", [title, nid,])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()

        return redirect(('/classes'))

def students(request):
    """
    学生列表
    :param request:封装请求相关的所有信息
    :return:
    """

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
    # 创建游标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 执行SQL，并返回受影响函数
    cursor.execute("select student.id,student.name,student.class_id,class.title from student left JOIN class on student.class_id = class.id")
    student_list = cursor.fetchall()
    # 关闭游标
    cursor.close()
    # 关闭连接
    conn.close()

    class_list = sqlheper.get_list('select id,title from class', [])

    return render(request,'students.html',{'student_list':student_list,'class_list':class_list})

def add_student(request):
    if request.method == "GET":
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回受影响函数
        cursor.execute("select id, title from class")
        class_list = cursor.fetchall()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()

        return  render(request,'add_student.html',{'class_list':class_list})
    else:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        #连接MySQL
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='cjly', passwd='cjly0915', db='django')
        # 创建游标
        cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
        # 执行SQL，并返回受影响函数
        cursor.execute('insert into student(name,class_id) value(%s,%s)',[name, class_id, ])
        conn.commit()
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()
        return  redirect('/students/')

def del_student(request):
    nid = request.GET.get('nid')
    sqlheper.modify('delete from student where id=%s', [nid, ])
    return redirect('/students/')

def edit_student(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        class_list = sqlheper.get_list("select id,title from class", [])
        current_student_info = sqlheper.get_one('select id,name,class_id from student where id=%s', [nid, ])
        return render(request, "edit_student.html",{'class_list':class_list,'current_student_info':current_student_info})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        sqlheper.modify('update student set name=%s,class_id=%s where id=%s', [name, class_id, nid])
        return redirect('/students/')

# ################## 对话框 ################# #

def modal_add_class(request):
    title = request.POST.get('title')
    if len(title) > 0:
        sqlheper.modify('insert into class(title) values(%s)', [title, ])
        return HttpResponse('ok')
    else:
        return HttpResponse('班级标题不能为空')


    # if len(title) > 0:
    #     sqlheper.modify('insert into class(title) values(%s)', [title, ])
    #     # 刷新原因：Form表单提交特性
    #     return redirect('/classes/')
    #     # return HttpResponse('ok')
    # else:
    #     #页面不要刷新，提示错误信息
    #     pass

def modal_edit_class(request):
    ret = {'status' : True, 'message': None}
    try:
        nid = request.POST.get('nid')
        content = request.POST.get('content')
        sqlheper.modify('update class set title=%s where id=%s', [content, nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = "处理异常"

    return HttpResponse(json.dumps(ret))

def modal_add_student(request):
    ret = {'status':True,'message':None}
    try:
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        sqlheper.modify('insert into student(name,class_id) values(%s,%s)', [name, class_id, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))

def modal_edit_student(request):
    ret = {'status':True,'message':None}
    try:
        nid = request.POST.get('nid')
        name = request.POST.get('name')
        class_id = request.POST.get('class_id')
        sqlheper.modify('update student set name=%s,class_id=%s where id=%s', [name, class_id, nid, ])
    except Exception as e:
        ret['status'] = False
        ret['message'] = str(e)
    return HttpResponse(json.dumps(ret))

#多对多，易老师表展示
def teacher(request):
    # teacher_list = sqlheper.get_list('select id,name from teacher',[])
    teacher_list = sqlheper.get_list("""
        SELECT teacher.id as tid,teacher.name,class.title FROM teacher
        LEFT JOIN teacher2class ON teacher.id = teacher2class.teacher_id
        LEFT JOIN class ON class.id = teacher2class.class_id
    """, [])

    result = {}
    for row in teacher_list:
        tid = row['tid']
        if tid in result:
            result[tid]['titles'].append(row['title'])
        else:
            result[tid] = {'tid': row['tid'], 'name': row['name'], 'titles': [row['title'], ]}

    return render(request,'teacher.html',{'teacher_list':result.values()})

def add_teacher(request):
    if request.method == "GET":
        class_list = sqlheper.get_list('select id,title from class',[])
        return render(request,'add_teacher.html',{'class_list' : class_list})
    else:
        name = request.POST.get('name')
        #老师表中添加一条数据
        teacher_id = sqlheper.create('insert into teacher(name) values(%s)',[name,])
        #老师和班级关系表中插入数据
        #['2', '3', '4', '5', '6', '7']
        #获取当前添加老师的id

        class_ids = request.POST.getlist('class_ids')
        #连接多次提交多次关闭多次
        # for cls_id in class_ids:
        #     sqlheper.modify('insert into teacher2class(teacher_id,class_id) values(%s,%s)',[teacher_id,cls_id])

        #连接一次提交多次再关闭一次
        # obj = sqlheper.SqlHelper()
        # for cls_id in class_ids:
        #     obj.modify('insert into teacher2class(teacher_id,class_id) values(%s,%s)',[teacher_id,cls_id])
        # obj.close()

        #连接一次并且提交一次再关闭
        obj = sqlheper.SqlHelper()
        data_list = []
        for cls_id in class_ids:
            temp = (teacher_id,cls_id)
            data_list.append(temp)
        obj.multiple_modify('insert into teacher2class(teacher_id,class_id) values(%s,%s)',data_list)
        obj.close()
        return redirect('/teacher/')

def edit_teacher(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj = sqlheper.SqlHelper()
        teacher_info = obj.get_one('select id,name from teacher where id =%s', [nid,])
        class_id_list = obj.get_list('select class_id from teacher2class where teacher_id=%s',[nid,])
        class_list = obj.get_list('select id,title from class',[])
        obj.close()

        print("当前老师信息",teacher_info)
        print("当前老师任教班级id",class_id_list)
        temp = []
        for i in class_id_list:
            temp.append(i['class_id'])
        print("所有班级",class_list)
        # return HttpResponse('...')
        return render(request,'edit_teacher.html',{'teacher_info' : teacher_info,'class_id_list' : temp,'class_list' : class_list,})
    else:
        nid = request.GET.get('nid')
        name = request.POST.get('name')
        class_ids = request.POST.getlist('class_ids')
        obj = sqlheper.SqlHelper()
        #更新老师表
        obj.modify('update teacher set name=%s where id=%s',[name,nid])
        #更新老师和班级关系表
        #1.先把当前老师和班级的对应关系删除，然后再添加
        obj.modify('delete from teacher2class where teacher_id=%s',[nid,])
        data_list = []
        for cls_id in class_ids:
            temp = (nid, cls_id)
            data_list.append(temp)
        #  data_list = [(nid, item) for item in class_ids]
        obj.multiple_modify('insert into teacher2class(teacher_id,class_id) values(%s,%s)', data_list)
        obj.close()
        return redirect('/teacher/')

def get_all_class(request):
    import time
    time.sleep(1)
    obj = sqlheper.SqlHelper()
    class_list = obj.get_list('select id,title from class',[])
    obj.close()
    return HttpResponse(json.dumps(class_list))

def modal_add_teacher(request):
    ret = {'status' : True, 'message' : None}
    try:
        name = request.POST.get('name')
        class_id_list = request.POST.getlist('class_id_list')

        teacher_id = sqlheper.create('insert into teacher(name) values(%s)', [name, ])

        obj = sqlheper.SqlHelper()
        data_list = []
        for cls_id in class_id_list:
            temp = (teacher_id, cls_id)
            data_list.append(temp)
        obj.multiple_modify('insert into teacher2class(teacher_id,class_id) values(%s,%s)', data_list)
        obj.close()
    except Exception as e:
        ret['status'] = False
        ret['message'] = "处理失败"
    return HttpResponse(json.dumps(ret))

def layout(request):
    return render(request,'layout.html');




























def test(request):
    return render(request,'test.html')





















