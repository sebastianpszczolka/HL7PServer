import socket
import time

frame = "\x0bMSH|^~\&|MEDIQUS|MEDIQUS|LAB|SIEMIRADZKI|20211105002842||ORM^O01|313200001.41|P|2.3|||AL|NE|POL|CP1250|PLPID|1|74112699728|20^^^^^MEDIQUS||TESTOWAA^PACJENTKA||19741126|F|||GROTGERA 2 ^^KRAKÓW^^30-004||500300100^^^ORC|NW|41.1^MEDIQUS||000000041^MEDIQUS|||^^^20211029^^R&NORMALNE|41.1^MEDIQUS||||15^MACKO^JAROSŁAW^^^^^MEDIQUS^PRZAW&3716967|43^Laboratorium wewn.^MEDIQUS||||5^Oddział Położniczo-Ginekologiczny^MEDIQUSOBR||41.1^MEDIQUS||188^Albumina w surowicy^MEDIQUS||||||||||20211029132951|^^MEDIQUS^^^^^|||||||||43BLG|1|DP|09R^^^09R&PLATNIK&MEDIQUSORC|NW|41.2^MEDIQUS||000000041^MEDIQUS|||^^^20211029^^R&NORMALNE|41.2^MEDIQUS||||15^MACKO^JAROSŁAW^^^^^MEDIQUS^PRZAW&3716967|43^Laboratorium wewn.^MEDIQUS||||5^Oddział Położniczo-Ginekologiczny^MEDIQUSOBR||41.2^MEDIQUS||192^Bilirubina całkowita w surowicy^MEDIQUS||||||||||20211029132951|^^MEDIQUS^^^^^|||||||||43BLG|1|DP|09R^^^09R&PLATNIK&MEDIQUS\x0d\x1c\x0d"

HOST = 'localhost'
PORT = 8091

if __name__ == '__main__':

    while True:
        time.sleep(0.1)

        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(4)
            s.connect((HOST, PORT))
            s.sendall(frame.encode('1250'))
            data = s.recv(1024)

            print(f'Received: {data}', )
            s.close()
        except Exception as exc:
            print(exc)
