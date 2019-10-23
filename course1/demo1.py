"""
五角星
"""
import turtle

"""
递归画 五角星
"""
def draw_recusive(size):
    count = 1
    while count <= 5:
        # 向前移动画笔
        turtle.forward(size)
        # 向右旋转 144度
        turtle.right(144)
        count += 1
    size += 10
    if size <= 100:
        draw_recusive(size)


def main():
    # 抬起画笔
    turtle.penup()
    # 往后移动
    turtle.backward(200)
    # 落下画笔
    turtle.pendown()
    # 画笔大小
    turtle.pensize(3)
    # 画笔颜色
    turtle.pencolor('red')
    draw_recusive(50)
    # 点击退出，不自动退出
    turtle.exitonclick()


if __name__ == '__main__':
    main()

