def main():   
    import sqlite3
    import pygame
    import time
    import pdb
    pygame.init()

    gw = pygame.display.set_mode((800, 400))
    conn = sqlite3.connect("game_files/trivia/test.db")
    cursor = conn.execute("SELECT Question, Option1, Option2, Option3, Option4 from Quiz;")
    run = True
    question = 0
    question_list = []
    option1_list = []
    option2_list = []
    option3_list = []
    option4_list = []
    correct = 0
    incorrect = 0


    def prints(x, y, text, size, bold):
        font = pygame.font.SysFont("arial", size, bold=bold)
        to_blit = font.render(text, False, (0, 0, 0))
        gw.blit(to_blit, (x, y))


    class Button:
        def __init__(self, x, y, w, h, text, background_color, foreground_color):
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.text = text
            self.bg = background_color
            self.fg = foreground_color
            self.check_hover()
            self.draw()

        def draw(self):
            pygame.draw.rect(gw, self.bg, (self.x, self.y, self.w, self.h))
            prints(self.x, self.y, self.text, 30, False)

        def check_hover(self):
            x, y = pygame.mouse.get_pos()
            if ((x > self.x) and (x < (self.x + self.w))) and ((y > self.y) and (y < (self.y + self.h))):
                self.bg = (189, 183, 107, 255)
                return True


    for row in cursor:
        question_list.append(row[0])
        option1_list.append(row[1])
        option2_list.append(row[2])
        option3_list.append(row[3])
        option4_list.append(row[4])

    conn.close()

    while run:
        gw.fill((255, 255, 255))
        try:
            prints(10, 10, f"{question + 1}. {question_list[question][:-1]}", 40, True)
            opt1 = Button(10, 90, 780, 35, f"A: {option1_list[question][:-1]}", (169, 169, 169, 255), (255, 255, 255))
            opt2 = Button(10, 170, 780, 35, f"B: {option2_list[question][:-1]}", (169, 169, 169, 255), (255, 255, 255))
            opt3 = Button(10, 250, 780, 35, f"C: {option3_list[question][:-1]}", (169, 169, 169, 255), (255, 255, 255))
            opt4 = Button(10, 330, 780, 35, f"D: {option4_list[question][:-1]}", (169, 169, 169, 255), (255, 255, 255))
        except IndexError:
            prints(10, 50,  "All done", 30, True)
            prints(10, 200, f"Correct:- {correct}", 30, False)
            prints(10, 350, f"Incorrect:- {incorrect}", 30, False)
        pygame.display.update()
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

            if i.type == pygame.MOUSEBUTTONDOWN:
                if opt1.check_hover():
                    correct += 1
                    question += 1
                if opt2.check_hover():
                    incorrect += 1
                    question += 1
                if opt3.check_hover():
                    incorrect += 1
                    question += 1
                if opt4.check_hover():
                    incorrect += 1
                    question += 1
    pygame.quit()
    return correct
score=main()
print(score)
with open("tempscore","w") as file:
    file.write(str(score))