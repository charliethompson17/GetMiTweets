# GetMiTweets
save anyone's tweets  
  save anyone's liked tweets  
  delete all your tweets older than 7 days  

## instructions

1. git clone the repository
```
git clone https://github.com/charliethompson17/GetMiTweets.git
```
2. retrive api keys and tokens from the twitter developer portal

3. edit credentials in `congig.ini`

4. cd into project directory

5. create virtual environment
```
python3 -m venv venv
```
6. activate virtual environment
```
source venv/bin/activate
```
7. install requirments.txt
```
pip install -r requirements.txt
```

## usage
1. cd to project directory
2. ensure the venv is activated

`getUserTweets.py` gets all tweets by the user and saves them to the output file in reverse order
```
python getUserTweets.py USERNAME USERNAMEs_TWEETS.txt
```

`getLikedTwets.py` gets all tweets liked by the user and saves them to the output file
```
python getLikedTweets.py USERNAME USERNAMEs_LIKED_TWEETS.txt
```

`deleteUserTweets.py` deletes all your tweets older than 7 days staring with the oldest
```
python deleteMyTweets.py
```
