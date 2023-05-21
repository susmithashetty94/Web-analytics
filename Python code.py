import pandas as pd
import matplotlib.pyplot as plt

question_list=[]
earnings_list=[]
views_list=[]
followers_list=[]
ad_impressions_list=[]
requests_list=[]
answers_list=[]

earnings_count=0
views_count=0
followers_count=0
ad_impressions_count=0
requests_count=0
answers_count=0

temp_earnings =0
temp_views =0
temp_followers =0
temp_ad_impressions=0
temp_requests=0
temp_answers=0

# Categories/Topics words lists
books_words_list=[' book']
tv_movies_words_list=['movies','Kevin Spacey','John Wick','movie theaters','actor','Netflix','Korean Odyssey','screenplay','drive-in theaters',
                      'guest star','screenplays','Boruto','Game of Thrones','Adini Sen Koy','films','Naruto Shippuden','TV','movie','Diane Adler',
                      'Stone Ocean','Geralt','Spider-Man','Adam Driver','Kabhi Khushi Kabhie Gham','Friends','Steve-O','123movies.re','entertainment',
                      'GEICO Gecko','FemeFun','season','One Direction characters','television','tv']
food_restaurants_words_list=['food','DoorDash','restaurant']
animals_words_list=['animal','rabbit','animals','rabbits','name of animal']
video_games_words_list=['video game','video games','PUBG','NBA','PlayStation 4','PS4','GTA','PS3']
language_words_list=['korean','english','bangla','Telugu','language']
education_words_list=['graduate','GPA']
medicine_health_words_list=['Medical facilities','emergency','allergy','sick','physician','surgeon','dental']
money_words_list=['deposit','debit card','payment','cash','money','capital','finance','tip','buy']
politics_words_list=['political issues','politics','elections','politician']
social_media_words_list=['Snapchat','Facebook','Whatsapp','Instagram','twitter']
location_words_list=['ice skating','country','city','area code','place','state','living in']
music_bands_words_list=['band','guitars','music','song','autotune','concerts','Spotify']
sports_words_list=['FIFA','sport','football','soccer','champions league','NFL']
technology_words_list=['technology','smart phone','Mac','computer','networking']
smoking_words_list=['Juul']
#celebrities_words_list=['graduate from','actor']
celebrities_words_list=['actor']
chemical_words_list=['chemical']
art_words_list=['art']
clothing_words_list=['clothing']

# Initialize dictionary
quest_count_dict ={'Money' : 0, 'Location' : 0, 'Companies' : 0, 'TV_and_Movies' : 0,
                'Politics' : 0, 'Clothing' : 0, 'Music_and_Bands' : 0, 'Food_and_Restaurants' : 0,
                'Video_Games' : 0, 'Sports' : 0, 'Language_Specific' : 0, 'Technology' : 0,
                'Celebrities' : 0, 'Art' : 0, 'Other' : 0, 'Animals' : 0, 'Healthcare' : 0, 'Books' : 0,
                'Education' : 0, 'Social_Media': 0, 'Smoking' : 0, 'Chemical' : 0}
earnings_count_dict={'Money' : 0, 'Location' : 0, 'Companies' : 0, 'TV_and_Movies' : 0,
                'Politics' : 0, 'Clothing' : 0, 'Music_and_Bands' : 0, 'Food_and_Restaurants' : 0,
                'Video_Games' : 0, 'Sports' : 0, 'Language_Specific' : 0, 'Technology' : 0,
                'Celebrities' : 0, 'Art' : 0, 'Other' : 0, 'Animals' : 0, 'Healthcare' : 0, 'Books' : 0,
                'Education' : 0, 'Social_Media': 0, 'Smoking' : 0, 'Chemical' : 0}
views_count_dict = {'Money' : 0, 'Location' : 0, 'Companies' : 0, 'TV_and_Movies' : 0,
                'Politics' : 0, 'Clothing' : 0, 'Music_and_Bands' : 0, 'Food_and_Restaurants' : 0,
                'Video_Games' : 0, 'Sports' : 0, 'Language_Specific' : 0, 'Technology' : 0,
                'Celebrities' : 0, 'Art' : 0, 'Other' : 0, 'Animals' : 0, 'Healthcare' : 0, 'Books' : 0,
                'Education' : 0, 'Social_Media': 0, 'Smoking' : 0, 'Chemical' : 0}
