from classes import *
from pynput.mouse import Listener

brd = Board()
matrix = brd.draw('white','black', 48)
#print(matrix)

def checkClick(x, y):
    for i in matrix:
        # max_x = str(i['pos'][0])
        # max_y = str(i['pos'][1])
        # min_y = str(i['pos'][2])
        # min_x = str(i['pos'][3])
        max_x = i['pos'][0][0]
        max_y = i['pos'][1][1]
        min_y = i['pos'][2][1]
        min_x = i['pos'][3][0]

        #print(max_x, max_y, min_x, min_y)

        if min_x <= x <= max_x and min_y <= y <= max_y:
            print(i['id'])
            return i['id']
        
def on_click(x, y, button, pressed):
    print(x, y)
    checkClick(x, y)
    return

while True:

    with Listener(on_click=on_click) as listener:
        listener.join()


    # if pyautogui.mouseDown(button='left'):
    #     click_x, click_y = pyautogui.position()
    #     checkClick(click_x, click_y)
        