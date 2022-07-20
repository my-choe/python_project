import pygame

#초기화(반드시 필요)
pygame.init() 

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Minyoung Game")

#이벤트 루프(창 꺼짐 방지)
running = True #게임 진행중인가? 확인
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생했는가?
            running = False


# pygame 종료
pygame.quit()