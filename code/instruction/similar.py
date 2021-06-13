from design.instruction.instructions import instruction
from design.util import similarity
from design.error.ERROR.PARAMETER_ERROR import PARAMETER_ERROR
from design.error.ERROR.NO_SUCH_COURSE_ERROR import NO_SUCH_COURSE_ERROR
from design.error.ERROR.PARAMETER_FORMAT_ERROR import PARAMETER_FORMAT_ERROR


import re

class similar(instruction):

    def __init__(self):
        self.long_name = "similar"
        self.short_name = "s"

    def execute(self, course_list: list, args=None):
        try:
            if len(args) != 2:
                raise PARAMETER_ERROR(self.long_name)
            elif args[0] not in course_list[1]:
                raise NO_SUCH_COURSE_ERROR(args[0])
            index = course_list[1].index(args[0])
            course_name, sim_list = similarity(course_list, index)
            suitable = []
            flag = False
            if args[1].isdigit():
                args[1] = int(args[1])
                if args[1] >=1:
                    length = min(args[1], len(sim_list))
                    suitable = sim_list[0:length:]
                else:
                    flag = True
            elif is_number(args[1]):
                args[1] = float(args[1])
                if args[1] >= 0.0 and args[1] <= 1.0:
                    for i in sim_list:
                        if i[1] >= args[1]:
                            suitable.append(i)
                        else:
                            break
                else:
                    flag = True
            else:
                flag = True

            if flag:
                raise PARAMETER_FORMAT_ERROR(self.long_name)

            print("course name: " + course_name)
            if len(suitable) == 0:
                print("sorry, no course meets your requirements.")
            else:
                print("similarity | course index | course name")
                for i in suitable:
                    print("{:.7f}  |   {:<5d}      | {}".format(i[1], i[0], course_list[0][i[0]][0]))



        except PARAMETER_ERROR as pe:
            print(pe)
        except PARAMETER_FORMAT_ERROR as fe:
            print(fe)
        finally:
            return course_list, True


def is_number(num:str):
    pattern = re.compile(r'(.*)\.(.*)\.(.*)')
    if pattern.match(num):
        return False
    return num.replace(".", "").isdigit()

