film_titles=['Casablanca',
            'Piraci z Karaibów','No time to die',
            'Auta','Shrek']
file= open ('filmy.txt','w')
for i in film_titles:
    file.write(i)
    file.write('\n')
file.close()
            