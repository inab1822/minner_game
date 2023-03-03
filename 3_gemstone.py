# 보석 이미지 불러오기

import os
import pygame


# 보석 클래스
class Gemstone(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(center = position)


def setup_gemstone():
    # 작은 금
    small_gold = Gemstone(gemstone_images[0],(200,380)) # 0번째 이미지를 (200,380)위치에
    gemstone_group.add(small_gold) # 그룹에 추가
    
    # 큰 금
    gemstone_group.add(Gemstone(gemstone_images[1],(300,500)))
    
    # 돌
    gemstone_group.add(Gemstone(gemstone_images[2],(300,380)))
    
    # 다이아몬드
    gemstone_group.add(Gemstone(gemstone_images[3],(900,420)))




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

# 4개 보석 이미지 불러오기 (작은 금, 큰 금, 돌, 다이아몬드)
gemstone_images = [
    pygame.image.load(os.path.join(currnet_path,"small_gold.png")), # 작은 금
    pygame.image.load(os.path.join(currnet_path,"big_gold.png")), # 큰 금
    pygame.image.load(os.path.join(currnet_path,"stone.png")), # 돌
    pygame.image.load(os.path.join(currnet_path,"diamond.png"))] # 다이아몬드

# 보석 그룹
gemstone_group = pygame.sprite.Group()
setup_gemstone() # 게임에 원하는 만큼의 보석을 정의

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
    
    gemstone_group.draw(screen) # 그룹내 모든 스프라이트를 screen에 그림
    
    pygame.display.update() # 업데이트       
            

pygame.quit() # 게임 종료