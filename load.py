import json
import urllib.request as req
data = json.load(open('popular_movies.json'))
i = 0
M_dat = {}
for movie in data:
    genre = movie['genres']
    title = movie['title']
    image_path = movie['poster_path']
    image_url = "https://image.tmdb.org/t/p/w600_and_h900_bestv2{}".format(image_path)    
    try:
        print(title,image_url)
        image_local = 'Img&Label/{} {}.jpg'.format(i, title)
        req.urlretrieve(image_url, image_local)      
    except:
        pass       
    M_dat[title] = {'genre ': genre, 'poster ': image_url, 'local':image_local}
        
    for line in M_dat.items():
        str_genre = '\n'.join(genre)
        file = open('Img&Label/%i %s.jpg.txt' %(i, title), 'w')
        file.write(str_genre)
        file.close
        
    i+=1