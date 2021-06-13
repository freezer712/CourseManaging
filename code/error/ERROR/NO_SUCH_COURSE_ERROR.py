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