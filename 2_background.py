# 배경 이미지 설정

import os
import pygame

# 초기화 과정
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Gold Miner')

# fps값 설정
clock = pygame.time.Clock()

# 배경이미지 불러오기
currnet_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
background = pygame.image.load(os.path.join(currnet_path, 'background.png'))

# game 루프
running = True
# running이 True이면 즉, 게임이 돌고 있으면 계속 반복
while running:
    
    clock.tick(30) # fps 값이 30으로 고정
    
    # X를 눌러 게임을 끄면
    # running이 False로 바뀌며 while문 종료
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 배경이미지 0,0 위치에 적용
    screen.blit(background,(0,0))
    pygame.display.update() # 업데이트       
            

pygame.quit() # 게임 종료