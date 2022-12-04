#!/usr/bin/env python
# coding: utf-8

# # Write a python program to display all the header tags from wikipedia.org.
# 

# In[1]:


#importing the required libraries
from bs4 import BeautifulSoup
import requests


# In[2]:


#sending request to get the html code of the webpage
page=requests.get("https://en.wikipedia.org/wiki/Main_Page")


# In[3]:


#diplaying whether the page url is scrapable/accessible
page


# In[4]:


#getting page html content
soup=BeautifulSoup(page.content)
soup


# In[5]:


#finding all the header tags and assigning them to a variable
header_tags=soup.find_all('span',class_='mw-headline')


# In[6]:


#calling the variable To display the header tags
header_tags


# In[ ]:





# # Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[7]:


#importing the required libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[8]:


#sending request to get the html code of the webpage
page1=requests.get("https://www.imdb.com/chart/top")


# In[9]:


#diplaying whether the page url is scrapable/accessible
page1


# In[53]:


#getting page html content
soup1=BeautifulSoup(page1.content,'html.parser')
soup1


# In[62]:


#creating empty lists for storing the required data
Movie = []
Year = []
Rating = []


# In[68]:


#Under Title column there is title & year, for only getting the title tag "a" is used along with 'titlecolum' class
#Movie year is under the same title column parent tag, with a seperate class "secondaryInfo"
#
movie_name = soup1.select("td.titleColumn a")
for i in movie_name:
    Movie.append(i.get_text())
movie_year = soup1.find_all('span',class_='secondaryInfo')
for i in movie_year:
    Year.append(i.get_text().replace('\n','').replace('(','').replace(')',''))
movie_rating = soup1.find_all('td',class_="ratingColumn imdbRating")
for i in movie_rating:
    Rating.append(i.get_text().replace('\n',''))


# In[69]:


Top100 = pd.DataFrame({})
Top100['Movie'] = Movie[0:100]
Top100['Year'] = Year[0:100]
Top100['Rating'] = Rating[0:100]


# In[65]:


Top100


# In[ ]:





# # Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.
# 

# In[83]:


#importing the required libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[84]:


#sending request to get the html code of the webpage
page2=requests.get("https://www.imdb.com/india/top-rated-indian-movies/")


# In[85]:


#diplaying whether the page url is scrapable/accessible
page2


# In[86]:


#getting page html content
soup2=BeautifulSoup(page2.content,'html.parser')
soup2


# In[87]:


#creating empty lists for storing the required data
India_Movie = []
India_Year = []
India_Rating = []


# In[88]:


#Under Title column there is title & year, for only getting the title tag "a" is used along with 'titlecolum' class
#Movie year is under the same title column parent tag, with a seperate class "secondaryInfo"
#
movie_name = soup2.select("td.titleColumn a")
for i in movie_name:
    India_Movie.append(i.get_text())
movie_year = soup2.find_all('span',class_='secondaryInfo')
for i in movie_year:
    India_Year.append(i.get_text().replace('\n','').replace('(','').replace(')',''))
movie_rating = soup2.find_all('td',class_="ratingColumn imdbRating")
for i in movie_rating:
    India_Rating.append(i.get_text().replace('\n',''))


# In[89]:


India_Top100 = pd.DataFrame({})
India_Top100['Movie'] = India_Movie[0:100]
India_Top100['Year'] = India_Year[0:100]
India_Top100['Rating'] = India_Rating[0:100]


# In[90]:


India_Top100


# In[ ]:





# # Write s python program to display list of respected former presidents of India(i.e. Name , Term of office) from https://presidentofindia.nic.in/former-presidents.htm
# 

# In[1]:


#importing the required libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[2]:


#sending request to get the html code of the webpage
page3=requests.get("https://presidentofindia.nic.in/former-presidents.htm")


# In[3]:


#diplaying whether the page url is scrapable/accessible
page3


# In[4]:


#getting page html content
soup3=BeautifulSoup(page3.content,'html.parser')
soup3


# In[46]:


#creating empty lists for storing the required data
President_Name=[]
Office_Term=[]


# In[47]:


for i in soup3.find_all('h3'):
    President_Name.append(i.get_text(strip=True).split('(')[0])
for i in soup3.find_all('p'):
    Office_Term.append(i.get_text(strip=True))


# In[48]:


President_Name


# In[70]:


Office_Term


# In[56]:


Office_Term.pop(1)


# In[69]:


#removed individual items other than office term by repeatedly executing the pop operation

Office_Term.pop(14)


# In[71]:


Former_pre_List=pd.DataFrame({})
Former_pre_List['Name']=President_Name
Former_pre_List['Term']=Office_Term


# In[72]:


Former_pre_List


# In[ ]:





# #Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# #a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# #b) Top 10 ODI Batsmen along with the records of their team and rating.
# #c) Top 10 ODI bowlers along with the records of their team and rating.

# In[73]:


#Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.


# In[1]:


#importing the required libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[2]:


#sending request to get the html code of the webpage
page4=requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")


# In[3]:


#diplaying whether the page url is scrapable/accessible
page4


# In[4]:


#getting page html content
soup4=BeautifulSoup(page4.content,'html.parser')
soup4


# In[20]:


#creating empty team list and finding all team names and saving in to the team
Team=[]
for i in soup4.find_all("span",class_="u-hide-phablet"):
    Team.append(i.text)


# In[21]:


#creating empty matches and points list and saving the points & matches in the lists
#As the matches and Points are under the same class and tags both are coming under single list, so seperating them
#Also the top No.1 team has different tag and class with banner, so we are scraping it seperately and appending it to the remaing list

Matches=[]
Points=[]
ODI_MMatches=soup4.find_all('td',class_="table-body__cell u-center-text")
for i in range(0,len(ODI_MMatches),2):
    Matches.append(ODI_MMatches[i].get_text().replace(',',''))
    Points.append(ODI_MMatches[i+1].get_text().replace(',',''))
match_1 = soup4.find("td",class_="rankings-block__banner--matches").get_text()
Matches.insert(0,match_1)
points_1 = soup4.find('td',class_="rankings-block__banner--points").get_text().replace(',','')
Points.insert(0,points_1)


# In[22]:


# ccreating empty rating list and saving the ratings to list like above
Rating=[]
rating_all = soup4.find_all('td', class_="table-body__cell u-text-right rating")
for i in rating_all:
    Rating.append(i.get_text().replace('\n',''))
Rating_1 = soup4.find('td', class_="rankings-block__banner--rating u-text-right").get_text().replace('\n','').strip()
Rating.insert(0,Rating_1)


# In[23]:


#assigning the lists to a pandas data frame and saving the first 10 in the lists to the DF
ICC_top_10_MTeams = pd.DataFrame({})
ICC_top_10_MTeams['Team'] = Team[0:10]
ICC_top_10_MTeams['Matches'] = Matches[0:10]
ICC_top_10_MTeams['Points'] = Points[0:10]
ICC_top_10_MTeams['Rating'] = Rating[0:10]


# In[24]:


ICC_top_10_MTeams


# In[ ]:





# Top 10 ODI Batsmen along with the records of their team and rating.

# In[63]:


#importing the required libraries
import pandas as pd
from bs4 import BeautifulSoup
import requests


# In[64]:


#sending request to get the html code of the webpage
page5=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")


# In[65]:


#diplaying whether the page url is scrapable/accessible
page5


# In[66]:


#getting page html content
soup5=BeautifulSoup(page5.text,'html.parser')
soup5


# In[79]:


#creating empty lists for storing names and details
Name=[]
Team=[]
Rating=[]


# In[80]:


#top 1 player has different class & tags as he is highlighted in a banner
#remaining players to be scraped seperately and both to be combined

Player1 = soup5.find("div",class_="rankings-block__banner--name-large").get_text()

Player_all = soup5.find_all('td',class_="table-body__cell rankings-table__name name")

for i in Player_all:
    Name.append(i.get_text().replace('\n',''))
Name.insert(0,Player1)


# In[89]:


