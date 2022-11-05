from server import app, db
from flask import jsonify, request


class Score(db.Model):
    
    id = db.Column(db.Integer(), primary_key=True, unique=True)
    username = db.Column(db.Text(), nullable=False, unique=True)
    game1_score = db.Column(db.Text(), nullable=False)
    game2_score = db.Column(db.Text(), nullable=False)
    game3_score = db.Column(db.Text(), nullable=False)
    game4_score = db.Column(db.Text(), nullable=False) 
    

    
@app.route('/', methods = ['POST', 'GET'])
def home():
    
    scores = []
    score_dict = {'username':str,'game1':str,'game2':str,'game3': str, 'game4':str}
    player_ = ''
    with open(r'C:\Users\Grzegorz\Documents\Porg\hakaton\server\scores.txt' , encoding='iso8859-2') as f:
        lines = f.readlines()
        
        count = sum(1 for _ in lines)
        print(count)
        player_num = int(count/4)
        
        
        for i in range(player_num):
            scores.append(score_dict)
            
        i = 0
       
        for line in lines:
            if player_ != line.split()[0]:
                player_ =line.split()[0]
                scores[i]['username'] = player_
                #print(scores[i])
                
            
            
            scores[i]['game' + str(i+1)] = line.split()[1]
            #print(scores[i]['game' + str(i+1)])
            
            
            
            if i == 3 and scores[i]['username'] == player_:
                
                user = scores[i-1]['username']
                g1 = scores[i-1]['game' + str(i-2)] 
                g2 = scores[i-1]['game' + str(i-1)]
                g3 = scores[i-1]['game' + str(i)] 
                g4 = scores[i-1]['game' + str(i + 1)]
                
                print(user)
                print(g1)
                print(g2)
                print(g3)
                print(g4)
                
                
                user_exists = Score.query.filter_by(username=user).first() is not None
                
                if user_exists:
                    
                    prev_g1 = Score.query.filter_by(username=user).first()
                    prev_g2 = Score.query.filter_by(username=user).first()
                    prev_g3 = Score.query.filter_by(username=user).first()
                    prev_g4 = Score.query.filter_by(username=user).first()
                    
                    if int(g1)>int(prev_g1.game1_score):
                        prev_g1.game1_score = g1
                    if int(g2)>int(prev_g2.game2_score):
                        prev_g2.game2_score = g2
                    if int(g3)>int(prev_g3.game3_score):
                        prev_g3.game3_score = g3
                    if int(g4)>int(prev_g4.game4_score):
                        prev_g4.game4_score = g4
                    
                    
                    db.session.commit()
                
                    
                else:            
                    new_score = Score(username = user ,game1_score = g1, 
                                    game2_score = g2,  game3_score = g3,
                                    game4_score = g4)
                    
                    print(new_score)
                    db.session.add(new_score)
                    db.session.commit()
                    i = 0
                    
            else:
                i = i+1
        f.close()
        
        
        
            
                

            
            
    return "XD"
        
    
    
    
        