followers_count_dict = {'Money' : 0, 'Location' : 0, 'Companies' : 0, 'TV_and_Movies' : 0,
                'Politics' : 0, 'Clothing' : 0, 'Music_and_Bands' : 0, 'Food_and_Restaurants' : 0,
                'Video_Games' : 0, 'Sports' : 0, 'Language_Specific' : 0, 'Technology' : 0,
                'Celebrities' : 0, 'Art' : 0, 'Other' : 0, 'Animals' : 0, 'Healthcare' : 0, 'Books' : 0,
                'Education' : 0, 'Social_Media': 0, 'Smoking' : 0, 'Chemical' : 0}
ad_impressions_count_dict = {'Money' : 0, 'Location' : 0, 'Companies' : 0, 'TV_and_Movies' : 0,
                'Politics' : 0, 'Clothing' : 0, 'Music_and_Bands' : 0, 'Food_and_Restaurants' : 0,
                'Video_Games' : 0, 'Sports' : 0, 'Language_Specific' : 0, 'Technology' : 0,
                'Celebrities' : 0, 'Art' : 0, 'Other' : 0, 'Animals' : 0, 'Healthcare' : 0, 'Books' : 0,
                'Education' : 0, 'Social_Media': 0, 'Smoking' : 0, 'Chemical' : 0}
requests_count_dict = {'Money' : 0, 'Location' : 0, 'Companies' : 0, 'TV_and_Movies' : 0,
                'Politics' : 0, 'Clothing' : 0, 'Music_and_Bands' : 0, 'Food_and_Restaurants' : 0,
                'Video_Games' : 0, 'Sports' : 0, 'Language_Specific' : 0, 'Technology' : 0,
                'Celebrities' : 0, 'Art' : 0, 'Other' : 0, 'Animals' : 0, 'Healthcare' : 0, 'Books' : 0,
                'Education' : 0, 'Social_Media': 0, 'Smoking' : 0, 'Chemical' : 0}
zero_earnings_count_dict = {'Money' : 0, 'Location' : 0, 'Companies' : 0, 'TV_and_Movies' : 0,
                'Politics' : 0, 'Clothing' : 0, 'Music_and_Bands' : 0, 'Food_and_Restaurants' : 0,
                'Video_Games' : 0, 'Sports' : 0, 'Language_Specific' : 0, 'Technology' : 0,
                'Celebrities' : 0, 'Art' : 0, 'Other' : 0, 'Animals' : 0, 'Healthcare' : 0, 'Books' : 0,
                'Education' : 0, 'Social_Media': 0, 'Smoking' : 0, 'Chemical' : 0}
answers_count_dict = {'Money' : 0, 'Location' : 0, 'Companies' : 0, 'TV_and_Movies' : 0,
                'Politics' : 0, 'Clothing' : 0, 'Music_and_Bands' : 0, 'Food_and_Restaurants' : 0,
                'Video_Games' : 0, 'Sports' : 0, 'Language_Specific' : 0, 'Technology' : 0,
                'Celebrities' : 0, 'Art' : 0, 'Other' : 0, 'Animals' : 0, 'Healthcare' : 0, 'Books' : 0,
                'Education' : 0, 'Social_Media': 0, 'Smoking' : 0, 'Chemical' : 0}

def get_data_from_excel():
    global question_list
    # read by default 1st sheet of an excel file
    dataframe1 = pd.read_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Dataset\\QuoraQuestions_excel.xlsx') 
    total_rows=len(dataframe1.index)
    #print(total_rows)
    for index, row in dataframe1[0:total_rows].iterrows():
        # each row is returned as a pandas series
        #question_list += [row["questions"]] + [row["earnings"]]
        question_list.append(row["questions"])
        earnings_list.append(row["earnings"])
        views_list.append(row["views"])
        followers_list.append(row["followers"])
        ad_impressions_list.append(row["ad_impressions"])
        requests_list.append(row['requests'])
        answers_list.append(row['answers'])
    return question_list