#scraping the players team like above
Player1_Team=soup5.find('div',class_="rankings-block__banner--nationality").get_text().replace('\n','')
Playerall_Teams=soup5.find_all('span',class_="table-body__logo-text")
for i in Playerall_Teams:
    Team.append(i.get_text())
Team.insert(0,Player1_Team)


# In[92]:


#scraping the players ratings like above
Player1_Rating=soup5.find('div',class_='rankings-block__banner--rating').get_text()
Playerall_Rating=soup5.find_all('td',class_='table-body__cell rating')
for i in Playerall_Rating:
    Rating.append(i.get_text())
Rating.insert(0,Player1_Rating)


# In[93]:


#now building the pandas data frame with the data extracted
ODI_MenBat_10=pd.DataFrame({})
ODI_MenBat_10['Player']=Name[0:10]
ODI_MenBat_10['Team']=Team[0:10]
ODI_MenBat_10['Rating']=Rating[0:10]


# In[94]:


ODI_MenBat_10


# In[ ]:





# Top 10 ODI bowlers along with the records of their team and rating.
# 

# In[95]:


#importing the required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[96]:


#sending request to get the html code of the webpage
page6=requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page6


# In[99]:


#getting page html content
soup6=BeautifulSoup(page6.content,"html.parser")
soup6


# In[116]:


#creating empty lists for storing names and details
Player=[]
Team=[]
Rating=[]


# In[117]:


#top 1 player has different class & tags as he is highlighted in a banner
#remaining players to be scraped seperately and both to be combined
Player1=soup6.find('div',"rankings-block__banner--name-large").get_text()
PlayerAll=soup6.find_all('td',class_='table-body__cell rankings-table__name name')
for i in PlayerAll:
    Player.append(i.get_text().replace('\n',''))
Player.insert(0,Player1)


# In[118]:


#scraping the players team like above
Player1_Team=soup6.find('div',class_='rankings-block__banner--nationality').get_text().replace('\n','')
PlayerAll_Team=soup6.find_all('span',class_='table-body__logo-text')
for i in PlayerAll_Team:
    Team.append(i.get_text())
Team.insert(0,Player1_Team)


# In[119]:


#scraping the players Ratings like above
Player1_Rating=soup6.find('div',class_='rankings-block__banner--rating').get_text()
PlayerAll_Rating=soup6.find_all('td',class_='table-body__cell rating')
for i in PlayerAll_Rating:
    Rating.append(i.get_text())
Rating.insert(0,Player1_Rating)


# In[120]:


#now building the pandas data frame with the data extracted & Displaying the DATA FRAME
ODI_MenBow_10=pd.DataFrame({})
ODI_MenBow_10['Player']=Player[0:10]
ODI_MenBow_10['Team']=Team[0:10]
ODI_MenBow_10['Rating']=Rating[0:10]
ODI_MenBow_10


# 6) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.
# b) Top 10 women’s ODI Batting players along with the records of their team and rating.
# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# a) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[121]:


#importing the required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[122]:


#sending request to get the html code of the webpage
page7=requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page7


# In[123]:


#getting page html content
soup7=BeautifulSoup(page7.content,"html.parser")
soup7


# In[125]:


#creating empty team list and finding all team names and saving in to the team (As all team names coming under same tag&class)
Team=[]
for i in soup7.find_all("span",class_="u-hide-phablet"):
    Team.append(i.text)


# In[128]:


#creating empty matches and points list and saving the points & matches in the lists
#As the matches and Points are under the same class and tags both are coming under single list, so seperating them
#Also the top No.1 team has different tag and class with banner, so we are scraping it seperately and appending it to the remaing list

Matches=[]
Points=[]
ODI_WMatches=soup7.find_all('td',class_="table-body__cell u-center-text")
for i in range(0,len(ODI_WMatches),2):
    Matches.append(ODI_WMatches[i].get_text().replace(',',''))
    Points.append(ODI_WMatches[i+1].get_text().replace(',',''))
match_1 = soup7.find("td",class_="rankings-block__banner--matches").get_text()
Matches.insert(0,match_1)
points_1 = soup7.find('td',class_="rankings-block__banner--points").get_text().replace(',','')
Points.insert(0,points_1)


