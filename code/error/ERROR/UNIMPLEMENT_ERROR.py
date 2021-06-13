from design.error.MyExecption import MyException
from design.error import error_code


class UNIMPLEMENT_ERROR(MyException):

    def __init__(self):
        self.error_code = error_code.error_code.UNIMPLEMENT_ERROR.value
        self.error_name = error_code.error_code.UNIMPLEMENT_ERROR.name

    def __str__(self):
        return "error name: " + self.error_name + "\nerror code : " + str(self.error_code) + "\n"\
                + '该指令尚未实现.'