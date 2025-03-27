from vending_machine import VendingMachine, Item


machine = VendingMachine()
snickers = Item("Snickers", 50)

machine.select_item(snickers)  # Внесите деньги сначала!
machine.insert_money(100)      # Внесено: 100 руб.
machine.select_item(snickers)  # Выбран: Snickers
machine.dispense()             # Выдан Snickers. Сдача: 50 руб.