# In[130]:


# ccreating empty rating list and saving the ratings to list like above
Rating=[]
rating_all = soup7.find_all('td', class_="table-body__cell u-text-right rating")
for i in rating_all:
    Rating.append(i.get_text().replace('\n',''))
Rating_1 = soup7.find('td', class_="rankings-block__banner--rating u-text-right").get_text().replace('\n','').strip()
Rating.insert(0,Rating_1)


# In[131]:


#assigning the lists to a pandas data frame and saving the first 10 in the lists to the DF & Accessing the DF
ICC_top_10_WTeams = pd.DataFrame({})
ICC_top_10_WTeams['Team'] = Team[0:10]
ICC_top_10_WTeams['Matches'] = Matches[0:10]
ICC_top_10_WTeams['Points'] = Points[0:10]
ICC_top_10_WTeams['Rating'] = Rating[0:10]
ICC_top_10_WTeams


# b) Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[132]:


#importing the required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[133]:


#sending request to get the html code of the webpage
#diplaying whether the page url is scrapable/accessible
page8=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page8


# In[135]:


#getting page html content
soup8=BeautifulSoup(page8.text,'html.parser')
soup8


# In[138]:


#creating empty lists for storing names and details
Name=[]
Team=[]
Rating=[]


# In[139]:


#top 1 player has different class & tags as he is highlighted in a banner
#remaining players to be scraped seperately and both to be combined

Player1 = soup8.find("div",class_="rankings-block__banner--name-large").get_text()

Player_all = soup8.find_all('td',class_="table-body__cell rankings-table__name name")

for i in Player_all:
    Name.append(i.get_text().replace('\n',''))
Name.insert(0,Player1)


# In[140]:


#scraping the players team like above
Player1_Team=soup8.find('div',class_="rankings-block__banner--nationality").get_text().replace('\n','')
Playerall_Teams=soup8.find_all('span',class_="table-body__logo-text")
for i in Playerall_Teams:
    Team.append(i.get_text())
Team.insert(0,Player1_Team)


# In[141]:


#scraping the players ratings like above
Player1_Rating=soup8.find('div',class_='rankings-block__banner--rating').get_text()
Playerall_Rating=soup8.find_all('td',class_='table-body__cell rating')
for i in Playerall_Rating:
    Rating.append(i.get_text())
Rating.insert(0,Player1_Rating)


# In[142]:


#now building the pandas data frame with the data extracted &accessing the DF
ODI_WMenBat_10=pd.DataFrame({})
ODI_WMenBat_10['Player']=Name[0:10]
ODI_WMenBat_10['Team']=Team[0:10]
ODI_WMenBat_10['Rating']=Rating[0:10]
ODI_WMenBat_10


# c) Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[143]:


#importing the required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup


# In[144]:


#sending request to get the html code of the webpage
#diplaying whether the page url is scrapable/accessible
page9=requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page9


# In[145]:


#getting page html content
soup9=BeautifulSoup(page9.text,'html.parser')
soup9


# In[146]:


#creating empty lists for storing names and details
Name=[]
Team=[]
Rating=[]


# In[147]:


#top 1 player has different class & tags as he is highlighted in a banner
#remaining players to be scraped seperately and both to be combined

Player1 = soup9.find("div",class_="rankings-block__banner--name-large").get_text()

Player_all = soup9.find_all('td',class_="table-body__cell rankings-table__name name")

for i in Player_all:
    Name.append(i.get_text().replace('\n',''))
Name.insert(0,Player1)


# In[149]:


#scraping the players team like above
Player1_Team=soup9.find('div',class_="rankings-block__banner--nationality").get_text().replace('\n','')
Playerall_Teams=soup9.find_all('span',class_="table-body__logo-text")
for i in Playerall_Teams:
    Team.append(i.get_text())
Team.insert(0,Player1_Team)


# In[150]:


#scraping the players ratings like above
Player1_Rating=soup9.find('div',class_='rankings-block__banner--rating').get_text()
Playerall_Rating=soup9.find_all('td',class_='table-body__cell rating')
for i in Playerall_Rating:
    Rating.append(i.get_text())
