import pyautogui

pyautogui.PAUSE = 0.7

A = list([7, 25, 18, 24, 15, 39, 21, 42, 27, 23, 47, 13, 33, 11, 20, 44])
x = 0

#print(pyautogui.position())
print(A)


pyautogui.click(x=832, y=1052)

pyautogui.doubleClick(x=17, y=162)

while x < len(A):
    pyautogui.write(str(A[x]))

    pyautogui.press('enter')

    pyautogui.click(x=17, y=162)

    x += 1

