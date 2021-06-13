from design.error.MyExecption import MyException
from design.error import error_code


class NO_INPUT_ERROR(MyException):

    def __init__(self):
        self.error_code = error_code.error_code.NO_INPUT_ERROR.value
        self.error_name = error_code.error_code.NO_INPUT_ERROR.name

    def __str__(self):
        return "error name: " + self.error_name + "\nerror code : " + str(self.error_code) + "\n"\
                + '无有效输入\n请在控制台输入命令\n输入help命令可获得帮助'