Rating.insert(0,Player1_Rating)


# In[151]:


#now building the pandas data frame with the data extracted &accessing the DF
ODI_WMenAR_10=pd.DataFrame({})
ODI_WMenAR_10['Player']=Name[0:10]
ODI_WMenAR_10['Team']=Team[0:10]
ODI_WMenAR_10['Rating']=Rating[0:10]
ODI_WMenAR_10


# As men & Women ODI batting & All rounder , Bowling scraping is similar we can make a user defined function
# We can also get test, T20 rankings for individuals 
# 
# This function can be run after importing the required libraries
# 
# Team ranking has different tags, so that can be done in other user defined function

# In[167]:


def ICC_Top10(url):
    Name=[]
    Team=[]
    Rating=[]

    Page = requests.get(url)
    soup = BeautifulSoup(Page.content, 'html.parser')
    Player1 = soup.find("div",class_="rankings-block__banner--name-large").get_text()
    Player_All = soup.find_all('td',class_="table-body__cell rankings-table__name name")
    for i in Player_All:
        Name.append(i.get_text().replace('\n',''))
    Name.insert(0,Player1)
    
    #Scraping the team
    Player1_Team = soup.find('div',class_='rankings-block__banner--nationality').get_text().replace('\n','')
    PlayerAll_Team = soup.find_all('span',class_='table-body__logo-text')
    for i in PlayerAll_Team:
        Team.append(i.get_text())
    Team.insert(0,Player1_Team) 
    #Rating scraping
    Player1_Rating = soup.find('div',class_="rankings-block__banner--rating").get_text().replace('\n','')
    Player_Allrating = soup.find_all('td',class_="table-body__cell rating")
    for i in Player_Allrating:
        Rating.append(i.get_text().replace('\n',''))
    Rating.insert(0,Player1_Rating)
    
    ICC_Top10 = pd.DataFrame({})
    ICC_Top10['Name'] = Name[0:10]
    ICC_Top10['Team'] = Team[0:10]
    ICC_Top10['Rating'] = Rating[0:10]
    print(ICC_Top10)


# In[168]:


ICC_Top10('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder')


# In[169]:


ICC_Top10('https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting')


# In[170]:


ICC_Top10('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting')


# In[171]:


ICC_Top10('https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling')


# In[ ]:





# Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :
# i) Headline
# ii) Time
# iii) News Link

# In[173]:


#importing the required libraries
import requests
from bs4 import BeautifulSoup


# In[174]:


#sending request to get the html code of the webpage
#diplaying whether the page url is scrapable/accessible
page=requests.get("https://www.cnbc.com/world/?region=world")
page


# In[175]:


#getting page html content
soup=BeautifulSoup(page.text,'html.parser')
soup


# In[180]:


Head_line=[]
for i in soup.find_all('div',class_='RiverHeadline-headline RiverHeadline-hasThumbnail'):
   Head_line.append(i.text)
Head_line


# In[181]:


time=[]
for i in soup.find_all('time'):
   time.append(i.text)
time


# In[183]:


page1 = requests.get("https://www.cnbc.com/world/?region=world") 
soup1 = BeautifulSoup(page1.content, "html.parser")
# Retrieve all of the anchor tags
# Returns a list of all the links
tags=soup1('a')
#Prints all the links in the list tags
for tag in tags:
    # Get the data from href key
    print(tag.get('href', None), end = "\n")


# In[ ]:





# 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days.
# https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details :
# i) Paper Title
# ii) Authors
# iii) Published Date
# iv) Paper URL

# In[187]:


#importing the required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[188]:


#sending request to get the html code of the webpage
#diplaying whether the page url is scrapable/accessible
page=requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
page


# In[189]:


#getting page html content
soup=BeautifulSoup(page.text,'html.parser')
soup


# In[237]:


#creating empty lists for saving the titles and other details

Paper_Title=[]
Authors=[]
Pub_Date=[]
Paper_URL=[]

#for extracting the paper titles
Papers=soup.find_all('h2',class_='sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg')
for i in Papers:
    Paper_Title.append(i.get_text())
    
