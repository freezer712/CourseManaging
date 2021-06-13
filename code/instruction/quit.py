from design.instruction.instructions import instruction
from design.util import save

class quit(instruction):

    def __init__(self):
        self.long_name = "quit"
        self.short_name = "q"

    def execute(self, course_list: list, args=None):
        print("感谢您的使用!")
        save(course_list)
        return course_list, False
