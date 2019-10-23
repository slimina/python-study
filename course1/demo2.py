import turtle

"""
画树枝
"""

def draw_branch(branch_length):


    if branch_length > 5:
        # 绘制右侧树枝
        turtle.forward(branch_length)
        turtle.right(20)
        draw_branch(branch_length -10)

        # 绘制左侧树枝
        turtle.left(40)
        draw_branch(branch_length - 10)

        if branch_length == 10:
            turtle.color('green')
        else:
            turtle.color('brown')
        # 返回之前的树枝
        turtle.right(20)
        turtle.backward(branch_length)


def main():
    # 向左旋转 90度
    turtle.left(90)
    turtle.penup()
    turtle.backward(200)
    turtle.pendown()
    turtle.color('brown')
    draw_branch(100)
    turtle.exitonclick()


if __name__ == '__main__':
    main()