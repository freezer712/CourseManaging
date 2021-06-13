from design.instruction.instructions import instruction
from design.error.ERROR.NO_SUCH_COURSE_ERROR import NO_SUCH_COURSE_ERROR
from design.error.ERROR.PARAMETER_ERROR import PARAMETER_ERROR
from design.util import show_course_info


class update(instruction):

    def __init__(self):
        self.long_name = "update"
        self.short_name = "u"

    def execute(self, course_list: list, args=None):
        try:
            if args[0] not in course_list[1]:
                raise NO_SUCH_COURSE_ERROR(args[0])

            index = course_list[1].index(args[0])

            if args[1].startswith("/intro="):
                if len(args) != 2:
                    raise PARAMETER_ERROR(self.long_name)
                course_list[0][index][1] = args[1][7::]
            elif args[1].startswith("/detail="):
                if len(args) != 2:
                    raise PARAMETER_ERROR(self.long_name)
                course_list[0][index][2] = args[1][8::]
            elif len(args) == 3:
                course_list[0][index][1] = args[1]
                course_list[0][index][2] = args[2]
            elif len(args) == 2:
                course_list[0][index][1] = args[1]
            else:
                raise PARAMETER_ERROR(self.long_name)
            show_course_info(course_list[0][index])

        except PARAMETER_ERROR as pe:
            print(pe)
        except NO_SUCH_COURSE_ERROR as ce:
            print(ce)
        finally:
            return course_list, True



