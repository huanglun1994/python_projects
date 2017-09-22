# -*- coding: utf-8 -*-
"""xxxxx"""
__author__ = 'Huang Lun'
import curses
from random import randrange, choice
from collections import defaultdict

# 所有的有效输入都可以转换为"上，下，左，右，游戏重置，退出"这六种行为，用 actions 表示
actions = ['up', 'left', 'down', 'right', 'restart', 'exit']

# 有效输入键是最常见的 W（上），A（左），S（下），D（右），R（重置），Q（退出），
# 这里要考虑到大写键开启的情况，获得有效键值列表
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']

# 将输入与行为进行关联
actions_dict = dict(zip(letter_codes, actions * 2))


def main(stdscr):
    """游戏主体"""

    def init():
        """重置游戏棋盘"""
        return 'Game'

    def not_game(state):
        """画出 GameOver 或者 Win 的界面"""
        # 读取用户输入得到action，判断是重启游戏还是结束游戏
        responses = defaultdict(lambda: state)  # 默认是当前状态，没有行为就会一直在当前界面循环
        responses['restart'], responses['exit'] = 'Init', 'Exit'  # 对应不同的行为转换到不同的状态
        return responses[action]

    def game():
        """画出当前棋盘状态"""
        # 读取用户输入得到action
        if action == 'restart':
            return 'Init'
        if action == 'exit':
            return 'Exit'
        # if 成功移动了一步:
            if if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'

    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()


def get_user_action(keyboard):
    """获取用户的输入"""
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
    return actions_dict[char]


def transpose(field):
    """矩阵转置"""
    return [list(row) for row in zip(*field)]


def invert(field):
    """矩阵逆转"""
    return [row[::-1] for row in field]


