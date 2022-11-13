# GetMiTweets
save your tweets and liked tweets

## install instructions
1. git clone the repository
```
git clone https://github.com/charliethompson17/GetMiTweets.git
```
2. create virtual environment
```
python3 -m venv /path/to/new/virtual/environment
```
3. activate virtual environment
```
source venv/bin/activate
```
3. install requirments.txt
```
pip install -r requirements.txt
```

## setup instructions
1. retrive api keys and tokens from twitter developer portal
2. edit credentials in congig.ini

## usage
1. cd to project directory
2. ensure the venv is activated
```
source venv/bin/activate
```

getUserTweets.py gets all tweets by the user specified in the config file and saves them to the output file specified in the config file in reverse order
```
python getUserTweets.py
```

getLikedTwets.py gets all tweets liked by the user specified in the config file and saves them to the output file specified in the config file
```
python getLikedTweets.py
```

deleteUserTweets.py deletes all your tweets older than 7 days
```
python deleteUserTweets.py
```
