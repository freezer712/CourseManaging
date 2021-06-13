from design.error.MyExecption import MyException
from design.error import error_code


class COURSE_EXISTED_ERROR(MyException):

    def __init__(self,course_name):
        self.error_code = error_code.error_code.COURSE_EXISTED_ERROR.value
        self.error_name = error_code.error_code.COURSE_EXISTED_ERROR.name
        self.course_name = course_name

    def __str__(self):
        return "error name: " +self.error_name+ "\nerror code : " + str(self.error_code) \
        + "\n" + '课程 \"' + self.course_name + '\"已经存在\n请重命名您的课程或直接对已存在课程操作'