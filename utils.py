import pymysql, hashlib, random, string

def generate_random_string(length):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))
connection = pymysql.connect(
        host='localhost',
        user='root',
        password='test',
        database='droidprivate',
        cursorclass=pymysql.cursors.DictCursor 
)
def get_user_amount():
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS user_count FROM users")
        result = cursor.fetchone()
        if result is None or 'user_count' not in result:
            return 0 
        return result['user_count']

def is_username_taken(username: str):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) AS user_count FROM users WHERE username = %s",username)
        result = cursor.fetchone()
        if result is None or 'user_count' not in result:
            return False
        return result['user_count'] > 0
def create_user(username: str, password: str):
    cursor = connection.cursor()
    user_id = get_user_amount()  
    if is_username_taken(username):
        return False
    cursor.execute(
        "INSERT INTO users (userId, rank, score, pp, accuracy, username, password) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (user_id, 0, 0, 0, 1.0, username, hashlib.md5(f"{password}taikotaiko".encode('utf-8')).hexdigest()) # idk, why this is "key" for hashing kekw 
    )
    connection.commit() 
    return True
def get_user(username: str, password: str):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s && password = %s",(username,password))
    rows = cursor.fetchall()
    if(len(rows) > 0):
        user = rows[0]
        return f"SUCCESS\n{user['userId']} SESSIONID {user['rank']} {user['score']} {user['pp']} {user['accuracy']} {user['username']}"
    else:
        return "FAILED\nWrong credentials"
def get_user_by_id(id: str):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE userId = %s",id)
    rows = cursor.fetchall()
    if(len(rows) > 0):
        user = rows[0]
        return f"SUCCESS\n{user['userId']} SESSIONID {user['rank']} {user['score']} {user['pp']} {user['accuracy']} {user['username']}"
    else:
        return "FAILED\nWrong credentials"
def get_user_rank_by_id(id: str):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE userId = %s",id)
    rows = cursor.fetchall()
    if(len(rows) > 0):
        user = rows[0]
        return user['rank']
    else:
        return False
def get_user_score_by_id(id: str):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE userId = %s",id)
    rows = cursor.fetchall()
    if(len(rows) > 0):
        user = rows[0]
        return user['score']
    else:
        return False
def get_user_accuracy_by_id(id: str):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE userId = %s",id)
    rows = cursor.fetchall()
    if(len(rows) > 0):
        user = rows[0]
        return user['accuracy']
    else:
        return False
def get_user_pp_by_id(id: str):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE userId = %s",id)
    rows = cursor.fetchall()
    if(len(rows) > 0):
        user = rows[0]
        return user['pp']
    else:
        return False
def generate_play(userID: str, ssid: str, filename: str, hash: str, songTitle: str, songArtist: str, songCreator: str):
    cursor = connection.cursor()
    playid = generate_random_string(8)
    print(f'Generated play for uid {userID} ({playid})')
    cursor.execute('INSERT INTO OnGoingPlays (userID, ssid, filename, hash, songTitle, songArtist, songCreator, playid) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);',(userID,ssid,filename,hash,songTitle,songArtist,songCreator,playid))
    connection.commit()
    return f"SUCCESS\n1 {playid}"

"""
'Data' struct
Mod String
Total Score With Multipler
Max Combo
Mark/Grade
Hit 300k
Hit 300
Hit 100k
Hit 100
Hit 50
Misses
Accuracy
Time
isPerfect(1/0)
PlayerName

Struct very smillar to osu! right?

Args:
    playID (str): PlayId sent during PreSubmit
    data (str): string explained above
    userID (str): UserID
"""
def get_play_response(playID: str, data: str, userID: str):
    # recalc score, recalc pp, recalc lb pos and many other shit im lazy to do rn :D
    rank = get_user_rank_by_id(userID)
    score = get_user_score_by_id(userID)
    pp = get_user_pp_by_id(userID)
    acc = get_user_accuracy_by_id(userID)
    
    if rank is not None:
        return f"SUCCESS\n{rank} {score} {acc} 420 {pp}"
    else:
        return f"FAILED\nErm. sir your profile doesn't exist, Skill issue?"
    

