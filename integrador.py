import os
import msvcrt
from typing import List, Tuple


WALL_CHAR = '#'
PATH_CHAR = '.'
PLAYER_CHAR = 'P'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_maze_map(maze_str: str, end: int) -> List[List[str]]:
    maze_map = [list(row) for row in maze_str.split("\n")]

    
    for row in maze_map:
        while len(row) < end:
            row.append(WALL_CHAR)
    
    
    maze_map[0][0] = PLAYER_CHAR
    maze_map[end][end] = PATH_CHAR
    
    return maze_map

def print_maze(maze_map: List[List[str]]):
    clear_screen()
    for row in maze_map:
        print("".join(row))

def get_key_input() -> str:
    key = msvcrt.getch().decode()
    return key

def main_loop(maze_map: List[List[str]], start: Tuple[int, int], end: Tuple[int, int]):
    px, py = start
    
    while (px, py) != end:
        print_maze(maze_map)
        key = get_key_input()
        
        
        prev_px, prev_py = px, py
        
        
        if key == 'w':
            new_px, new_py = px - 1, py
        elif key == 's':
            new_px, new_py = px + 1, py
        elif key == 'a':
            new_px, new_py = px, py - 1
        elif key == 'd':
            new_px, new_py = px, py + 1
        else:
            continue  
        
        
        if (
            0 <= new_px < len(maze_map) and
            0 <= new_py < len(maze_map[0]) and
            maze_map[new_px][new_py] != WALL_CHAR
        ):
            
            maze_map[px][py] = PATH_CHAR
            #
            px, py = new_px, new_py
            maze_map[px][py] = PLAYER_CHAR


if __name__ == "__main__":
    
    maze_str = """
  ███████████████████
      █         █   █
█ █ ███ ███████ █ █ █
█ █           █ █ █ █
█ █ ███████ █ █████ █
█ █       █ █     █ █
███████ ███████ █ █ █
█ █     █ █     █   █
█ ███████ ███ █████ █
█   █       █ █   █ █
█ ███ ███ █ █████ █ █
█   █   █ █   █   █ █
███ ███████ █ █ █ █ █
█ █   █     █   █   █
█ █ █ █████ █████ █ █
█   █ █     █ █   █ █
█ █████ █████ █████ █
█         █         █
█ █████ █████████ █ █
█   █         █   █ 
███████████████████ 


    """
    
    end = 10  
    maze_map = create_maze_map(maze_str, end)
    start = (0, 0)  
    main_loop(maze_map, start, (end, end))





