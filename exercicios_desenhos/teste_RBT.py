import pyautogui

pyautogui.PAUSE = 0.1

#A = list([7, 25, 18, 24, 15, 39, 21, 42, 27, 23, 47, 13, 33, 11, 20, 44])
A = list(range(1, 17))
x = 0

print(pyautogui.position())


pyautogui.click(x=832, y=1052)

pyautogui.doubleClick(x=41, y=274)

while x < len(A):
    pyautogui.write(str(A[x]))

    pyautogui.press('tab')

    pyautogui.press('space')

    pyautogui.hotkey('shift', 'tab')

    x += 1

