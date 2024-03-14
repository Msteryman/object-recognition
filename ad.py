import keyboard

def say_hello():
    print("Привет, мир!")

keyboard.add_hotkey('t', say_hello)

keyboard.wait('esc')  # Программа будет работать до нажатия клавиши "esc" для выхода
print('hell')