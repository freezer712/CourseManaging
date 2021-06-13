from design.error.MyExecption import MyException
from design.error import error_code


class NO_SUCH_COMMAND_ERROR(MyException):

    def __init__(self, command_name):
        self.error_code = error_code.error_code.NO_SUCH_COMMAND_ERROR.value
        self.error_name = error_code.error_code.NO_SUCH_COMMAND_ERROR.name
        self.command_name = command_name

    def __str__(self):
        return "error name: " + self.error_name + "\nerror code : " + str(self.error_code) + '\n\"'\
                + self.command_name + "\"不是一个有效命令\n请检查您的输入并重新输入有效命令\n输入help命令可获得帮助"