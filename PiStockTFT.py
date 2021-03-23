import pygame
import requests
from bs4 import BeautifulSoup
import time

pygame.init()

#Delay
time.sleep(10)

X = 640
Y = 480

# because this has no frame to quit, you will have to quit using CTRL+C in PowerShell
display_surface = pygame.display.set_mode((X, Y), pygame.FULLSCREEN) 
pygame.mouse.set_cursor((8,8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

# colors
white = (255, 255, 255) 
red = (255, 0, 0)
green = (0 , 255, 0)
black = (0, 0, 0)
grey = (220, 220, 220)

def tickers():
    i = 1
    while True:
        # ticker1
        url = 'https://finance.yahoo.com/quote/PSTH'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        price = float(soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.replace(',',''))
        open_ = float(soup.find_all('td', {'class': 'Ta(end) Fw(600) Lh(14px)'})[0].find('span').text.replace(',',''))
        change_ = float((price / open_) - 1)
        o_ch = ("{:.2f}".format(price - open_))
        percent_change = ("{:.2f}".format((change_ * 100)) + '%')
        font = pygame.font.Font('/home/pi/Desktop/Code New Roman b.otf', 40, bold = True)
        if change_ == 0:
            ourColor = white
        elif change_ > 0:
            ourColor = green
        else:
            ourColor = red
        # ticker2
        url2 = 'https://finance.yahoo.com/quote/PLUG?p=PLUG'
        response2 = requests.get(url2)
        soup2 = BeautifulSoup(response2.text, 'lxml')
        price2 = float(soup2.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.replace(',',''))
        open_2 = float(soup2.find_all('td', {'class': 'Ta(end) Fw(600) Lh(14px)'})[0].find('span').text.replace(',',''))
        change_2 = float((price2 / open_2) - 1)
        o_ch2 = ("{:.2f}".format(price2 - open_2))
        percent_change2 = ("{:.2f}".format((change_2 * 100)) + '%')
        if change_2 == 0:
            ourColor2 = white
        elif change_2 > 0:
            ourColor2 = green
        else:
            ourColor2 = red
        # ticker3
        url3 = 'https://finance.yahoo.com/quote/PLTR?p=PLTR'
        response3 = requests.get(url3)
        soup3 = BeautifulSoup(response3.text, 'lxml')
        price3 = float(soup3.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.replace(',',''))
        open_3 = float(soup3.find_all('td', {'class': 'Ta(end) Fw(600) Lh(14px)'})[0].find('span').text.replace(',',''))
        change_3 = float((price3 / open_3) - 1)
        o_ch3 = ("{:.2f}".format(price3 - open_3))
        percent_change3 = ("{:.2f}".format((change_3 * 100)) + '%')
        if change_3 == 0:
            ourColor3 = white
        elif change_3 > 0:
            ourColor3 = green
        else:
            ourColor3 = red
        # ticker 4
        url4 = 'https://finance.yahoo.com/quote/SE?p=SE'
        response4 = requests.get(url4)
        soup4 = BeautifulSoup(response4.text, 'lxml')
        price4 = float(soup4.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text.replace(',',''))
        open_4 = float(soup4.find_all('td', {'class': 'Ta(end) Fw(600) Lh(14px)'})[0].find('span').text.replace(',',''))
        change_4 = float((price4 / open_4) - 1)
        o_ch4 = ("{:.2f}".format(price4 - open_4))
        percent_change4 = ("{:.2f}".format((change_4 * 100)) + '%')
        if change_4 == 0:
            ourColor4 = white
        elif change_4 > 0:
            ourColor4 = green
        else:
            ourColor4 = red
        #adds the plus sign before a positive number
        if price-open_ > 0:
            plus = '+'
        else:
            plus = ''
        if price2-open_2 > 0:
            plus2 = '+'
        else:
            plus2 = ''
        if price3-open_3 > 0:
            plus3 = '+'
        else:
            plus3 = ''
        if price4-open_4 > 0:
            plus4 = '+'
        else:
            plus4 = ''
        # what to display
        stockname = font.render('PSTH' + '    ' + ("{:.2f}".format(price)), True, white)
        stocknameRect = stockname.get_rect()
        stocknameRect.center = (X // 2, 70)
        text = font.render('('+plus+str(o_ch) + ', ' +plus+percent_change+')', True, ourColor)
        textRect = text.get_rect()
        textRect.center = (X // 2, 110)
        
        stockname2 = font.render('PLUG' + '    ' + ("{:.2f}".format(price2)), True, white)
        stocknameRect2 = stockname2.get_rect()
        stocknameRect2.center = (X // 2, 170)
        text2 = font.render('('+plus2+str(o_ch2) + ', ' +plus2+percent_change2+')', True, ourColor2)
        textRect2 = text2.get_rect()
        textRect2.center = (X // 2, 210)
        
        stockname3 = font.render('PLTR' + '    ' + ("{:.2f}".format(price3)), True, white)
        stocknameRect3 = stockname3.get_rect()
        stocknameRect3.center = (X // 2, 270)
        text3 = font.render('('+plus3+str(o_ch3) + ', ' +plus3+percent_change3+')', True, ourColor3)
        textRect3 = text3.get_rect()
        textRect3.center = (X // 2, 310)
        
        stockname4 = font.render('SE ' + '    ' + ("{:.2f}".format(price4)), True, white)
        stocknameRect4 = stockname4.get_rect()
        stocknameRect4.center = (X // 2, 370)
        text4 = font.render('('+plus4+str(o_ch4) + ', ' +plus4+percent_change4+')', True, ourColor4)
        textRect4 = text4.get_rect()
        textRect4.center = (X // 2, 410)
        #data loop to display
        if i > 0:
            display_surface.fill(black)
            display_surface.blit(stockname, stocknameRect)
            display_surface.blit(text, textRect)
            display_surface.blit(stockname2, stocknameRect2)
            display_surface.blit(text2, textRect2)
            display_surface.blit(stockname3, stocknameRect3)
            display_surface.blit(text3, textRect3)
            display_surface.blit(stockname4, stocknameRect4)
            display_surface.blit(text4, textRect4)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.quit()
                    pygame.display.quit()
                    quit()
            pygame.display.update()
    i =+ 1
tickers()
