from requests import get
#baixa todas as imagens de uma categoria(travel__world-desktop-wallpapers) por página
#para mudar a categoria basta mudar no primeiro get e a quantidade de páginas(xx) conforme o site
nome = 0
for xx in range(1,60):
    a = get('https://www.hdwallpapers.in/travel__world-desktop-wallpapers/page/'+str(xx))
    if a.status_code == 200:
        l1 = []
        l2 = []
        l3 = []
        l4 = []
        b = tuple(a.text)
        salvamento = r"C:\Users\Daniel\Desktop\aprendizado python\teste1 requests (imagesdownloader)\wallpaper desktop\Nature\\"

        for i, v in enumerate(b):
            if str(''.join(b[i : i+13])) == 'class="thumb"':
                l1.append(''.join(b[i : i+200]))

        for cc in l1:
            a = False
            for i,ccc in enumerate(cc):
                if cc[i:i+7] == 'href="/':
                    a = True
                if a:
                    l3.append(cc[i+7])
                if str(''.join(cc[i+8:i+24])) == '-wallpapers.html':
                    break
            l4.append(str(''.join(l3[:])))
            l3.clear()

        for c in l4:
            bb = get('https://www.hdwallpapers.in/download/'+c+'-1920x1080.jpg')#caso a página não exista o site retorna a homepage com status 200
            urlurl = 'https://www.hdwallpapers.in/download/'+c+'-1920x1080.jpg' #e se faz necessário a checagem (bb.url == urlurl)
            if bb.status_code == 200 and bb.url == urlurl:
                nome += 1
                with open(salvamento+'image'+str(nome)+'.jpg', 'wb') as f:
                    f.write(bb.content)
print('FIM')
