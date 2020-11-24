#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：李浩
日期：2020.11.24
"""
import random

def name_to_number(choice_name):
    """
    将石头，剪刀，纸，史波克，蜥蜴转换为对应数字
    """
    if choice_name=="石头":
       return 0
    elif choice_name=="史波克":
       return 1
    elif choice_name=="纸":
       return 2
    elif choice_name=="蜥蜴":
       return 3
    elif choice_name=="剪刀":
       return 4
    else:
       return 5

def number_to_name(computer_number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if computer_number==0:
       computer_name="石头"
    elif computer_number==1:
       computer_name="史波克"
    elif computer_number== 2:
       computer_name ="纸"
    elif computer_number==3:
       computer_name="蜥蜴"
    else:
       computer_name="剪刀"
    return computer_name
def rpsls(choice_name):
    """
    定义游戏规则
    """
    computer_number=random.randrange(0, 4)
    player_choice_number=name_to_number(choice_name)
    computer_name=number_to_name(computer_number)
    print("您的选择是："+str(choice_name))
    print("计算机的选择是："+str(computer_name))
    if player_choice_number==4 and computer_number==2:
        print("您赢了！")
    elif player_choice_number==4 and computer_number==3:
        print("您赢了！")
    elif player_choice_number==3 and computer_number==1:
        print("您赢了！")
    elif player_choice_number==3 and computer_number==2:
        print("您赢了！")
    elif player_choice_number==2 and computer_number==0:
        print("您赢了！")
    elif player_choice_number==2 and computer_number==1:
        print("您赢了！")
    elif player_choice_number==1 and computer_number==4:
        print("您赢了！")
    elif player_choice_number==1 and computer_number==0:
        print("您赢了！")
    elif player_choice_number==0 and computer_number==4:
        print("您赢了！")
    elif player_choice_number==0 and computer_number==3:
        print("您赢了！")
    elif player_choice_number==5:
        print("Error: No Correct Name")
    elif player_choice_number==computer_number:
        print("计算机和您选的一样呢")
    else:
           print("计算机赢了啊/(ㄒoㄒ)/~~")
    return choice_name
print("欢迎使用RPSLS游戏")#文字提示
print("请输入您的选择:")
print("----------------")
choice_name=input()
rpsls(choice_name)


