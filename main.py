from requests import get,post,Session
from bs4 import BeautifulSoup as parser
from re import search,findall
import os
import sys
url = 'https://mbasic.facebook.com'
loop=0

def login(cookie=None):
  cook = input(
    '(•) Your Facebook Cookies: '
    )
  cookie = {'cookie':cook}
  try:
    ceklogin = parser(
      get(
        url+'/me',cookies=cookie
        ).content,'html.parser'
      ).find('title').text
    if 'Facebook - Masuk atau Daftar' in str(ceklogin):
      exit(
        '(!) Invalid Cookies'
        )
    else:
      print(
        '(✓) Login As {}'.format(ceklogin)
        )
      with open('Data/cookies.txt','w') as scookie:
        scookie.write(cook);scookie.close()
      menu()
  except:
    exit(
        '(!) Invalid Cookies'
        )

def target_react(urlz,type_react):
  global loop
  cook = open('Data/cookies.txt','r').read()
  cookie = {
    'cookie':cook
  }
  get_react = parser(
    get(url+'{}'.format(urlz),cookies=cookie).content,'html.parser'
    )
  for reaction in get_react.find_all('a',href=True):
    if 'Tanggapi' in reaction:
      choose = parser(
        get(url+'{}'.format(reaction['href']),cookies=cookie).content,'html.parser'
        ).find_all('a')
      if(
        type_react in['01','1']
        ):
          execute_like = get(
            url+'{}'.format(choose[1]['href']),cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(execute_like.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini Sekarang'
              )
          else:
            loop+=1
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
      elif(
        type_react in['02','2']
        ):
          execute_super = get(
            url+'{}'.format(choose[2]['href']),cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(execute_super.content):
            exit(
              '(!) Anda Tidak Dapat Menggunakan Fitur Ini Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
            
      elif(
        type_react in['03','3']
        ):
          execute_care = get(
            url+'{}'.format(choose[3]['href']),cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang' in str(execute_care.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
              
      elif(
        type_react in['04','4']
        ):
          execute_haha = get(
            url+'{}'.format(choose[4]['href']),cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang' in str(execute_haha.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
      elif(
        type_react in['05','5']
        ):
          execute_wow = get(
            url+'{}'.format(choose[5]['href']),cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang' in str(execute_wow.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
      elif(
        type_react in['06','6']
        ):
          execute_sad = get(
            url+'{}'.format(choose[6]['href']),cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang' in str(execute_sad.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
                
      elif(
        type_react in['07','7']
        ):
          execute_angry = get(
            url+'{}'.format(choose[7]['href']),cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang' in str(execute_angry.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
    else:
      pass

  if 'Lihat Berita Lain' in str(get_react):
    target_react(get_react.find('a',string='Lihat Berita Lain')['href'],type_react)

def timeline_react(urlx,type_react):
  global loop
  cook = open('Data/cookies.txt','r').read()
  cookie = {
    'cookie': cook
  }
  for i in urlx.find_all('a'):
    if 'Tanggapi' in str(i):
      if(
        type_react in['01','1']
        ):
          choose = parser(
            get(url+i['href'],cookies=cookie).content,'html.parser'
            ).find_all('a')
          execute_like = get(
            url+choose[1]['href'],cookies=cookie
            )
          title = search(r'<title>(.*?)</title>',str(execute_like.content))[1]
          if title == 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang':
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
      elif(
        type_react in['02','2']
        ):
          choose = parser(
            get(url+i['href'],cookies=cookie).content,'html.parser'
            ).find_all('a')
          execute_love = get(
            url+choose[2]['href'],cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(execute_love.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
      elif(
        type_react in['03','3']
        ):
          choose = parser(
            get(url+i['href'],cookies=cookie).content,'html.parser'
            ).find_all('a')
          execute_care = get(
            url+choose[3]['href'],cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(execute_care.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
              
      elif(
        type_react in['04','4']
        ):
          choose = parser(
            get(url+i['href'],cookies=cookie).content,'html.parser'
            ).find_all('a')
          execute_haha = get(
            url+choose[4]['href'],cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(execute_haha.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
      elif(
        type_react in['05','5']
        ):
          choose = parser(
            get(url+i['href'],cookies=cookie).content,'html.parser'
            ).find_all('a')
          execute_wow = get(
            url+choose[5]['href'],cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(execute_wow.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
      elif(
        type_react in['06','6']
        ):
          choose = parser(
            get(url+i['href'],cookies=cookie).content,'html.parser'
            ).find_all('a')
          execute_sad = get(
            url+choose[6]['href'],cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(execute_sad.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini  Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
      elif(
        type_react in['07','7']
        ):
          choose = parser(
            get(url+i['href'],cookies=cookie).content,'html.parser'
            ).find_all('a')
          execute_angry = get(
            url+choose[7]['href'],cookies=cookie
            )
          if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in str(execute_angry.content):
            exit(
              '\n(!) Anda Tidak Dapat Menggunakan Fitur Ini Sekarang'
              )
          else:
            loop+=1 
            print(
              f'\n(INFO) Succes Reaction - {loop}',end=''
              )
      
  if 'Lihat Berita Lain' in str(urlx):
    nextContent = urlx.find('a',string='Lihat Berita Lain')['href']
    getNext = parser(
      get(url+nextContent,cookies=cookie).content,'html.parser'
      )
    timeline_react(getNext,type_react)

def menu():
  cook = open('Data/cookies.txt','r').read()
  cookie = {
    'cookie':cook
  }
  if len(cook) == 0:
    return login(True)
  try:
    data = get(
      url+'/me',cookies=cookie
      ).text
    name = search(r'<title>(.*?)</title>',data)[1]
    username = search(r'name="target" value="(.*?)"',data)[1]
  except:
    return login(True)
  os.system('clear')
  print('\t\t[F a c e b o o k B o t]\n')
  print(f'(•) Name: {name}')
  print(f'(•) Username: {username}')
  print(
  '''
  {1} Spam Reaction Target User 
  {2} Spam Reaction TimeLine
  '''
  )
  cursor = input(
    '(?)\t>> '
    )
  if(
    cursor in['01','1']
    ):
      print(
        '\n{01} Likes\n{02} Super\n{03} Peduli\n{04} Haha\n{05} Wow\n{06} Sedih\n{07} Marah'
        )
      type_react = input(
        '\n(?)\t>> '
        )
      target = input('(?) username or id: ')
      urltarget = url+'/{}'.format(target)
      get_ = parser(
        get(urltarget,cookies=cookie).content,'html.parser'
        )
      target_react(get_.find('a',string='Linimasa')['href'],type_react)
      
  elif(
    cursor in['02','2']
    ):
      print(
        '\n{01} Likes\n{02} Super\n{03} Peduli\n{04} Haha\n{05} Wow\n{06} Sedih\n{07} Marah'
        )
      type_react = input(
        '\n(?)\t>> '
        )
      urlx = parser(
        get(url,cookies=cookie).content,'html.parser'
        )
      timeline_react(urlx,type_react)
  
if __name__=='__main__':
  menu()