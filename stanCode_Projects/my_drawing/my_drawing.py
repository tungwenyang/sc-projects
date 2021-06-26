"""
File: my_drawing.py
Name: Claire Yang
----------------------
This program is to draw "The Starry Night' (by Vincent van Gogh) with GObject Classes
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause


def main():
    """
    This program is to draw "The Starry Night' (by Vincent van Gogh) with GObject Classes
    """
    # background
    window = GWindow(width=850, height=640, title='The Starry Night')
    background = GRect(850, 640)
    background.filled = True
    background.fill_color = 'midnightblue'
    background.color = 'midnightblue'
    window.add(background)

    # mountains
    for i in range(11):
        for j in range(5 + i):
            mt1 = GPolygon()
            mt1.add_vertex(((-20 - 80 * i) + 160 * j, (550 + 20 * i) - 15 * j))
            mt1.add_vertex(((180 - 80 * i) + 160 * j, (550 + 20 * i) - 15 * j))
            mt1.add_vertex(((80 - 80 * i) + 160 * j, (500 + 20 * i) - 15 * j))
            mt1.filled = True
            mt1.fill_color = 'black'
            mt1.color = 'darkslategrey'
            window.add(mt1)
    pause(700)

    # houses
    for i in range(10):
        # low
        if i % 2 == 0:
            # house
            h1 = GRect(30, 20)
            h1.filled = True
            h1.fill_color = 'black'
            h1.color = 'saddlebrown'
            window.add(h1, x=380 + 50 * i, y=620)
            # roof
            r1 = GPolygon()
            r1.add_vertex((370 + 50 * i, 620))
            r1.add_vertex((420 + 50 * i, 620))
            r1.add_vertex((395 + 50 * i, 575))
            r1.filled = True
            r1.fill_color = 'black'
            r1.color = 'saddlebrown'
            window.add(r1)
        # high
        else:
            h1 = GRect(30, 40)
            h1.filled = True
            h1.fill_color = 'black'
            h1.color = 'saddlebrown'
            window.add(h1, x=380 + 50 * i, y=600)
            r1 = GPolygon()
            r1.add_vertex((370 + 50 * i, 600))
            r1.add_vertex((420 + 50 * i, 600))
            r1.add_vertex((395 + 50 * i, 555))
            r1.filled = True
            r1.fill_color = 'black'
            r1.color = 'saddlebrown'
            window.add(r1)
    pause(700)

    # galaxy
    for i in range(9):
        for j in range(20):
            g1 = GOval(100, 5)
            g1.filled = True
            if (i + j) % 5 == 0:
                g1.fill_color = 'khaki'
                g1.color = 'khaki'
            elif (i + j) % 5 == 1:
                g1.fill_color = 'lemonchiffon'
                g1.color = 'lemonchiffon'
            elif (i + j) % 5 == 2:
                g1.fill_color = 'wheat'
                g1.color = 'wheat'
            elif (i + j) % 5 == 3:
                g1.fill_color = 'palegoldenrod'
                g1.color = 'palegoldenrod'
            else:
                g1.fill_color = 'midnightblue'
                g1.color = 'midnightblue'
            window.add(g1, x=(-50 + 5 * i) + 60 * j, y=(460 + 5 * i) - 7.5 * j)
    pause(700)

    # star behind the wind
    # 1
    s_bw_1 = GOval(30, 30)
    s_bw_1.filled = True
    s_bw_1.fill_color = 'lemonchiffon'
    s_bw_1.color = 'lemonchiffon'
    window.add(s_bw_1, x=250, y=160)
    for i in range(5):
        s_bw_1_l = GOval(50 - 10 * i, 50 - 10 * i)
        s_bw_1_l.color = 'Khaki'
        window.add(s_bw_1_l, x=265 - (50 - 10 * i) / 2, y=175 - (50 - 10 * i) / 2)
    pause(700)

    # 2
    s_bw_2 = GOval(40, 40)
    s_bw_2.filled = True
    s_bw_2.fill_color = 'lemonchiffon'
    s_bw_2.color = 'lemonchiffon'
    window.add(s_bw_2, x=-25, y=160)
    for i in range(7):
        s_bw_2_l = GOval(70 - 10 * i, 70 - 10 * i)
        s_bw_2_l.color = 'orange'
        window.add(s_bw_2_l, x=-5 - (70 - 10 * i) / 2, y=180 - (70 - 10 * i) / 2)
    pause(700)

    # wind blow
    for i in range(5):
        for j in range(10):
            w = GOval(100, 5)
            w.filled = True
            if (i + j) % 5 == 0:
                w.fill_color = 'lightskyblue'
                w.color = 'lightskyblue'
            elif (i + j) % 5 == 1:
                w.fill_color = 'ivory'
                w.color = 'ivory'
            elif (i + j) % 5 == 2:
                w.fill_color = 'skyblue'
                w.color = 'skyblue'
            elif (i + j) % 5 == 3:
                w.fill_color = 'azure'
                w.color = 'azure'
            else:
                w.fill_color = 'aliceblue'
                w.color = 'aliceblue'
            window.add(w, x=(-50 + 5 * i) + 50 * j, y=(190 + 5 * i) - 11 * j)
    pause(700)

    # big wind circle
    w1 = GArc(250, 385, 0, 130)
    w1.filled = True
    w1.fill_color = 'lightskyblue'
    w1.color = 'lightskyblue'
    window.add(w1, x=370, y=95)
    w2 = GArc(445, 220, 120, 130)
    w2.filled = True
    w2.fill_color = 'lightblue'
    w2.color = 'lightblue'
    window.add(w2, x=365, y=95)
    w3 = GArc(275, 350, 240, 130)
    w3.filled = True
    w3.fill_color = 'lightsteelblue'
    w3.color = 'lightsteelblue'
    window.add(w3, x=370, y=90)
    for i in range(13):
        w4 = GOval(260 - 20 * i, 260 - 20 * i)
        w4.color = 'aliceblue'
        window.add(w4, x=470 - (260 - 20 * i) / 2, y=195 - (260 - 20 * i) / 2)
    pause(700)

    # wind blow
    for i in range(5):
        for j in range(10):
            w = GOval(100, 5)
            w.filled = True
            if (i + j) % 5 == 0:
                w.fill_color = 'lightskyblue'
                w.color = 'lightskyblue'
            elif (i + j) % 5 == 1:
                w.fill_color = 'ivory'
                w.color = 'ivory'
            elif (i + j) % 5 == 2:
                w.fill_color = 'skyblue'
                w.color = 'skyblue'
            elif (i + j) % 5 == 3:
                w.fill_color = 'azure'
                w.color = 'azure'
            else:
                w.fill_color = 'aliceblue'
                w.color = 'aliceblue'
            window.add(w, x=(-50 + 5 * i) + 50 * j, y=(190 + 5 * i) - 11 * j)
    pause(700)

    # small wind circle
    small_w1 = GOval(90, 90)
    small_w1.filled = True
    small_w1.fill_color = 'lightskyblue'
    small_w1.color = 'lightskyblue'
    window.add(small_w1, x=580, y=250)
    for i in range(10):
        small_w2 = GOval(140 - 15 * i, 140 - 15 * i)
        small_w2.color = 'aliceblue'
        window.add(small_w2, x=625 - (140 - 15 * i) / 2, y=295 - (140 - 15 * i) / 2)
    pause(700)

    # star behind the tree
    s_bt = GOval(40, 40)
    s_bt.filled = True
    s_bt.fill_color = 'khaki'
    s_bt.color = 'khaki'
    window.add(s_bt, x=85, y=280)
    for i in range(6):
        s_bt_l = GOval(60 - 10 * i, 60 - 10 * i)
        s_bt_l.color = 'lemonchiffon'
        window.add(s_bt_l, x=105 - (60 - 10 * i) / 2, y=300 - (60 - 10 * i) / 2)
    pause(700)

    # tree
    t1 = GRect(50, 400)
    t1.filled = True
    t1.fill_color = 'black'
    t1.color = 'black'
    window.add(t1, x=120, y=240)

    t2 = GArc(150, 160, 80, 200)
    t2.filled = True
    t2.fill_color = 'black'
    t2.color = 'black'
    window.add(t2, x=100, y=300)

    t3 = GArc(220, 220, 80, 200)
    t3.filled = True
    t3.fill_color = 'black'
    t3.color = 'black'
    window.add(t3, x=80, y=440)

    t4 = GArc(30, 150, 135, 185)
    t4.filled = True
    t4.fill_color = 'black'
    t4.color = 'black'
    window.add(t4, x=110, y=180)

    t5 = GArc(100, 120, 260, 150)
    t5.filled = True
    t5.fill_color = 'black'
    t5.color = 'black'
    window.add(t5, x=110, y=150)

    t6 = GArc(60, 100, 250, 180)
    t6.filled = True
    t6.fill_color = 'black'
    t6.color = 'black'
    window.add(t6, x=130, y=100)

    t7 = GArc(30, 150, 110, 185)
    t7.filled = True
    t7.fill_color = 'black'
    t7.color = 'black'
    window.add(t7, x=142, y=20)

    t8 = GArc(80, 120, 80, 180)
    t8.filled = True
    t8.fill_color = 'black'
    t8.color = 'black'
    window.add(t8, x=120, y=130)

    t9 = GArc(30, 150, 230, 170)
    t9.filled = True
    t9.fill_color = 'black'
    t9.color = 'black'
    window.add(t9, x=155, y=170)

    t10 = GArc(80, 150, 270, 170)
    t10.filled = True
    t10.fill_color = 'black'
    t10.color = 'black'
    window.add(t10, x=150, y=250)

    t11 = GArc(150, 180, 270, 190)
    t11.filled = True
    t11.fill_color = 'black'
    t11.color = 'black'
    window.add(t11, x=130, y=380)

    t12 = GRect(150, 100)
    t12.filled = True
    t12.fill_color = 'black'
    t12.color = 'black'
    window.add(t12, x=150, y=540)

    t13 = GArc(150, 220, 290, 190)
    t13.filled = True
    t13.fill_color = 'black'
    t13.color = 'black'
    window.add(t13, x=240, y=530)

    t14 = GRect(100, 100)
    t14.filled = True
    t14.fill_color = 'black'
    t14.color = 'black'
    window.add(t14, x=150, y=440)

    t15 = GArc(150, 180, 280, 190)
    t15.filled = True
    t15.fill_color = 'black'
    t15.color = 'black'
    window.add(t15, x=180, y=420)

    t16 = GArc(30, 180, 220, 170)
    t16.filled = True
    t16.fill_color = 'black'
    t16.color = 'black'
    window.add(t16, x=175, y=310)

    t17 = GArc(30, 150, 135, 185)
    t17.filled = True
    t17.fill_color = 'black'
    t17.color = 'black'
    window.add(t17, x=80, y=530)

    pause(700)

    # moon
    m1 = GOval(120, 120)
    m1.filled = True
    m1.fill_color = 'khaki'
    m1.color = 'khaki'
    window.add(m1, x=730, y=0)
    for i in range(17):
        l1 = GOval(170-10*i, 170-10*i)
        l1.color = 'gold'
        window.add(l1, x=790-(170-10*i)/2, y=60-(170-10*i)/2)

    m2 = GOval(80, 80)
    m2.filled = True
    m2.fill_color = 'darkorange'
    m2.color = 'darkorange'
    window.add(m2, x=750, y=20)

    m3 = GOval(55, 55)
    m3.filled = True
    m3.fill_color = 'gold'
    m3.color = 'gold'
    window.add(m3, x=775, y=25)

    for i in range(8):
        l2 = GOval(80-10*i, 80-10*i)
        l2.color = 'orange'
        window.add(l2, x=790-(80-10*i)/2, y=60-(80-10*i)/2)

    pause(700)

    # stars
    s1 = GOval(100, 100)
    s1.filled = True
    s1.fill_color = 'moccasin'
    s1.color = 'moccasin'
    window.add(s1, x=240, y=275)
    for i in range(14):
        s1_l = GOval(140 - 10 * i, 140 - 10 * i)
        s1_l.color = 'gold'
        window.add(s1_l, x=290 - (140 - 10 * i) / 2, y=325 - (140 - 10 * i) / 2)
    pause(700)

    s3 = GOval(60, 60)
    s3.filled = True
    s3.fill_color = 'lemonchiffon'
    s3.color = 'lemonchiffon'
    window.add(s3, x=505, y=-10)
    for i in range(8):
        s3_l = GOval(80 - 10 * i, 80 - 10 * i)
        s3_l.color = 'orange'
        window.add(s3_l, x=535 - (80 - 10 * i) / 2, y=20 - (80 - 10 * i) / 2)
    pause(700)

    s6 = GOval(60, 60)
    s6.filled = True
    s6.fill_color = 'lemonchiffon'
    s6.color = 'lemonchiffon'
    window.add(s6, x=30, y=-20)
    for i in range(8):
        s6_l = GOval(80 - 10 * i, 80 - 10 * i)
        s6_l.color = 'gold'
        window.add(s6_l, x=60 - (80 - 10 * i) / 2, y=10 - (80 - 10 * i) / 2)
    pause(700)

    s2 = GOval(60, 60)
    s2.filled = True
    s2.fill_color = 'lemonchiffon'
    s2.color = 'lemonchiffon'
    window.add(s2, x=610, y=80)
    for i in range(9):
        s2_l = GOval(90 - 10 * i, 90 - 10 * i)
        s2_l.color = 'Khaki'
        window.add(s2_l, x=640 - (90 - 10 * i) / 2, y=110 - (90 - 10 * i) / 2)
    pause(700)

    s4 = GOval(50, 50)
    s4.filled = True
    s4.fill_color = 'lemonchiffon'
    s4.color = 'lemonchiffon'
    window.add(s4, x=300, y=-35)
    for i in range(8):
        s4_l = GOval(80 - 10 * i, 80 - 10 * i)
        s4_l.color = 'Khaki'
        window.add(s4_l, x=325 - (80 - 10 * i) / 2, y=-10 - (80 - 10 * i) / 2)
    pause(700)

    s5 = GOval(50, 50)
    s5.filled = True
    s5.fill_color = 'khaki'
    s5.color = 'khaki'
    window.add(s5, x=165, y=60)
    for i in range(8):
        s5_l = GOval(80 - 10 * i, 80 - 10 * i)
        s5_l.color = 'ivory'
        window.add(s5_l, x=190 - (80 - 10 * i) / 2, y=85 - (80 - 10 * i) / 2)
    pause(700)

    # label
    label_1 = GLabel('The Starry Night')
    label_1.font = '-14'
    label_1.color = 'beige'
    window.add(label_1, x=690, y=210)

    label = GLabel('- Vincent van Gogh')
    label.font = '-10'
    label.color = 'beige'
    window.add(label, x=720, y=233)


if __name__ == '__main__':
    main()
