from design.instruction.instructions import instruction
from design.error.ERROR.NO_SUCH_COMMAND_ERROR import NO_SUCH_COMMAND_ERROR
from design.error.ERROR.NO_INPUT_ERROR import NO_INPUT_ERROR
class invalid_command(instruction):

    def __init__(self,isEmpty:bool):
        self.long_name = "invalid"
        self.short_name = "i"
        self.isEmpty = isEmpty

    def execute(self, course_list: list, args=None):
        try:
            if self.isEmpty:
                raise NO_INPUT_ERROR
            else:
                raise NO_SUCH_COMMAND_ERROR(args[0])
        except NO_SUCH_COMMAND_ERROR as e:
            print(e)
        except NO_INPUT_ERROR as ie:
            print(ie)
        finally:
            return course_list, True
