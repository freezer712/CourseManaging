# `CourseManaging`信息管理系统

[TOC]



## 1. 项目概述

`CourseManaging`信息管理系统是一个用命令行对课程进行管理的数据库系统。此系统采用面向对象的设计思想，在此系统中，用户可以对数据库进行增删改查等各类操作，同时设有`help`、`save`、`quit`等辅助指令帮助用户更好地理解和使用此系统。

代码开源地址：https://github.com/freezer712/CourseManaging

## 2. 项目目录结构介绍

![cm-1](http://freezer712.top/CourseManaging/cm-1.png)

### design

`design`是项目的总目录，包含`CourseManaging`信息管理系统的所有代码文件

#### 2.1. error

`error`目录是自定义异常的总目录，包含`CourseManaging`信息管理系统所有报错及其相关的代码文件

##### 2.1.1. MyException.py

`MyException.py` 包含`MyException`类，该类继承`Exception`类，是所有自定义异常的基类

##### 2.1.2. error_code.py

`error_code.py`包含`error_code`类，该类继承`Enum`类，包含了系统中各类报错的错误名称及错误码

##### 2.1.3. ERROR

`ERROR`目录包含8个具体报错的类文件

#### 2.2. instruction

`instruction`目录下包含信息管理系统的12个指令。

#### 2.3. main.py

项目主文件

#### 2.4. util.py

包含一些工具函数

#### 2.5. coursera_corpus.xlsx , coursera_corpus.txt , coursera_corpus

数据文件

#### 2.6. send_emails.py

用于向指定邮箱发送确认邮件

## 3. 功能（指令）介绍

### 3.1. create(c)

* 指令格式：`create--[课程名]--[课程介绍]--[课程详情]`

`create`指令可简写为`c`。`create`指令用于向数据库中添加新的课程，课程内容包括三部分：课程名，课程介绍，课程详情。其中课程名为数据库主键，不可重复，课程介绍和课程详情为非必填项，允许为空。参数数量不合要求时会报错`PARAMETER_ERROR`。

### 3.2. createn(n)

* 指令格式：`createn--[课程名1]--[课程介绍1]--[课程详情1] (--[课程名2]--[课程介绍2]--[课程详情2])*`

`createn`指令可简写为`n`。`ceraten`指令用于一次性将创建多门课程，每门课程均按照`[课程名]--[课程介绍]--[课程详情]`的顺序，，若多门课程中有若干门无法添加，不会影响其他可添加课程。参数数量不合要求时会报错`PARAMETER_ERROR`。

### 3.3. delete(d)

* 指令格式：`delete--[课程名]`

  `delete`指令可简写为`d`。`delete`指令用于删除数据库中已有的课程，若删除不存在的课程会报错。参数数量不合要求时会报错`PARAMETER_ERROR`。

### 3.4. help(h)

* 指令格式：`help`

  `help`指令可简写为`h`。`help`指令用于向用户展示帮助信息，方便用户了解本系统的使用。

### 3.5. quit(q)

* 指令格式：`quit`

`quit`指令可简写为`q`。`quit`指令用于退出`CourseManaging`信息管理系统，同时会将所有修改保存到xlsx文件中。

### 3.6. read(r)

* 指令格式：`read--[课程名]`

  `read`指令可简写为`r`。`read`指令用于查阅系统中已存在的课程的各类信息，若课程不存在则会报错。参数数量不合要求时会报错`PARAMETER_ERROR`。

### 3.7. update(u)

* 指令格式1：`update--[课程名]--[课程介绍]`

* 指令格式2：`update--[课程名]--[课程介绍]--[课程详情]`

* 指令格式3：`update--[课程名]--/intro=[课程介绍]`

* 指令格式4：`update--[课程名]--/detail=[课程详情]`

* 指令格式1：`update--[课程名]`

  `update`指令可简写为`u`。`update`指令用于更新系统中已经存在的课程的信息，包括课程介绍和课程详情。`update`指令共有4中不同的格式，用户可以根据自己的需求使用最方便的指令格式。`update`指令无法更改课程的课程名，并且如果系统中课程不存在，则会报错。参数数量不合要求时会报错`PARAMETER_ERROR`。

### 3.8. similar(s)

* 指令格式1：`similar--[课程名]--[数量]`

* 指令格式2：`similar--[课程名]--[相似度]`

  `similar`指令可简写为`s`。`similar`指令用于筛选和指定课程相似度满足一定要求的课程。其中，`similar`指令有两种格式，格式1：`similar--[课程名]--[数量]`中用于筛选和指定课程相似度最高的`[数量]`门课程，其中`[数量]`为正整数，大于等于1；格式2：`similar--[课程名]--[相似度]`用于筛选和指定课程相似度大于等于`[相似度]`的课程，其中`[相似度]`为0到1的浮点数。参数数量不合要求时会报错`PARAMETER_ERROR`, 参数范围不合要求时会报错`PARAMETER_FORMAT_ERROR`。

### 3.9. save(v)

* 指令格式：`save`

  `save`指令可简写为`v`。`save`指令用于将系统中的修改保存到xlsx文件中。

## 4. 代码实现详解

### 4.1. main.py

`main.py` 包含一个函数main(),作为项目启动的入口，main函数负责在启动开始和结束时给出相应的提示和反馈，在项目启动时，会首先调用util.py文件中的read_file()函数读取已有的课程内容，同时main函数利用while循环解析输入的指令和参数，由于课程介绍和课程详情中函数空格等一些空白字符，所以指令暂时采用--作为分隔符。当输入的指令或简写符合已定义的指令时，将生成对应的指令实例，当输入指令与所有已有指令均不匹配时，使用默认指令实例invalid_command ；判断完指令类型后统一调用指令实例的execute函数，由指令实例自行负责检验参数数量、格式是否符合要求；指令执行后返回course_list和flag，coourse_list是系统中经修改后的课程列表，flag是用来判断程序是否需要继续执行，除quit外均为True。

###  4.2 util.py

`util.py`是一个工具类，包含`show_course_info(course: list)`、`save(course_list:list)`、`read_file() -> list`、`upload_txt_data()`、`similarity(course_list:list, courseindex:int) ->list`五个工具函数。

#### 4.2.1. show_course_info(course: list)

该函数参数为list类型的course，负责格式化输出课程信息，包括课程名，课程介绍，课程详情。例如`update`，`read`等指令在展示课程信息是会统一调用此函数。无返回值。

```python
def show_course_info(course: list):
    assert len(course) == 3
    print("course name:           " + course[0])
    print("course intorduction:   " + course[1])
    print("course detail:         " + course[2])
```



#### 4.2.2.save(course_list:list)

save函数参数为course_list，负责将系统中的修改保存到coursera_corpus.xlsx文件中。该函数调用xlsxwriter包，将课程信息按照规定格式写入文件。无返回值。

```python
def save(course_list:list):
    try:
        workbook = xlsxwriter.Workbook("coursera_corpus.xlsx")
        sheet1 = workbook.add_worksheet()
        if len(course_list[0]) == 0:
            workbook.close()
            return
        index = 1
        for i in course_list[0]:
            sheet1.write_row("A" + str(index), i)
            index += 1
        workbook.close()
    except FileCreateError as fe:
        print(fe)
    except PermissionError as pe:
        print(pe)
```



#### 4.2.3. read_file() -> list

read_file()函数用于读取`coursera_corpus.xlsx`，将文件中的课程信息读入系统中并以列表的形式保存.返回值为course_list:list。

```python
def read_file() -> list:
    workbook = xlrd.open_workbook("coursera_corpus.xlsx")
    sheet1 = workbook.sheet_by_index(0)
    total_rows = sheet1.nrows
    course_list = [[], []]

    for i in range(total_rows):
        temp = sheet1.row_values(rowx=i,start_colx=0,end_colx=3)
        course_list[0].append(temp)
        course_list[1].append(temp[0])

    return course_list

```



#### 4.2.4. upload_txt_data()

`upload_text_data()`用于解析`coursera_corpus.txt`成规定格式course_list，并调用save()函数将course_list数据保存到`coursera_corpus.xlsx`中。无返回值。

```python
def upload_txt_data():
    with open("coursera_corpus.txt",encoding="utf-8") as f:
        lines = f.readlines()
    data = [[], []]
    for i in lines:
        temp = i.split("	")
        for i in range(len(temp)):
            temp[i] = temp[i].strip()
        assert len(temp) == 3
        data[0].append(temp)
        data[1].append(temp[0])
    f.close()
    save(data)
```



#### 4.2.5. similarity(course_list:list, courseindex:int) ->list

该函数用于计算course_list列表中与制定课程的相似度。计算是通过调用nltk包的功能来实现将所有字母转为小写，分词，分离符号，去掉停用词，过滤符号，单词词干化，去掉低频词，应用gensim做课程相似度实验。返回内容为课程index和相似度等。

```python
def similarity(course_list:list, courseindex:int) ->list:
    courses = [i[0] + " " + i[1] + " " + i[2] for i in course_list[0]]
    courses = [ i.encode("utf-8") for i in courses]
    courses_name = course_list[1]
    texts_tokenized = [[word.lower() for word in word_tokenize(document.decode('utf-8'))] for document in courses]
    english_stopwords = stopwords.words('english')
    texts_filtered_stopwords = [[word for word in document if not word in english_stopwords]
                                for document in texts_tokenized]
    english_punctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%']
    texts_filtered = [[word for word in document if not word in english_punctuations] for document in
                      texts_filtered_stopwords]
    st = LancasterStemmer()
    texts_stemmed = [[st.stem(word) for word in docment] for docment in texts_filtered]
    all_stems = sum(texts_stemmed, [])
    stems_once = set(stem for stem in set(all_stems) if all_stems.count(stem) == 1)
    texts = [[stem for stem in text if stem not in stems_once] for text in texts_stemmed]
    #logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    corpus_tfidf = tfidf[corpus]
    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=10)
    index = similarities.MatrixSimilarity(lsi[corpus])
    ml_course = texts[courseindex]
    ml_bow = dictionary.doc2bow(ml_course)
    ml_lsi = lsi[ml_bow]
    sims = index[ml_lsi]
    sort_sims = sorted(enumerate(sims), key=lambda item: -item[1])
    return [courses_name[courseindex], sort_sims]
```



### 4.3. send_emails.py

该程序通过调用`smtplib`和`email`库来实现向指定邮箱发送验证码的功能，用于验证删库跑路（bonus features）操作。

### 4.4. instruction

`instruction`为指令目录，每个指令分别负责实现某个指令或者功能

#### 4.4.1. instructions

`instructions`类是基类，包括long_name,short_name两个属性和execute一个函数。当衍生类execute未实现时，会调用基类的execute方法，报错`UNIMPLEMENT_ERROR`。

```python
from design.error.ERROR.UNIMPLEMENT_ERROR import UNIMPLEMENT_ERROR

class instruction:

    def execute(self, course_list: list,args=None):
        try:
            raise UNIMPLEMENT_ERROR
        except:
            print(UNIMPLEMENT_ERROR)
        return course_list, True
```



#### 4.4.2. invalid_command

当指令没有定义时，执行execute会调动invalid_command的execute函数，报错`NO_SUCH_COMMAND_ERROR`。

```python
from design.instruction.instructions import instruction
from design.error.ERROR.NO_SUCH_COMMAND_ERROR import NO_SUCH_COMMAND_ERROR
from design.error.ERROR.NO_INPUT_ERROR import NO_INPUT_ERROR
class invalid_command(instruction):

    def __init__(self,isEmpty:bool):
        self.long_name = "invalid"
        self.short_name = "i"
        self.isEmpty = isEmpty

    def execute(self, course_list: list, args=None):
        try:
            if self.isEmpty:
                raise NO_INPUT_ERROR
            else:
                raise NO_SUCH_COMMAND_ERROR(args[0])
        except NO_SUCH_COMMAND_ERROR as e:
            print(e)
        except NO_INPUT_ERROR as ie:
            print(ie)
        finally:
            return course_list, True
```



#### 4.4.3.其他

每个指令会首先根据自己的指令内容检验参数是否符合要求，并根据情况报错`PARAMETER_ERROR`、`NO_SUCH_COURSE_ERROR`、`COURSE_EXISTED_ERROR`、`PARAMETER_FORMAT_ERROR`等。

再分别根据参数执行指令内容。

```python
from design.instruction.instructions import instruction
from design.error.ERROR.NO_SUCH_COURSE_ERROR import NO_SUCH_COURSE_ERROR
from design.error.ERROR.PARAMETER_ERROR import PARAMETER_ERROR
from design.util import show_course_info

class read(instruction):

    def __init__(self):
        self.long_name = "read"
        self.short_name = "r"

    def execute(self, course_list: list, args=None):
        try:
            if len(args) != 1:
                raise PARAMETER_ERROR(self.long_name)
            elif args[0] not in course_list[1]:
                raise NO_SUCH_COURSE_ERROR(args[0])
            index = course_list[1].index(args[0])
            show_course_info(course_list[0][index])
        except PARAMETER_ERROR as pe:
            print(pe)
        except NO_SUCH_COURSE_ERROR as ce:
            print(ce)
        finally:
            return course_list, True

```





```python
from design.instruction.instructions import instruction
from design.error.ERROR.PARAMETER_ERROR import PARAMETER_ERROR
from design.error.ERROR.NO_SUCH_COURSE_ERROR import NO_SUCH_COURSE_ERROR
class delete(instruction):

    def __init__(self):
        self.long_name = "delete"
        self.short_name = "d"

    def execute(self, course_list: list, args=None):
        try:
            if len(args) != 1:
                raise PARAMETER_ERROR(self.long_name)
            elif args[0] not in course_list[1]:
                raise NO_SUCH_COURSE_ERROR(args[0])
            index = course_list[1].index(args[0])
            del course_list[0][index]
            del course_list[1][index]
            print('The course \"' + args[0] + '\" is deleted successfully.')
        except PARAMETER_ERROR as pe:
            print(pe)
        except NO_SUCH_COURSE_ERROR as ce:
            print(ce)
        finally:
            return course_list, True
```



### 4.5. error

`MyException`是自定义异常的基类

`error_code`是错误码

`ERROR`是各类自定义的错误（异常），分别负责在不同的情况向用户输出各类错误信息。

```python
class MyException(Exception):


    def __str__(self):
        return "自定义异常"
```



```python
from design.error.MyExecption import MyException
from design.error import error_code


class NO_SUCH_COURSE_ERROR(MyException):

    def __init__(self, course_name):
        self.error_code = error_code.error_code.NO_SUCH_COURSE_ERROR.value
        self.error_name = error_code.error_code.NO_SUCH_COURSE_ERROR.name
        self.course_name = course_name

    def __str__(self):
        return "error name: " + self.error_name + "\nerror code : " + str(self.error_code) + "\n"\
                + '课程\"' +self.course_name + '\"不存在\n请输入有效的课程名'
```



## 5. bonus features

~~删库跑路是程序员最后的倔强~~。虽然本系统指令格式与正常的linux等不一样，但是不妨将`rm -rf /*` 作为固定指令用于~~删库跑路~~清除数据库所有数据。同时，作为特殊操作为防止失误，~~删库跑路~~清除数据库所有数据指令会有两重验证，分别为手输入“`I confirm to perform this operation.`” 全文和向邮箱发送验证码。验证均只有一次机会，验证失败程序会自动退出。

```python
import time

from design.instruction.instructions import instruction
from design.instruction.save import save_op
from design.send_emails import send_mail


class run(instruction):

    def __init__(self):
        self.long_name = "delete and run"
        self.short_name = "x"
        self.tips = "删库跑路！"


    def execute(self, course_list: list,args=None):
        print("删库有风险，跑路需谨慎。")
        print("请完整输入 “I confirm to perform this operation.” 确认您的操作: ")
        flag = False

        confirm = input()
        if confirm == "I confirm to perform this operation.":
            print("已确认删库跑路操作!")
            for j in range(3):
                email = input("请输入你的邮箱验证本操作: ")
                if email.find("@") == -1:
                    print("格式错误.")
                    continue
                else:
                    code = send_mail(email)
                    print("验证码已发送到邮箱.")
                    time.sleep(1)
                    input_code = input("请输入验证码：")
                    if input_code == code:
                        print("验证成功.")
                        flag = True
                        break
                    else:
                        print("验证失败.")
                        flag = False
                        break

            if flag:
                print(self.tips)
                print("正在删库中......")
                course_list = [[], []]
                save_op().execute(course_list=course_list, args=None)
                print("删库成功，请及时跑路或主动拨打110自首！")
                return course_list, False
        else:
            print("确认失败.")

        return course_list, False
```

## 6. 使用流程演示

### 6.0. 启动

![cm-2](http://freezer712.top/CourseManaging/cm-2.png)

### 6.1.  create

![cm-3](http://freezer712.top/CourseManaging/cm-3.png)

### 6.2. createn

![cm-4](http://freezer712.top/CourseManaging/cm-4.png)

### 6.3. delete

![cm-5](http://freezer712.top/CourseManaging/cm-5.png)

### 6.4. read

![cm-6](http://freezer712.top/CourseManaging/cm-6.png)

### 6.5. update

![cm-7](http://freezer712.top/CourseManaging/cm-7.png)

### 6.6. similar

![cm-8](http://freezer712.top/CourseManaging/cm-8.png)

### 6.7. save

![cm-9](http://freezer712.top/CourseManaging/cm-9.png)



![cm-10](http://freezer712.top/CourseManaging/cm-10.png)

### 6.8. quit

![cm-12](http://freezer712.top/CourseManaging/cm-12.png)

### 6.9. rm -rf /*

![cm-14](http://freezer712.top/CourseManaging/cm-14.png)

### 6.10. help

![cm-13](http://freezer712.top/CourseManaging/cm-13.png)

### 6.11. 其他

![cm-15](http://freezer712.top/CourseManaging/cm-15.png)