#for extracting the Author names
author=soup.find_all('span',class_='sc-1w3fpd7-0 dnCnAO')
for i in author:
    Authors.append(i.get_text())
    
# for extracting the published date
PubDate=soup.find_all('span',class_='sc-1thf9ly-2 dvggWt')
for i in PubDate:
    Pub_Date.append(i.get_text())

#for extracting the paper URL
soup2=soup.find('div',class_='sc-orwwe2-3 jOMrrY').find_all('a')
for i in soup2:
    Paper_URL.append(i.get('href', None))


# In[243]:


Most_Downloaded=pd.DataFrame({})
Most_Downloaded['Title']=Paper_Title
Most_Downloaded['Author']=Authors
Most_Downloaded['Publish Date']=Pub_Date
Most_Downloaded['URL']=Paper_URL
Most_Downloaded


# In[ ]:





# 9) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# ii) Cuisine
# iii) Location
# iv) Ratings
# v) Image URL

# In[246]:


#importing the required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[247]:


#sending request to get the html code of the webpage
#diplaying whether the page url is scrapable/accessible
page=requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page


# In[248]:


#getting page html content
soup=BeautifulSoup(page.text,'html.parser')
soup


# In[273]:


#creating empty lists for saving the names and other details

Rest_Name=[]
Cuisine=[]
Location=[]
Rating=[]
Image_URL=[]

#to get the restaurant names
Name=soup.find_all('a',class_='restnt-name ellipsis')
for i in Name:
    Rest_Name.append(i.get_text())
    
#to get the cuisine
cui=soup.find_all('span',class_='double-line-ellipsis')
for i in cui:
    Cuisine.append(i.text.split('|')[1])

#to get the Location
Loc=soup.find_all('div',class_='restnt-loc ellipsis')
for i in Loc:
    Location.append(i.get_text())
    
#to get the Rating
Rate=soup.find_all('div',class_='restnt-rating rating-4')
for i in Rate:
    Rating.append(i.get_text())
    
#to get Image_url
imgurl=soup.find_all('img',class_='no-img')
for i in imgurl:
    Image_URL.append(i.get('data-src'))
    


# In[274]:


Rest_Data=pd.DataFrame({})
Rest_Data['Title']=Rest_Name
Rest_Data['Cuisine']=Cuisine
Rest_Data['LOcation']=Location
Rest_Data['Rating']=Rating
Rest_Data['ImageURL']=Image_URL
Rest_Data


# In[ ]:





# 10) Write a python program to scrape the details of top publications from Google Scholar from
# https://scholar.google.com/citations?view_op=top_venues&hl=en
# i) Rank
# ii) Publication
# iii) h5-index
# iv) h5-median

# In[275]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[276]:


page=requests.get("https://scholar.google.com/citations?view_op=top_venues&hl=en")
page


# In[277]:


soup=BeautifulSoup(page.content,'html.parser')
soup


# In[299]:



#creating empty lists for saving the names and other details
Rank=[]
Publication=[]
H5_Index=[]
H5_Median=[]

#to get the rank of publication
Ranks=soup.find_all('td',class_='gsc_mvt_p')
for i in Ranks:
    Rank.append(i.get_text())
    
#to get the publication names    
Publ=soup.find_all('td',class_='gsc_mvt_t')
for i in Publ:
    Publication.append(i.get_text())
    
    
#to get the h5-index
H5_ind=soup.find_all('a',class_='gs_ibl gsc_mp_anchor')
for i in H5_ind:
    H5_Index.append(i.get_text())
    

#to get the h5-median
H5_med=soup.find_all('span',class_='gs_ibl gsc_mp_anchor')
for i in H5_med:
    H5_Median.append(i.get_text().split(',')[0])
    


# In[300]:


#to create a pandas data frame and saving the lists to DF and accessing it

Top_Publications=pd.DataFrame({})
Top_Publications['Rank'] = Rank
Top_Publications['Publication'] = Publication
Top_Publications['h5-index'] = H5_Index
Top_Publications['h5-median'] = H5_Median
Top_Publications


# In[ ]:




