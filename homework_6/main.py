# from bank import Bank

# bank = Bank()

# while True:
#     print("1. Создать счет")
#     print("2. Установить пин-код")
#     print("3. Внести деньги")
#     print("4. Снять деньги")
#     print("5. Проверить баланс")
#     print("6. Выход")

#     choice = input("Выберите действие: ")

#     if choice == "1":
#         account_number = input("Введите номер счета: ")
#         initial_balance = float(input("Введите начальный баланс: "))
#         account = bank.create_account(account_number, initial_balance)
#         if account:
#             print(f"Счет {account_number} создан успешно.")
#         else:
#             print(f"Счет {account_number} уже существует.")

#     elif choice == "2":
#         account_number = input("Введите номер счета: ")
#         new_pin = input("Введите новый пин-код: ")
#         bank.set_pin(account_number, new_pin)

#     elif choice == "3":
#         account_number = input("Введите номер счета: ")
#         amount = float(input("Введите сумму для внесения: "))
#         bank.deposit(account_number, amount)

#     elif choice == "4":
#         account_number = input("Введите номер счета: ")
#         amount = float(input("Введите сумму для снятия: "))
#         withdrawn_amount = bank.withdraw(account_number, amount)
#         if withdrawn_amount > 0:
#             print(f"Снято {withdrawn_amount} сом.")
#         else:
#             print("Недостаточно средств или счет не существует.")

#     elif choice == "5":
#         account_number = input("Введите номер счета: ")
#         balance = bank.get_balance(account_number)
#         if balance is not None:
#             print(f"Баланс счета {account_number}: {balance} сом.")
#         else:
#             print("Счет не существует.")

#     elif choice == "6":
#         print("Выход из программы.")
#         break
