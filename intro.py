from buttons import *

def red_quick_intro(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    # 491 frames
    file.write(b(Select | B | Up))
    file.write(b(Empty) * 3)
    file.write(b(Select | B | Up))
    file.write(b(Empty) * 168)
    file.write(b(A))
    file.write(b(Empty) * 145)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))

def red_first_hop(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    file.write(b(A))
    file.write(b(Empty) * 133)
    file.write(b(Start))
    file.write(b(Empty) * 169)
    file.write(b(A))
    file.write(b(Empty) * 145)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))

def red_second_hop(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    file.write(b(A))
    file.write(b(Empty) * 193)
    file.write(b(Start))
    file.write(b(Empty) * 168)
    file.write(b(A))
    file.write(b(Empty) * 145)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))

def red_third_hop(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    file.write(b(A))
    file.write(b(Empty) * 302)
    file.write(b(Start))
    file.write(b(Empty) * 167)
    file.write(b(A))
    file.write(b(Empty) * 145)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))

def red_fourth_hop(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    file.write(b(A))
    file.write(b(Empty) * 450)
    file.write(b(Start))
    file.write(b(Empty) * 168)
    file.write(b(A))
    file.write(b(Empty) * 145)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))


def blue_quick_intro(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    file.write(b(Select | B | Up))
    file.write(b(Empty) * 3)
    file.write(b(Select | B | Up))
    file.write(b(Empty) * 167)
    file.write(b(A))
    file.write(b(Empty) * 153)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))


def blue_first_hop(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    file.write(b(A))
    file.write(b(Empty) * 133)
    file.write(b(Start))
    file.write(b(Empty) * 168)
    file.write(b(A))
    file.write(b(Empty) * 153)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))


def blue_second_hop(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    file.write(b(A))
    file.write(b(Empty) * 193)
    file.write(b(Start))
    file.write(b(Empty) * 167)
    file.write(b(A))
    file.write(b(Empty) * 153)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))


def blue_third_hop(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    file.write(b(A))
    file.write(b(Empty) * 302)
    file.write(b(Start))
    file.write(b(Empty) * 166)
    file.write(b(A))
    file.write(b(Empty) * 153)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))


def blue_fourth_hop(file, palette=Empty, extra=0):
    file.write(b(Empty) * 75)
    file.write(b(palette))
    file.write(b(Empty) * 415)
    file.write(b(A))
    file.write(b(Empty) * 450)
    file.write(b(Start))
    file.write(b(Empty) * 167)
    file.write(b(A))
    file.write(b(Empty) * 153)
    file.write(b(Start | A))
    file.write(b(Empty) * 49)
    file.write(b(Start | A))
    file.write(b(Empty) * (42 + extra))