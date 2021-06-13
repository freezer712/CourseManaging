from design.instruction.instructions import instruction
from design.error.ERROR.PARAMETER_ERROR import PARAMETER_ERROR
from design.instruction.create import create
class createn(instruction):

    def __init__(self):
        self.long_name = "createn"
        self.short_name = "n"

    def execute(self, course_list: list, args=None):
        try:
            if (len(args) % 3) != 0:
                raise PARAMETER_ERROR(self.long_name)
            c = create()
            for i in range(0,len(args),3):
                c.execute(args=args[i:i+3], course_list=course_list)
        except PARAMETER_ERROR as pe:
            print(pe)
        finally:
            return course_list, True