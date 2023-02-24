import os, subprocess, http.server,  socketserver, threading, urllib.parse, ssl, sys
import password, gek_kl, obr, save_fail, post_get, pes



if not(os.path.exists(obr.pyti(__file__)  + 'passwords')):
    os.mkdir(obr.pyti(__file__) + 'passwords')
         
por_ad = eval('{' + open(obr.pyti(__file__) + 'por/pr_admk.txt','r').read() + '}')
por_us = eval("{" + open(obr.pyti(__file__) + 'por/pr_user.txt','r').read() + "}")

save_fail.save(obr.pyti(__file__), 'zad')
save_fail.save(obr.pyti(__file__), 'tst')
save_fail.save(obr.pyti(__file__), 'pes')
save_fail.save(obr.pyti(__file__), 'pos')
save_fail.save(obr.pyti(__file__), 'rez')


klus = threading.Lock()#ключ userof
klad = threading.Lock()
test = threading.Lock()
redg = threading.Lock()
rega = threading.Lock()#ограничения пороля админа
regu = threading.Lock()#ограничения пороля пользователя
posl = threading.Lock()#посылки



konfig = {}
konadm = {}

pos = 0

class Server(http.server.BaseHTTPRequestHandler):
    global  klus, klad, test, podg, regu, posl, pos
    
    def do_GET(self):
      
      key = self.headers.get('Cookie', '')[4:]#получения ключа


      if key in konfig:#зареган user
          
          path  = post_get.prov_put_zad(self.path)

          if self.path in ('/', '/zadac'):#меню
               html  = """<html>
                                <head>
                                      <title> Главная страница</title>
                                      <style>
                                         body{
                                                  background: #676767;
                                             }
                                         button{
                                                  width:100px;
                                               }
                                         a{
                                             background-color: #FFFFFF;
                                             border: none;
                                             color: #000000;
                                             padding: 10px 10px;
                                             text-align: center;
                                             text-decoration: none;
                                             display: inline-block;
                                             font-size: 15px;
                                             }

                                      </style>
                                </head>
                                <body>
                                      <h1><p align = left>Тестирующая система Нejudge<sup>β</sup></p></h1>
                                                <table style="text-align: left;">
                                                 <th>
                                                    <form action = "/vhd" method = "POST">
                                                            <button>Выход</button>
                                                    </form>
                                                  </th>
                                                  <th>
                                                    <form action = "/itog"  method = "GET">
                                                         <button>Итог</button>
                                                    </form>
                                                  </th>
                                              </table>""".encode('utf-8')

               for i in os.listdir(obr.pyti(__file__) + 'zad'):
                   html += ('''<p alig = left> <a href = "/zadac/''' + post_get.nach_put(i) + '''/1">''' +  i + '''</a></p>''').encode()
                                                                                 
               html += '''         <br/>
                                </body>
                            </html>'''.encode()
            
            
               klus.acquire()
               s =  gek_kl.kluch()
               konfig[s] = konfig[key]
               del  konfig[key]
               klus.release()

               self.send_response(200)              
               self.send_header('Set-Cookie' ,'key='+s +'; path=/')

               self.send_header('Content-Type', 'text/html; charset=utf-8')
               self.send_header('Content-Length', len(html))
               self.end_headers() 
               self.wfile.write(html)

          
          elif path[0]:
              zad_in_razd = obr.pyti(__file__) + '/'.join(list(path[1].split('/'))[:-1])#для всех задач
              salka = '/' + '/'.join(list(self.path[1:].split('/'))[:-1])#для сылок
              zad = obr.pyti(__file__) + path[1] + '/'
              for i in os.listdir(obr.pyti(__file__) + path[1]):
                  if i[-5:]  == '.html':
                      zad += i 
                      break
              

              html = ('''
                        <html>
                             <head>
                                 <style>
                                     body{
                                             background: #676767;
                                         }
                                     button{
                                            width:100px;
                                           }
                                     table{
                                                border-collapse: collapse;
                                          }
                                     .tr_right{
                                               background: #65994C; 
                                               color: #000;
                                             }
                                     .tr_half{
                                                  background: #FFFF00; 
                                                  color: #000;
                                               }
                                     .tr_wrong{
                                                 background: #FF0000; 
                                                 color: #000;
                                               }
                                     .bit{
                                             background-color: #FFFFFF;
                                             border: none;
                                             color: #000000;
                                             padding: 10px 10px;
                                             text-align: center;
                                             text-decoration: none;
                                             display: inline-block;
                                             font-size: 15px;
                                             }
                                     .bit_cur{
                                             background-color: #006400;
                                             border: none;
                                             color: #000000;
                                             padding: 10px 10px;
                                             text-align: center;
                                             text-decoration: none;
                                             display: inline-block;
                                             font-size: 15px;
                                             }
                                     .svet{
                                                  background: white;     
                                                  width: 100%;
                                                }

                                 </style>
                                 <title>''' + i[:-5] + '</title>').encode()
              html += ''' 

                             </head>
                             <body>
                                    <h1><p alig = left>Тестирующая система Нejudge<sup>β</sup></p></h1>
                                    <table style="text-align: left;">
                                                 <th>
                                                    <form action = "/vhd" method = "POST">
                                                            <button>Выход</button>
                                                    </form>
                                                  </th>
                                                  <th>
                                                    <form action = "/itog"  method = "GET">
                                                         <button>Итог</button>
                                                    </form>
                                                  </th>
                                    </table>
                                                                          
                                    <table style="text-align: left;">'''.encode()

              for i in range(len(os.listdir(zad_in_razd))):
                  html +=  ('''<th>   
                                 
                                     <a class = "'''+  ('bit' if str(i + 1) != list(path[1].split('/'))[-1:][0] else 'bit_cur') + '''" href="''' + salka + '/' + str(i+1) + '''">''' + str(i+1) + '''</a>
                               
                              </th>''').encode() 
              


              html += '''</table>'''.encode() + """<table class = "svet"> <tr align = left> <th>""".encode() + open( zad, 'rb').read() 
             
              html += ( '''
                     </br>
                     <form method = "POST"  action = "''' + post_get.post_swap_get(self.path, 'testk')  + '''" enctype="multipart/form-data">
                            <select name = "azk" alig = left>
                                      <option disabled="" selected="" style="display: none">Выберите язык</option>
                                      <option>g++ (C++)</option>
                                      <option>gcc (C)</option>
                                      <option>Python3.7</option>
                                      <option>RUST</option>
                                      <option>FREE Pascal</option>

                            </select>
                            <input type="file" name="fal"/>
                            <input type="submit" value="Отправить"/>
                     </form>''').encode()
              try:
                  html += '''<table border="3" width="100%" align = left >
                                    <tr>
                                         <th>Номер послыки</th><th>Номер задачи</th><th>Язык</th><th>Количество балов</th>'''.encode()
                  xxx =  os.listdir(obr.pyti(__file__) + 'rez/' +  path[1][3:] + '/' + konfig[key][0])
                  xxx.sort()
                  for i in xxx[::-1]:
                      html += open(obr.pyti(__file__) + 'rez/'+ path[1][3:] + '/' + konfig[key][0] + '/' + i, 'rb').read()
                      
              except:
                  html 
              html += '''</th>
                             </tr>
                                </table>
                                    </body>
                                        </html>'''.encode()

              klus.acquire()#ограничения генирации ключей
              s =  gek_kl.kluch()
              konfig[s] = konfig[key]
              del  konfig[key]
              klus.release()#снятия на ограничения

              self.send_response(200)              
              self.send_header('Set-Cookie' ,'key='+s +'; path=/')

              self.send_header('Content-Type', 'text/html; charset=utf-8')
              self.send_header('Content-Length', len(html))
              self.end_headers() 
              self.wfile.write(html)


          else:#странца не найдена
              
              html = '''
                      <html>
                            <head>
                                    <title>404 error</title>
                                    <style>
                                            body{
                                                  background: #676767;
                                                 }
                                            p{
                                                     font-size: 90px;
                                                     margin-top: 45%;
                                             }


                                    </style>
                            </head>
                            <body>
                                 <h1><p align = center>404 страница не найдена</p></h1>
                                 <a href = "/" > вернутся назад</a>
                            </body>
                        </html>'''.encode()
              

                            
              klus.acquire()
              s =  gek_kl.kluch()
              konfig[s] = konfig[key]
              del  konfig[key]
              klus.release()   
              
              self.send_response(200)
              self.send_header('Content-Type', 'text/html; charset=utf-8')
              self.send_header('Content-Length', len(html))
              self.send_header('Set-Cookie' ,'key='+s +'; path=/')
              self.end_headers() 
              self.wfile.write(html)



      
      
      
      
      
      
      
      
      else:# Не зареган товарищь 
            
            if self.path ==  '/':
                html =  '''
                <html>
                    <head>
                        <title>login</title>
                        <style>
                              body{
                                       background: #676767;
                                   }
                              button{
                                      width:210px;
                                      height:29px;            
                                    }

                                      
                              input{
                                       width:210px;
                                       height:29px;
                                   } 
                              p{
                                         margin-bottom: 0.5%;
                               }
                        </style>
                    </head>
                    <body>
                              <h1><p align = center>Вход в тестирующую систему <br> Нejudge<sup>β</sup></p></h1>'''.encode()
                if key != '':
                          html += """<p align = center>
                                        <table>
                                                 <td  bgcolor="DC143C"><font size = "4">Логин или пaроль в введен не правильно</font></tb>
                                        </table>
                               </p>""".encode('utf-8')
                html+='''
                              <form action = '/log' method = "POST">
                                      <p align = center><input name = "log" placeholder = "login" autocomplete="off"/></p>
                                      <p align = center><input name = "por" placeholder = "Пароль" type="password" autocomplete="off"/></p>
                                      <p align = center><button>Войти</button></p>
                              </form>
                              
                              <p align = center><input type="button" value="Регистрация" onclick="window.location.href = '/reg';"/></p>
                           
                    </body>
                </html>'''.encode()

                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', len(html))
                self.end_headers() 
                self.wfile.write(html)
            
            

            elif self.path == '/reg':
                html = '''<html>
                                <head>
                                      <title>Регистарция</title>
                                      <style>
                                           body{
                                                background: #676767;
                                               }
                                           button{
                                                     width:210px;
                                                     height:29px;
                                                     radius: 5px;
                                                }

                                           input{
                                                     width: 210px;
                                                     height: 29px
                                                     radius: 5px;
                                                }

                                      </style>
                                </head>
                                <body>
                                      <h1><a alig = left>Регистрация в тестирующую систему Нejudge<sup>β</sup></a></h1>
                                      
                                      <form action = '/reg' method = "POST">
                                                    <p align = left><input name = "nam" placeholder = "Имя" autocomplete="off" minlength = "3" required oninvalid="this.setCustomValidity('Поле не должно быть пустым')" /></p>
                                                    <p align = left>Имя пользвателя должно быть больше 3 символов</p>
                                                    <p align = left><input name = "nam" placeholder = "login" autocomplete="off" minlength = "4" required oninvalid="this.setCustomValidity('Поле не должно быть пустым')" /></p>
                                                    <p align = left>login должен быть больше 3 символов</p>
                                                    <p align = left><input name = "nam" placeholder = "Пароль" type = "password" autocomplete="off" minlength="6" required oninvalid="this.setCustomValidity('Поле не должно быть пустым')"  /></p>
                                                    <p align = left>Пароль должен быть больше 5 символов</p>
                                                    <p align = left><input name = "nam" placeholder = "Повторить пaроль" type = "password" autocomplete="off" required oninvalid="this.setCustomValidity('Поле не должно быть пустым')" /></p>
                                                    <p align = left><button>Регистрация</button></p>
                                      </form>
                                </body>
                            </html>'''.encode('utf-8')


                self.send_response(200)
                self.send_header('Content-Type', 'text/html; charset=utf-8')
                self.send_header('Content-Length', len(html))
                self.end_headers() 
                self.wfile.write(html)
                             

            
            
            else:
              
                self.send_response(302)
                self.send_header('Location', '/')
                self.end_headers()

    


                                      

            
   
    def do_POST(self):
            keu = str(self.headers.get('Cookie', ''))[4:]
            
            if keu  in  konfig: 
                  path = post_get.in_get(self.path)
                  if path[0]:
                       global pos
                       l = int(self.headers.get('Content-Length'))
                       l = self.rfile.read(l)
                       print(l.decode())
                       lang_and_code = obr.fail_leng(l)
                       print(lang_and_code)
                       posl.acquire()
                       pos += 1
                       folder = obr.pyti(__file__) + 'pos' + path[1][3:] + '/'  + str(pos) 
                       pesok =  obr.pyti(__file__) + 'pes' + path[1][3:]
                       test =  obr.pyti(__file__) + 'tst' + path[1][3:]
                       rez =  obr.pyti(__file__) + 'rez' + path[1][3:] + '/' +konfig[keu][0]
                       print(folder)
                       os.mkdir(folder)

                       threading.Thread(target = pes.pes, args=( pesok, pos, folder, test, rez, lang_and_code)).start()
                       posl.release()
                       
                       klus.acquire()#ограничения генирации ключей
                       s =  gek_kl.kluch()
                       konfig[s] = konfig[keu]
                       del  konfig[keu]
                       klus.release()#снятия на ограничения



                       self.send_response(302)
                       self.send_header('Set-Cookie' ,'key='+s +'; path=/')
                       self.send_header('Location', '/zadac'  +  self.path[6:])
                       self.end_headers()
                       
                  elif self.path == '/vhd':

                      if keu in konfig:
                           del konfig[keu] 
                    
                      self.send_response(302)
                      self.send_header('Set-Cookie','key=''; path=/')#выход
                      self.send_header('Location', '/')
                      self.end_headers()
      


            else:
                if self.path == '/log':
                    keu = '0'
                    l = int(self.headers.get('Content-Length'))
                    s = self.rfile.read(l)
                    print(s)
             
                    log, por  = s[4:].split(b'&por=')
                    log, por  = urllib.parse.unquote(log.decode()), urllib.parse.unquote(por.decode())
            
                    if (log in por_us) and (por_us[log][0] == password.encoding_password(por)):
                   
                         s = gek_kl.kluch()
                         konfig[s] =log,  por_us[log][1]
                         keu = s 
                                
                    self.send_response(302)
                    self.send_header('Set-Cookie' ,'key='+keu +'; path=/')#вход 
                    self.send_header('Location', '/')
                    self.end_headers()

                elif self.path == '/reg':
                   flag = False
                   data = self.rfile.read(int(self.headers.get('Content-Length')))
                   data = list(data[4:].split(b'nam='))
                   for i in  range(len(data)):
                          data[i] = urllib.parse.unquote(obr.reg(data[i].decode()))

                   if obr.regist(data):
                       regu.acquire()#ограничение потока
                       if data[1] not in os.listdir(obr.pyti(__file__) + 'passwords'):
                           open(obr.pyti(__file__) + 'por/pr_user.txt' ,'a').write((',\n' if len(por_us) > 0 else '') + """'""" + data[1] + """':('""" + password.encoding_password(data[2]) + """','""" + data[0] + """')""")
                            
                           print(data[2])
                           por_us[data[1]] = (password.encoding_password(data[2]), data[0])
                           flag = True 
                       regu.release()#Снимаем ограничения

                   if flag:
                       html = '''<html>
                                <head>
                                      <title>Регистарция</title>
                                      <style>
                                           body{
                                                background: #676767;
                                               }
                                           button{
                                                    width:210px;
                                                 }
                                           table{
                                                  background: white;
                                                  margin-left: 5%;
                                                  width: 90%;
                                                }
                                            
                                                                                       
                                           th{
                                                padding-left: 0.5%;
                                             }
                                           .th1{
                                               padding-top: 0.5%;
                                              }



                                           a{
                                                  text-decoration: none;
                                                  background-color: #696969;
                                                  color: #FFFFFF; 
                                                  padding: 3px;
                                            }
                                           a:hover{
                                                  text-decoration: none;
                                                  background-color: #808080; 
                                                  color: #FFFFFF; 
                                                  padding: 3px;                                             
                                                  }



                                      </style>
                                </head>
                                <body>
                                   <table>
                                        <tr align = left>
                                             <th>
                                                <h2>Регистрация успешно выполнена</h2>
                                                <h2><a href = "/"><span class="link">Войти в главное меню</span></a></h2>
                                             </th> 
                                        </tr>
                                   </table>
                                </body>
                                </head>
                                </html>'''.encode()
                   else:
                           html = '''<html>
                                <head>
                                      <title>Регистарция error</title>
                                      <style>
                                           body{
                                                background: #676767;
                                               }
                                           button{
                                                    width:210px;
                                                 }
                                           table{
                                                  background: white;
                                                  margin-left: 5%;
                                                  width: 90%;
                                                }
                                           .indetli{
                                                padding-left: 2%;
                                             }
                                           
                                           th{
                                                padding-left: 0.5%;
                                             }
                                           .th1{
                                               padding-top: 0.5%;
                                              }



                                           a{
                                                  text-decoration: none;
                                                  background-color: #696969;
                                                  color: #FFFFFF; 
                                                  padding: 3px;
                                            }
                                           a:hover{
                                                  text-decoration: none;
                                                  background-color: #808080; 
                                                  color: #FFFFFF; 
                                                  padding: 3px;                                             
                                                  }
                                      </style>
                                </head>
                                <body>
                                   <table>
                                         <tr align = left>
                                             <th class = "th1"><h2><font color = "#FF0000">В регистрации отказано</font></h2></th>
                                         </tr>
                                         <tr align = left>
                                            <th><h2>Возможные ошибки</h2></th>
                                         </tr>
                                         <tr align = left>
                                            <th class = "indetli"><h2><li>Вы неправильно набран логин.</li></h2></th>
                                         </tr>
                                         <tr align = left>
                                            <th class = "indetli"><h2><li>Логин такой уже существует.</li></h2></th>
                                         </tr>
                                         <tr align = left>
                                             <th class = "indetli"><h2><li>Пароли не совподают.</li></h2></th>
                                         </tr>
                                         <tr align = left>
                                             <th class = "indetli"><h2><li>Логин или пароль слишком маленький.</li></h2></th>
                                         </tr>
                                         <tr align = left>
                                             <th class = "indetli"><h2><li>Имя пользователя слишком маленькое.</li></h2></th>
                                         </tr>
                                         <tr align = left>
                                             <th class = "indetli"><h2><li>В одной из полях регистраци содержат запрещенные сиволы.</li></h2></th>
                                         </tr>

                                         <tr align = left>
                                                <th><h2><a href = "/"><span class="link">Вернутся назад</span></a></h2></th><th><th><h2><a href = "/reg"><span class="link">Попробовать сново</span></a></h2></th>
                                         </tr>
                                   </table>
                                </body>
                                </head>
                                </html>'''.encode()
 


                
                   self.send_response(200)
                   self.send_header('Content-Type', 'text/html; charset=utf-8')
                   self.send_header('Content-Length', len(html))
                   self.end_headers() 
                   self.wfile.write(html)
           
                

             
            

            



    










class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer): #ThreadingMixIn нужен для потоков, если без потоков нужно убрать
    assert""" def get_request(self):# для шифорвания поролей и https подрубать толко если есть сертификатик
        #принимаем сокет
        sock, addr = self.socket.accept()
        #создаем обертку для шифрования
        sock = ssl.wrap_socket(sock, server_side=True, keyfile='key.txt', certfile='cert.txt')
        #возвращаем "как было"
        return sock, addr"""

    pass



if __name__ == "__main__":
     class ThreadingHTTPServer(socketserver.ThreadingMixIn, http.server.HTTPServer): 
         if "-https" in sys.argv:
                def get_request(self):
                    sock, addr = self.socket.accept()
                    sock = ssl.wrap_socket(sock, server_side=True, keyfile='key.txt', certfile='cert.txt')
                    return sock, addr
         pass

     ThreadingHTTPServer(('', 8080), Server).serve_forever()


                     

