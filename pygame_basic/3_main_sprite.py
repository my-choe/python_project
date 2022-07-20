import pygame

#초기화(반드시 필요)
pygame.init() 

#화면 크기 설정
screen_width = 480 #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width, screen_height))


#화면 타이틀 설정
pygame.display.set_caption("Minyoung Game")

#배경 이미지 불러오기
background = pygame.image.load("D:/PythonWorkspace/pygame_basic/background.png")

#캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/PythonWorkspace/pygame_basic/character.png")
character_size = character.get_rect().size #캐릭터 이미지 크기
character_width = character_size[0] #캐릭터 가로 크기
character_height = character_size[1] #캐릭터 세로 크기
character_x_pos = (screen_width / 2) - (character_width / 2)#화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height - character_height #화면 세로 크기 가장 아레에 해당하는 곳에 위치



#이벤트 루프(창 꺼짐 방지)
running = True #게임 진행중인가? 확인
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생했는가?
            running = False
    
    screen.blit(background, (0, 0)) #게임 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() #게임화면 다시 그리기(반드시 계속 호출되어야 함)


# pygame 종료
pygame.quit()