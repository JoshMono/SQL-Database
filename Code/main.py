from commands import Commands

if __name__ == "__main__":
    sql_object = Commands().SQL()
    sql_object.open_db_connection()
    sql_object.landing_page()
    sql_object.close_db_connection()