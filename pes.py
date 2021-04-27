import os, shutil


lang = {'g++ (C++)':'.cpp',
        'gcc (C)':'.c',
        'Python3.7':'.py',
        'RUST':'.rs',
        "FRI Pascal":".pas"}


def pes(pesok, nom_pos, folder, tst, rez, lang_and_code):
    open(folder + '/' + str(nom_pos) + lang[lang_and_code[0]], 'w').write(lang_and_code[1])
    import sys
    sys.path.insert(0, pesok)
    import test
    s = test.pes(folder, tst, nom_pos, lang[lang_and_code[0]])
    k = 0 
    for i in  s:
        if i == 1: 
            k += 1
    if k  ==  len(s):
        clas = 'class = "tr_right"'
    elif k != 0:
        clas = 'class = "tr_half"'
    else:
        clas = 'class = "tr_wrong"'
    try:

             os.mkdir(rez)
             m = ''
    
    except:
        m = open(rez + '/' +  'rez.html','r').read()
    
    m = '''<tr ''' + clas + '''><th>''' + str(nom_pos)  +  ''' </th><th>''' + pesok.split('/')[-1:][0] + '''</th><th>''' + lang_and_code[0] + '''</th><th>''' + str(k) +  ''' in ''' + str(len(s))   + '''</th></tr> ''' + m
    open(rez + '/' +  'rez.html','w').write(m)
    shutil.rmtree('/'.join(folder.split('/')[:-1]))



        


