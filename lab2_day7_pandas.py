import  pandas as pd
db=pd.read_csv("C:/Users/bader/OneDrive/gitlesson/Day7-Lab2-Pandas/instagram_users.csv")
print("Q3: Print the number of rows and columns contained in the dataset\n",db.shape,"\n")
print("Q4: Print the size of dataset\n",db.size,"\n")
print("Q5: Print the data type of each column\n",db.dtypes,"\n")
print("Q6: Print the entire dataset\n",db,"\n")
print("Q7: Print the first 5 rows\n",db.head(),"\n")
print("Q8: Print the last 5 rows\n",db.tail(),"\n")
print("Q9: Print the total number of null values\n",db.isnull().sum(),"\n")
print("Q10: Print the rows that has duplicate values\n",db[db.duplicated()],"\n")
db=db.drop_duplicates()
print("Q11: Remove all duplicate values\n",db,"\n")
print("Q12: Print the number of rows and columns contained in the dataset after removing the duplicate values\n",db.shape,"\n")
db.columns=["Num_posts","Num_following","Num_followers","Biography_length","Picture_availability","Link_availability","Average_caption_length","Caption_zero","Non_image_percentage","Engagement_rate_like","Engagement_rate_comment","Location_tag_percentage","Average hashtag count","Promotional keywords","Followers keywords","Cosine similarity","Post interval","real_fake"]
print("Q13: Rename all dataset's columns\n",db,"\n")
db=db.replace({"real_fake":{"f":"fake","r":"real"}})
print("Q14: Change the class's values to real and fake\n",db,"\n")
print("Q15: Print the total number of each fake accounts and real accounts:\n",db["real_fake"].value_counts(),"\n")


print("Q16: Print the count, mean, std, min, 25%, 50%, 75% and the max for each column:\n\n",db.describe())



