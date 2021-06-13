from design.instruction.instructions import instruction
from design.error.ERROR.COURSE_EXISTED_ERROR import COURSE_EXISTED_ERROR
from design.error.ERROR.PARAMETER_ERROR import PARAMETER_ERROR


class create(instruction):

    def __init__(self):
        self.long_name = "create"
        self.short_name = "c"

    def execute(self, course_list: list, args=None):
        if args is None:
            args = []
        try:
            if args[0] in course_list[1]:
                raise COURSE_EXISTED_ERROR(args[0])
            elif len(args) != 3:
                raise PARAMETER_ERROR(self.long_name)
            temp = [args[0],args[1],args[2]]
            course_list[0].append(temp)
            course_list[1].append(args[0])
            print('The course \"' + args[0] + '\" is created successfully.')
        except COURSE_EXISTED_ERROR as e:
            print(e)
        except PARAMETER_ERROR as pe:
            print(pe)
        finally:
            return course_list, True