def categorize_data_list(question,earnings,views,followers,ad_impressions,requests,answers):
        #print(type(question))
        #print(question)
        if len(question) == 0: 
                return None
        elif any(word in question for word in money_words_list): 
                return 'Money' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in books_words_list): 
                return 'Books' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in location_words_list): 
                return 'Location'  , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in tv_movies_words_list): 
                return 'TV_and_Movies' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in food_restaurants_words_list): 
                return 'Food_and_Restaurants' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in animals_words_list): 
                return 'Animals' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in video_games_words_list): 
                return 'Video_Games' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in language_words_list): 
                return 'Language_Specific' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in education_words_list): 
                return 'Education' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in medicine_health_words_list): 
                return 'Healthcare' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in politics_words_list): 
                return 'Politics' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in social_media_words_list): 
                return 'Social_Media' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in music_bands_words_list): 
                return 'Music_and_Bands' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in sports_words_list): 
                return 'Sports' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in technology_words_list): 
                return 'Technology' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in smoking_words_list): 
                return 'Smoking' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in celebrities_words_list): 
                return 'Celebrities' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in chemical_words_list): 
                return 'Chemical' , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in art_words_list): 
                return 'Art'  , earnings,views, followers,  ad_impressions,requests,answers
        elif any(word in question for word in clothing_words_list): 
                return 'Clothing'  , earnings,views, followers,  ad_impressions,requests,answers
        else: 
                return 'Other' , earnings,views, followers,  ad_impressions,requests,answers
        
def excel_data_to_dictonary(topic_type):

    global earnings_count
    global views_count
    global followers_count
    global ad_impressions_count
    global requests_count
    global answers_count

    global temp_earnings
    global temp_views
    global temp_followers
    global temp_ad_impressions
    global temp_requests
    global temp_answers

    # Question category dictionary
    quest_count_dict[topic_type[0]] = quest_count_dict.get(topic_type[0], 0) + 1 

    # Earnings
    temp_earnings = temp_earnings + float(topic_type[1])
    earnings_count_dict[topic_type[0]] = round(earnings_count_dict.get(topic_type[0]) + temp_earnings, 2)  #+ earnings_count
    temp_earnings = 0

    # Views
    temp_views = temp_views +  int(topic_type[2]) 
    views_count_dict[topic_type[0]] = views_count_dict.get(topic_type[0]) + temp_views
    temp_views = 0

    # Followers
    temp_followers = temp_followers + int(topic_type[3]) 
    followers_count_dict[topic_type[0]] = followers_count_dict.get(topic_type[0]) + temp_followers
    temp_followers = 0

    # Ad_Impressions
    temp_ad_impressions = temp_ad_impressions + int(topic_type[4]) 
    ad_impressions_count_dict[topic_type[0]] = ad_impressions_count_dict.get(topic_type[0]) + temp_ad_impressions
    temp_ad_impressions = 0

    # Requests
    temp_requests = temp_requests + int(topic_type[5]) 
    requests_count_dict[topic_type[0]] = requests_count_dict.get(topic_type[0]) + temp_requests
    temp_requests = 0

    # Zero Earnings Category
    if(topic_type[1] == '$0.00'):
        zero_earnings_count_dict[topic_type[0]] = zero_earnings_count_dict.get(topic_type[0], 0) + 1

    # Answers
    temp_answers = temp_answers + int(topic_type[6]) 
    answers_count_dict[topic_type[0]] = answers_count_dict.get(topic_type[0]) + temp_answers
    temp_answers = 0

