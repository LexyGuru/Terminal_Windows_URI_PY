import webbrowser
from sty import fg, ef, rs
import os.path
import os
import time

file = "c:\\temp\\speedtest.txt"


class speedtest:
    global ff
    ff = "    "

    # speedtest_cli
    def speedtest_start_save(self):
        f = "speedtest.exe > c:\\temp\\speedtest.txt"
        os.system(r"" + f)

        with open('c:\\temp\\speedtest.txt', encoding='utf8') as f:
            for line in f:
                print(line.strip())
        os.system("cls")

    # webopen speedtest
    def speedtest_cli_info_web(self):
        word = "Result URL:"
        with open(r'c:\\temp\\speedtest.txt', 'r', encoding="utf8") as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    """print(word, 'string exists in file')
                    print('Line Number:', lines.index(line))
                    print('Line:', line)
                    print("")
                    print(line[14:-1])"""
                    webp = line[14:-1]
                    webbrowser.open(webp)


# color speedtest :)
class speedtest_color:

    def Server(self):
        word = "Server:"
        with open(r'c:\\temp\\speedtest.txt', 'r', encoding="utf8") as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    # print(ff + line[4:-1])
                    print(fg(15, 180, 250) + ff + line[4:14] + fg(110, 55, 220) + line[14:-1] + fg.rs)

    def ISP(self):
        word = "ISP:"
        with open(r'c:\\temp\\speedtest.txt', 'r', encoding="utf8") as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    print(fg(15, 180, 230) + line[0:14] + fg(100, 55, 210) + line[14:-1] + fg.rs)

    def Idle_Latency(self):
        word = "Idle Latency:"
        with open(r'c:\\temp\\speedtest.txt', 'r', encoding="utf8") as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    # print(line[0:-1])
                    print(fg(15, 180, 210) + line[0:14] + fg(90, 55, 200) + line[14:-1] + fg.rs)

    def Download(self):
        word = "Download:"
        with open(r'c:\\temp\\speedtest.txt', 'r', encoding="utf8") as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    # print(ff + line[4:-1])
                    print(fg(15, 180, 190) + line[0:14] + fg(80, 55, 190) + line[14:-1] + fg.rs)

    def Upload(self):
        word = "Upload:"
        with open(r'c:\\temp\\speedtest.txt', 'r', encoding="utf8") as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    # print(ff + line[4:-1])
                    print(fg(5, 180, 170) + line[0:14] + fg(70, 55, 180) + line[14:-1] + fg.rs)

    def Packet_Loss(self):
        word = "Packet Loss:"
        with open(r'c:\\temp\\speedtest.txt', 'r', encoding="utf8") as fp:
            # read all lines in a list
            lines = fp.readlines()
            for line in lines:
                # check if string present on a current line
                if line.find(word) != -1:
                    # print(ff + line[4:-1])
                    print(fg(5, 180, 150) + line[0:14] + fg(60, 55, 170) + line[14:-1] + fg.rs)


class file_true_false_ch:
    # Output False True
    def out_True(self):
        print(
            fg(255, 10, 70) + "S" +
            fg(245, 10, 80) + "p" +
            fg(235, 10, 90) + "e" +
            fg(225, 10, 100) + "e" +
            fg(215, 10, 110) + "d" +
            fg(205, 10, 120) + "t" +
            fg(195, 10, 130) + "e" +
            fg(185, 10, 140) + "s" +
            fg(175, 10, 150) + "t " +
            fg(165, 10, 160) + "b" +
            fg(155, 10, 170) + "y " +
            fg(145, 10, 180) + "O" +
            fg(135, 10, 190) + "o" +
            fg(125, 10, 200) + "k" +
            fg(115, 10, 210) + "l" +
            fg(105, 10, 220) + "a" +
            fg.rs + "\n")
        speedtest_color.Server('self')
        speedtest_color.ISP('self')
        speedtest_color.Idle_Latency('self')
        speedtest_color.Download('self')
        speedtest_color.Upload('self')
        speedtest_color.Packet_Loss('self')

    def out_False(self):
        print(
            fg(255, 10, 70) + "S" +
            fg(245, 10, 80) + "p" +
            fg(235, 10, 90) + "e" +
            fg(225, 10, 100) + "e" +
            fg(215, 10, 110) + "d" +
            fg(205, 10, 120) + "t" +
            fg(195, 10, 130) + "e" +
            fg(185, 10, 140) + "s" +
            fg(175, 10, 150) + "t " +
            fg(165, 10, 160) + "b" +
            fg(155, 10, 170) + "y " +
            fg(145, 10, 180) + "O" +
            fg(135, 10, 190) + "o" +
            fg(125, 10, 200) + "k" +
            fg(115, 10, 210) + "l" +
            fg(105, 10, 220) + "a" +
            fg.rs + "\n")
        print("2-5 min")
        speedtest.speedtest_start_save('self')


    def ende(self):
        file_true_false_ch.out_True('self')
        created = os.path.getctime(file)
        year, month, day, hour, minute, second = time.localtime(created)[:-3]

        old_name = r"C:\temp\speedtest.txt"
        new_name = r"C:\temp\speedtest_" + "%02d-%02d-%d-" % (day, month, year) + "%02d-%02d-%02d" % (
            hour, minute, second) + ".txt"
        print(
            fg(105, 10, 220) + "D" +
            fg(115, 15, 210) + "a" +
            fg(125, 20, 200) + "t" +
            fg(135, 25, 190) + "e " +
            fg(145, 30, 180) + "c" +
            fg(155, 35, 170) + "r" +
            fg(165, 40, 160) + "e" +
            fg(175, 45, 150) + "a" +
            fg(185, 50, 140) + "t" +
            fg(195, 55, 130) + "e" +
            fg(205, 60, 120) + "d" +
            fg(215, 65, 110) + ":" +

            fg(105, 10, 220) + " %02d/%02d/%d " % (day, month, year) +
            fg(255, 50, 0) + "%02d:%02d:%02d" % (hour, minute, second))
        os.rename(old_name, new_name)


# file ????
file_exists = os.path.exists('c:\\temp\\speedtest.txt')

if file_exists == False:
    file_true_false_ch.out_False('self')
    file_exists = os.path.exists('c:\\temp\\speedtest.txt')

if file_exists == True:
    file_true_false_ch.ende('self')










