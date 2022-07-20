import pstats
from re import I
import pygame

#초기화(반드시 필요)
pygame.init() 

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Minyoung Game")

# FPS
clock = pygame.time.Clock()

#배경 이미지 불러오기
background = pygame.image.load("D:/PythonWorkspace/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size #캐릭터 이미지 크기
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)#화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아레에 해당하는 곳에 위치


#이동할 좌표
to_x = 0
to_y = 0

#이동 속도
character_speed = 0.6

#이벤트 루프(창 꺼짐 방지)
running = True #게임 진행중인가? 확인
while running:
    dt = clock.tick(60) # 게임화면의 초당 프레임 수 설정

    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생했는가?
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    #프레임 수에 따라 보정하기 위해 dt 곱하기
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계값 처리
    if character_x_pos < 0 :
        character_x_pos = 0 
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    #세로 경계값 처리
    if character_y_pos < 0 :
        character_y_pos = 0 
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height




    screen.blit(background, (0, 0)) #게임 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면 다시 그리기(반드시 계속 호출되어야 함)


# pygame 종료
pygame.quit()