from buttons import *

Same = object()

def direction(file, dir, num=1, fill=Empty, extra=0):
    if fill is Same:
        fill = dir
    for _ in range(num):
        file.write(b(dir))
        file.write(b(fill) * (16 + extra))

def ledge_jump(file, dir, num=1, fill=Empty, extra=0):
    if fill is Same:
        fill = dir
    for _ in range(num):
        file.write(b(dir))
        file.write(b(fill) * (39 + extra))

def overworld_a(file, num=1, fill=Empty, extra=0):
    file.write(b(A))
    file.write(b(fill) * (1 + extra))

def wait(file, num=1):
    file.write(b(Empty) * num)

def raw(file, input):
    file.write(b(input))
