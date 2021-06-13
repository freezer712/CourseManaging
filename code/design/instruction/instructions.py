from design.error.ERROR.UNIMPLEMENT_ERROR import UNIMPLEMENT_ERROR

class instruction:

    def execute(self, course_list: list,args=None):
        try:
            raise UNIMPLEMENT_ERROR
        except:
            print(UNIMPLEMENT_ERROR)
        return course_list, True