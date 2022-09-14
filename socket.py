import sys
import socket


class Utama():
    print(" Masukan Pilihan Anda")
    print("1) Sebagai Server")
    print("2) Sebagai Client")
    print("3) Keluar")

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":

        lokasi = socket.gethostbyname("127.0.0.1")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((lokasi, 2120))
        s.listen(5)
        print("Server sudah aktif")

        client, alamat = s.accept()
        print("Menerima koneksi dari : ", alamat)
        while True:
            data = client.recv(1024).decode()
            if not data:
                break
            print("Pesan masuk :", str(data))
            data = input(">")
            client.send(data.encode())
    elif pilihan == "2":

        alamatServer = input("Masukan alamat server : ")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((alamatServer, 2120))
        pesan = input(">")
        while pesan != "bye":
            s.send(pesan.encode())
            data = s.recv(1024).decode()
            print("server : ", data)
            pesan = input(">")
        s.close()

    else:
        quit()


if __name__ == "__main__":
    Utama()
    sys.exit()
