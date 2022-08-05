# dwh-coding-challenge

author : Ogi Guntara

this program is tool to visualize historical table view of user banking activity, it visualize table as follows :
  1. Accounts
  2. Savings Accounts
  3. Cards
  4. Combination of all table
  5. Transaction details
  
How it works :
  1. first of all, it will read all over json data at folder 'data' and stored them in to list of dictionaries
  2. then the list is converted in to data frame using pandas
  3. with keep using pandas, the raw dataframe manipulated in to desire outcomes to visualize (print std)

How to use it :
  1. unzip file to get data set and scripts : **unzip dwh-coding-challenge.zip**
  2. make sure your current directory is in to program folder : **cd dwh-coding-challenge**
  3. build docker image : **docker build -t 'python-dwh-challenge' .**
  4. run docker : **docker run -ti python-dwh-challenge**

Task to complete :
  1. Visualize the complete historical table view of each tables in tabular format in stdout (hint: print your table)
  2. Visualize the complete historical table view of the denormalized joined table in stdout by joining these three tables (hint: the join key lies in the resources   section, please read carefully)
  3. From result from point no 2, discuss how many transactions has been made, when did each of them occur, and how much the value of each transaction?  
   Transaction is defined as activity which change the balance of the savings account or credit used of the card

Result :

![task1_accounts](https://user-images.githubusercontent.com/96209699/182984746-d2ea534b-4165-4ad5-bb60-7b81a0a7c7bb.jpg)
![task1_savings_accounts](https://user-images.githubusercontent.com/96209699/182984770-a3a465c1-44cf-43eb-a881-7c2026cce5c5.jpg)
![task1_cards](https://user-images.githubusercontent.com/96209699/182984790-74e37057-e4cc-4187-be8a-4314602a18f0.jpg)
![task2_all](https://user-images.githubusercontent.com/96209699/182984808-6ea828ae-f4e9-475b-932e-a5972f6ab95e.jpg)
![task3](https://user-images.githubusercontent.com/96209699/182984842-31186401-61ac-40e4-b5c4-1f17d36ab25f.jpg)
