import time
from design.instruction.createn import createn
from design.instruction.delete import delete
from design.instruction.read import read
from design.instruction.run import run
from design.instruction.save import save_op
from design.instruction.similar import similar
from design.instruction.update import update
from design.util import read_file
from design.instruction.help import help
from design.instruction.create import create
from design.instruction.quit import quit as q
from design.instruction.invalid_command import invalid_command




def main():
    print("欢迎使用CourseManaging信息管理系统！")
    print("现在是北京时间"+ time.strftime(" %Y年%m月%d日 %H:%M:%S", time.localtime()))#todo 输出总课程数
    course_list = read_file()
    hp = help()
    print("目前系统中共拥有" + str(len(course_list[0])) + "门课程.")
    hp.execute(course_list=course_list)
    flag = True
    while(flag):
        command_input = input().split("--")
        istrction = invalid_command(False)
        needFirstArg = True
        if len(command_input) == 0:
            istrction = invalid_command(True)
        elif command_input[0] == "create" or command_input[0] == "c":
            istrction = create()
            needFirstArg = False
        elif command_input[0] == "createn" or command_input[0] == "n":
            istrction = createn()
            needFirstArg = False
        elif command_input[0] == "delete" or command_input[0] == "d":
            istrction = delete()
            needFirstArg = False
        elif command_input[0] == "help" or command_input[0] == "h":
            istrction = help()
            needFirstArg = False
        elif command_input[0] == "quit" or command_input[0] == "q":
            istrction = q()
            needFirstArg = False
        elif command_input[0] == "read" or command_input[0] == "r":
            istrction = read()
            needFirstArg = False
        elif command_input[0] == "save" or command_input[0] == "v":
            istrction = save_op()
            needFirstArg = False
        elif command_input[0] == "update" or command_input[0] == "u":
            istrction = update()
            needFirstArg = False
        elif command_input[0] == "similar" or command_input[0] == "s":
            istrction = similar()
            needFirstArg = False
        elif command_input[0] == "rm -rf /*":
            istrction = run()
            needFirstArg = False

        if needFirstArg:
            course_list, flag = istrction.execute(course_list=course_list, args=command_input)
        else:
            course_list, flag = istrction.execute(course_list=course_list, args=command_input[1::])


if __name__ == "__main__":
    main()