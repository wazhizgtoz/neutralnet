"""_summary_
    The examples using the mysqlx module store the configuration in a 
    file named config.py, which is also located in the same directory where 
    Python is executed.
"""

connect_args = {
    "host":"127.0.0.1",
    "port":"3306",
    "user":"root",
    "password":"woot",
    "charset": "utf8mb4",
    "collation": "utf8mb4_unicode_ci",
    "use_unicode": True
};