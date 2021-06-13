from design.instruction.instructions import instruction
from design.util import save
class save_op(instruction):

    def __init__(self):
        self.long_name = "save"
        self.short_name = "v"

    def execute(self, course_list: list, args=None):
        save(course_list)
        print("保存成功！")
        return course_list, True