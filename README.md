# dwh-coding-challenge

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
  1. unzip file to get data set and scripts : unzip dwh-coding-challenge.zip
  2. make sure your current directory is in to program folder : cd dwh-coding-challenge
  3. build docker image : docker build -t 'python-dwh-challenge' .
  4. run docker : docker run -ti python-dwh-challenge
