#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ����
���ڣ�2020.11.24
"""
import random

def name_to_number(choice_name):
    """
    ��ʯͷ��������ֽ��ʷ���ˣ�����ת��Ϊ��Ӧ����
    """
    if choice_name=="ʯͷ":
       return 0
    elif choice_name=="ʷ����":
       return 1
    elif choice_name=="ֽ":
       return 2
    elif choice_name=="����":
       return 3
    elif choice_name=="����":
       return 4
    else:
       return 5

def number_to_name(computer_number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if computer_number==0:
       computer_name="ʯͷ"
    elif computer_number==1:
       computer_name="ʷ����"
    elif computer_number== 2:
       computer_name ="ֽ"
    elif computer_number==3:
       computer_name="����"
    else:
       computer_name="����"
    return computer_name
def rpsls(choice_name):
    """
    ������Ϸ����
    """
    computer_number=random.randrange(0, 4)
    player_choice_number=name_to_number(choice_name)
    computer_name=number_to_name(computer_number)
    print("����ѡ���ǣ�"+str(choice_name))
    print("�������ѡ���ǣ�"+str(computer_name))
    if player_choice_number==4 and computer_number==2:
        print("��Ӯ�ˣ�")
    elif player_choice_number==4 and computer_number==3:
        print("��Ӯ�ˣ�")
    elif player_choice_number==3 and computer_number==1:
        print("��Ӯ�ˣ�")
    elif player_choice_number==3 and computer_number==2:
        print("��Ӯ�ˣ�")
    elif player_choice_number==2 and computer_number==0:
        print("��Ӯ�ˣ�")
    elif player_choice_number==2 and computer_number==1:
        print("��Ӯ�ˣ�")
    elif player_choice_number==1 and computer_number==4:
        print("��Ӯ�ˣ�")
    elif player_choice_number==1 and computer_number==0:
        print("��Ӯ�ˣ�")
    elif player_choice_number==0 and computer_number==4:
        print("��Ӯ�ˣ�")
    elif player_choice_number==0 and computer_number==3:
        print("��Ӯ�ˣ�")
    elif player_choice_number==5:
        print("Error: No Correct Name")
    elif player_choice_number==computer_number:
        print("���������ѡ��һ����")
    else:
           print("�����Ӯ�˰�/(��o��)/~~")
    return choice_name
print("��ӭʹ��RPSLS��Ϸ")#������ʾ
print("����������ѡ��:")
print("----------------")
choice_name=input()
rpsls(choice_name)


