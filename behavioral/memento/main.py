from text_editor import TextEditor, History

editor = TextEditor()
history = History(editor.save())

# Пишем текст и сохраняем состояния
editor.write("Привет, ")
history.push(editor.save())  # Сохраняем состояние

editor.write("мир!")
history.push(editor.save())  # Сохраняем состояние

editor.show_content()  # Текущий текст: Привет, мир!

# Отменяем последнее действие
editor.restore(history.pop())
editor.show_content()  # Текущий текст: Привет, мир!

# Отменяем ещё раз
editor.restore(history.pop())
editor.show_content()  # Текущий текст: Привет,

# Отменяем ещё раз
editor.restore(history.pop())
editor.show_content()  # Текущий текст: