from screen import Screen
from sugar import Joystick
from board import *
import random

# 初始化屏幕
s = Screen()
s.autoRefresh(False)
BG_COLOR = 0x000000

# 初始化摇杆
joystick = Joystick()

# 游戏参数
BOARD_SIZE = 3
TILE_SIZE = 40
BOARD_START_X = 20
BOARD_START_Y = 20

# 颜色
TILE_COLOR = 0x004488
SELECTED_COLOR = 0xFF8800
EMPTY_COLOR = 0x222222
TEXT_COLOR = 0xFFFFFF

# 按键状态
last_btn_a = False
last_btn_b = False

# 游戏状态
board = []
empty_pos = (0, 0)  # 空格位置 (row, col)
selected_pos = None  # 选中的数字位置 (row, col)

def get_center_position(text, size=1, screen_w=160, screen_h=128):
    chinese_w, english_w, number_w, space_w, char_h = 12, 7, 7, 6, 12
    total_width = 0
    for ch in text:
        if '\u4e00' <= ch <= '\u9fff':
            total_width += chinese_w
        elif ch.isdigit():
            total_width += number_w
        elif ch == ' ':
            total_width += space_w
        else:
            total_width += english_w
    w, h = total_width * size, char_h * size
    x, y = (screen_w - w) // 2, (screen_h - h) // 2
    return x, y, w, h

def init_board():
    """初始化棋盘"""
    global board, empty_pos
    # 创建有序棋盘
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    empty_pos = (2, 2)
    
    # 随机移动打乱（确保可解）
    for _ in range(100):
        possible_moves = get_valid_moves()
        if possible_moves:
            move = random.choice(possible_moves)
            swap_with_empty(move)

def get_valid_moves():
    """获取可以移动到空格的位置"""
    row, col = empty_pos
    moves = []
    
    # 检查四个方向
    if row > 0:
        moves.append((row - 1, col))  # 上
    if row < BOARD_SIZE - 1:
        moves.append((row + 1, col))  # 下
    if col > 0:
        moves.append((row, col - 1))  # 左
    if col < BOARD_SIZE - 1:
        moves.append((row, col + 1))  # 右
    
    return moves

def swap_with_empty(pos):
    """交换指定位置与空格"""
    global board, empty_pos
    row, col = pos
    empty_row, empty_col = empty_pos
    
    # 交换
    board[empty_row][empty_col], board[row][col] = board[row][col], board[empty_row][empty_col]
    empty_pos = (row, col)

def can_move_to_empty(pos):
    """检查指定位置是否可以移动到空格"""
    row, col = pos
    empty_row, empty_col = empty_pos
    
    # 检查是否相邻
    if (abs(row - empty_row) == 1 and col == empty_col) or \
       (abs(col - empty_col) == 1 and row == empty_row):
        return True
    return False

def draw_board():
    """绘制棋盘"""
    global board, empty_pos, selected_pos
    
    # 清除整个屏幕（用背景色覆盖）
    s.rect(0, 0, 160, 128, BG_COLOR, 1)
    
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            x = BOARD_START_X + col * TILE_SIZE
            y = BOARD_START_Y + row * TILE_SIZE
            
            value = board[row][col]
            
            if value == 0:
                # 空格
                s.rect(x, y, TILE_SIZE - 2, TILE_SIZE - 2, EMPTY_COLOR, 1)
            else:
                # 数字块
                color = SELECTED_COLOR if selected_pos == (row, col) else TILE_COLOR
                s.rect(x, y, TILE_SIZE - 2, TILE_SIZE - 2, color, 1)
                
                # 绘制数字
                text = str(value)
                # 计算居中位置
                x_center = x + TILE_SIZE // 2 - (len(text) * 7) // 2
                y_center = y + TILE_SIZE // 2 - 6
                s.text(text, x_center, y_center, 1, TEXT_COLOR)
    
    # 显示标题和提示
    x, y, w, h = get_center_position("華容道", 1)
    s.text("華容道", x, BOARD_START_Y + TILE_SIZE * BOARD_SIZE + 10, 1, 0xFFFFFF)
    
    s.text("按A/B選數", 5, BOARD_START_Y + TILE_SIZE * BOARD_SIZE + 25, 0, 0x00FF00)
    s.text("搖桿移動", 5, BOARD_START_Y + TILE_SIZE * BOARD_SIZE + 37, 0, 0x00FF00)

def check_win():
    """检查是否获胜"""
    target = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return board == target

# 初始化游戏
init_board()

# 主循环
while True:
    # 读取摇杆状态
    joystick_state = joystick.state()
    
    # 读取A/B按键
    button = read_button()
    btn_a = (button == 1)
    btn_b = (button == 3)
    
    # 按A键：选择上一个数字
    if btn_a and not last_btn_a:
        # 找到所有非空位置
        all_positions = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] != 0]
        if all_positions:
            if selected_pos is None:
                selected_pos = all_positions[0]
            else:
                idx = all_positions.index(selected_pos)
                selected_pos = all_positions[(idx - 1) % len(all_positions)]
    
    # 按B键：选择下一个数字
    if btn_b and not last_btn_b:
        # 找到所有非空位置
        all_positions = [(r, c) for r in range(BOARD_SIZE) for c in range(BOARD_SIZE) if board[r][c] != 0]
        if all_positions:
            if selected_pos is None:
                selected_pos = all_positions[0]
            else:
                idx = all_positions.index(selected_pos)
                selected_pos = all_positions[(idx + 1) % len(all_positions)]
    
    # 更新按键状态
    last_btn_a = btn_a
    last_btn_b = btn_b
    
    # 摇杆控制移动
    if selected_pos is not None:
        row, col = selected_pos
        moved = False
        
        # 检查选中的数字是否与空格相邻
        empty_row, empty_col = empty_pos
        is_adjacent = (abs(row - empty_row) + abs(col - empty_col)) == 1
        
        if is_adjacent:
            if joystick_state == 'up':
                # 向上移动到空格
                if empty_row < row:
                    swap_with_empty(selected_pos)
                    selected_pos = None  # 移动后清除选中状态
                    moved = True
            elif joystick_state == 'down':
                # 向下移动到空格
                if empty_row > row:
                    swap_with_empty(selected_pos)
                    selected_pos = None  # 移动后清除选中状态
                    moved = True
            elif joystick_state == 'left':
                # 向左移动到空格
                if empty_col < col:
                    swap_with_empty(selected_pos)
                    selected_pos = None  # 移动后清除选中状态
                    moved = True
            elif joystick_state == 'right':
                # 向右移动到空格
                if empty_col > col:
                    swap_with_empty(selected_pos)
                    selected_pos = None  # 移动后清除选中状态
                    moved = True
        
        # 检查获胜
        if moved and check_win():
            s.rect(0, 0, 160, 128, BG_COLOR, 1)
            x, y, w, h = get_center_position("恭喜獲勝！", 2)
            s.text("恭喜獲勝！", x, 50, 2, 0x00FF00)
            s.refresh()
            import time
            time.sleep(2)
            init_board()
            selected_pos = None
    
    # 绘制棋盘
    draw_board()
    s.refresh()