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