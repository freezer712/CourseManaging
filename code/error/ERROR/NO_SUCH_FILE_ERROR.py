from design.error.MyExecption import MyException
from design.error import error_code


class NO_SUCH_FILE_ERROR(MyException):

    def __init__(self,file_name):
        self.error_code = error_code.error_code.NO_SUCH_FILE_ERROR.value
        self.error_name = error_code.error_code.NO_SUCH_FILE_ERROR.name
        self.file_name = file_name

    def __str__(self):
        return "error name: " +self.error_name+ "\nerror code : " + str(self.error_code) + "\n\"" \
               + self.file_name + "\"不在指定目录下\n请检查文件路径是否正确"

