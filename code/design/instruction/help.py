from design.instruction.instructions import instruction

class help(instruction):

    def __init__(self):
        self.long_name = "help"
        self.short_name = "h"

    def execute(self, course_list: list, args=None):
        print()
        print("--------------------------------------------------------------------------------")
        print("信息系统使用说明")
        print("指令     | 简写  |    格式                                    | 使用说明")
        print("create  |  c   |   create--[课程名]--[课程简介]--[课程详情]     |  创建一门课程")
        print("createn |  n   |   createn[--[课程名]--[课程简介]--[课程详情]]* |  连续创建多门课程")
        print("delete  |  d   |   delete--[课程名]                          |  删除课程")
        print("help    |  h   |   help                                     |  显示帮助信息")
        print("read    |  r   |   read--[课程名]                            |  查找课程")
        print("update  |  u   |   update--[课程名]--[课程简介]--[课程详情]     |  更新课程内容")
        print("update  |  u   |   update--[课程名]--/intro=[内容]            |  更新课程简介")
        print("update  |  u   |   update--[课程名]--/detail=[内容]           |  更新课程详情")
        print("similar |  s   |   similar--[课程名]--[相似度]                |  查找相似度大于等于[相似度]的课程")
        print("similar |  s   |   similar--[课程名]--[数量]                  |  查找相似度最高的[数量]门课程")
        print("save    |  v   |   save                                     |  保存当前课程数据")
        print("quit    |  q   |   quit                                     |  退出管理系统")
        print("--------------------------------------------------------------------------------")
        print()
        return course_list, True