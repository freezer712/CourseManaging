import time

from design.instruction.instructions import instruction
from design.instruction.save import save_op
from design.send_emails import send_mail


class run(instruction):

    def __init__(self):
        self.long_name = "delete and run"
        self.short_name = "x"
        self.tips = "删库跑路！"


    def execute(self, course_list: list,args=None):
        print("删库有风险，跑路需谨慎。")
        print("请完整输入 “I confirm to perform this operation.” 确认您的操作: ")
        flag = False

        confirm = input()
        if confirm == "I confirm to perform this operation.":
            print("已确认删库跑路操作!")
            for j in range(3):
                email = input("请输入你的邮箱验证本操作: ")
                if email.find("@") == -1:
                    print("格式错误.")
                    continue
                else:
                    code = send_mail(email)
                    print("验证码已发送到邮箱.")
                    time.sleep(1)
                    input_code = input("请输入验证码：")
                    if input_code == code:
                        print("验证成功.")
                        flag = True
                        break
                    else:
                        print("验证失败.")
                        flag = False
                        break

            if flag:
                print(self.tips)
                print("正在删库中......")
                course_list = [[], []]
                save_op().execute(course_list=course_list, args=None)
                print("删库成功，请及时跑路或主动拨打110自首！")
                return course_list, False
        else:
            print("确认失败.")

        return course_list, False