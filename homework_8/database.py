import sqlite3

class RPSDatabase:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS rps_results
                          (id INTEGER PRIMARY KEY AUTOINCREMENT, player_name TEXT, player_choice TEXT, computer_choice TEXT, result TEXT)''')
        self.conn.commit()

    def save_result(self, player_name, player_choice, computer_choice, result):
        self.c.execute("INSERT INTO rps_results (player_name, player_choice, computer_choice, result) VALUES (?, ?, ?, ?)",
                       (player_name, player_choice, computer_choice, result))
        self.conn.commit()