def import_dict_to_excel(quest_count_dict, earnings_count_dict, views_count_dict, followers_count_dict, 
                         ad_impressions_count_dict,requests_count_dict, zero_earnings_count_dict,answers_count_dict):
    # Since 'other' type questions number is high so consider it as 0 for DV
    quest_count_dict['Other']=0
    earnings_count_dict['Other']=0
    views_count_dict['Other']=0
    followers_count_dict['Other']=0
    ad_impressions_count_dict['Other']=0
    requests_count_dict['Other']=0
    zero_earnings_count_dict['Other']=0
    answers_count_dict['Other']=0
    column_names=['Sum']

    # # Writing the data to a excelsheet
    data_list=[quest_count_dict,earnings_count_dict,views_count_dict,followers_count_dict,ad_impressions_count_dict,
               requests_count_dict,zero_earnings_count_dict,answers_count_dict]
    data_frame_common=pd.DataFrame(data_list, index=['Categories Count','Earnings','Views','Followers',
                                                     'Ad_Impressions','Requests','Zero Earnings Categories','Answers'])
    data_frame_common.to_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Data\\18-April\\Common_Data_Quora.xlsx')

    data_frame_dict_category=pd.DataFrame(quest_count_dict,column_names)
    data_frame_dict_earnings=pd.DataFrame(earnings_count_dict,column_names)
    data_frame_dict_views=pd.DataFrame(views_count_dict,column_names)
    data_frame_dict_followers=pd.DataFrame(followers_count_dict,column_names)
    data_frame_dict_ad_impressions=pd.DataFrame(ad_impressions_count_dict,column_names)
    data_frame_dict_requests=pd.DataFrame(requests_count_dict,column_names)
    data_frame_dict_zero_earnings_category=pd.DataFrame(zero_earnings_count_dict,column_names)
    data_frame_dict_answers=pd.DataFrame(answers_count_dict,column_names)

    # Writing the data to a excelsheet
    data_frame_dict_category.to_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Data\\18-April\\CategoriesCount_Quora.xlsx')
    data_frame_dict_earnings.to_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Data\\18-April\\Earnings_Quora.xlsx')
    data_frame_dict_views.to_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Data\\18-April\\Views_Quora.xlsx')
    data_frame_dict_followers.to_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Data\\18-April\\Followers_Quora.xlsx')
    data_frame_dict_ad_impressions.to_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Data\\18-April\\Ad_Impressions_Quora.xlsx')
    data_frame_dict_requests.to_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Data\\18-April\\Requests_Quora.xlsx')
    data_frame_dict_zero_earnings_category.to_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Data\\18-April\\Zero_Earnings_Categories_Quora.xlsx')
    data_frame_dict_answers.to_excel('E:\\UTA\\Spring 2023\\Web & Social\\Project\\quora\\Data\\18-April\\Answers_Quora.xlsx')

############################   Function Call    #########################################################################################

# Get questions with earnings,views,followers & ad_impressions from the dataset (excelsheet)
question_list=get_data_from_excel()
#print(question_list)

# Creating dictionaries according to topic type,earnings,views,followers & ad_impressions
for (item,item2,item3,item4,item5,item6,item7) in zip(question_list,earnings_list,views_list,followers_list,ad_impressions_list,requests_list,answers_list):
    #print(item)
    topic_type=categorize_data_list(item,item2,item3,item4,item5,item6,item7)
    #print(topic_type) is a tuple
    excel_data_to_dictonary(topic_type)


# Writing/Importing the above data to excel sheet
import_dict_to_excel(quest_count_dict, earnings_count_dict, views_count_dict, followers_count_dict, 
                     ad_impressions_count_dict,requests_count_dict,zero_earnings_count_dict,answers_count_dict)

# Printing all the dictionaries
print('********* Catgories Question Count **********')
print(quest_count_dict)
print('********* Earnings **********')
print(earnings_count_dict)
print('********* Views **********')
print(views_count_dict)
print('********* Followers **********')
print(followers_count_dict)
print('********* Ad_Impressions **********')
# Set the value 'need more views' to 0 from column 'ad_impressions' in quora excel
print(ad_impressions_count_dict)
print('********* Requests **********')
print(requests_count_dict)
print('************ Zero Earnings Category ***************')
print(zero_earnings_count_dict)
print('************ Answers ***************')
print(answers_count_dict)

