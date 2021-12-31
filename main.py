from flask import Flask, request, render_template, redirect, url_for
import pickle
from model import model
import numpy as np

app = Flask(__name__)
# We need to save the result elsewhere, cannot send the result directly to the route.
chance_of_admit = 0

@app.route('/',methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        return redirect(url_for('predict'))
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return render_template('predict.html')


@app.route('/result',methods = ['GET','POST'])
def result():
    # Push the back button
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        #Get parameter from user input
        GPA=float(request.values['GPA']) 
        TOEFL=int(request.values['TOEFL']) 
        GRE=int(request.values['GRE']) 
        university_rank=int(request.values['university'])
        personal_statement_strength = int(request.values['ps'])
        recommendation_strength=int(request.values['rl'])
        research_original=request.values['research_experience']
        research=-1
        if research_original=='Yes':
            research=1
        else:
            research=0
        
        chances = ""
        predict_features = np.array([GRE,TOEFL,university_rank,personal_statement_strength,recommendation_strength,GPA,research]).reshape(1,-1)
        chance_of_admit = ChoosingProcess(predict_features)
        print(chance_of_admit==3)
        if chance_of_admit == 3:
            chances += "Highly"
        elif chance_of_admit == 2:
            chances += "Medium"
        elif chance_of_admit == 1:
            chances += "Low"
        print(chances)
        TOEFLAdvice,SOPAdvice,ResearchAdvice,RecommendationAdvice = 0,0,0,0
        if TOEFL<100:
            TOEFLAdvice = 1
            # TOEFLAdvice['head'] = "TOELF"
            # TOEFLAdvice['main'] = "Your TOEFL score is lower than the average in recent years. Please note that although this score does not represent your academic level, it will affect your level of adaptation to the English academic environment in the future. If you still have time, please register for a TOEFL test and prepare carefully. Following are some websites that may help you:"
            # TOEFLAdvice['link1'] = "To register: https://www.ets.org/toefl"
            # TOEFLAdvice['link2'] = "To tips and mock exam: https://www.ets.org/s/toefl/free-practice/start.html"
        if personal_statement_strength < 4:
            SOPAdvice = 1
            # SOPAdvice['head'] = "The Strength of SOP"
            # SOPAdvice['main'] = " Your SOP is not strong enough to persuade the school to admit you. Also, you may exaggerate the strengthyour SOP, hence we strongly recommend you have a consultation in the school’s guidance center or online. Here are some websites of tips and online consultants that may help you."
            # SOPAdvice['link1'] = "To improve: https://www.harvardsqessays.com/essay-editing/college/"
            # SOPAdvice['link2'] = "To check grammar: https://www.grammarly.com/ "  
        if research == 0:
            ResearchAdvice = 1
            # ResearchAdvice['head'] = "Research Opportunity"
            # ResearchAdvice['main'] = "If you have ever had a research opportunity, it will greatly increase your competitiveness among other students. Research opportunity includes individual academic working, working with any professor or even final project of classes. If you still cannot find any project, we have some useful websites for you:  "
            # ResearchAdvice['link1'] = "For data analysis project:https://www.kaggle.com/"
            # ResearchAdvice['link2'] = "For where to find project: https://www.quora.com/"
        if recommendation_strength <4:
            RecommendationAdvice = 1
            # RecommendationAdvice['head'] = "The Strength of Letter of Recommendation:"
            # RecommendationAdvice['main'] = " Your Recommendation letter is not strong enough to persuade the school to admit you. You may persuade your professor to rewrite the letter with more words of praises, or try to find another professor. "
      

        return render_template('result.html', chances = chances, TOEFL = TOEFL, SOP = personal_statement_strength, RS = research, RM=recommendation_strength, TOEFLAdvice = TOEFLAdvice, SOPAdvice = SOPAdvice, ResearchAdvice= ResearchAdvice,RecommendationAdvice=RecommendationAdvice)


def ChoosingProcess(predict_features):
        #Predict the probability of admit
        

        model1 = model()
        model1.load()
        chance_of_admit = model1.predict(predict_features.reshape(1,-1))
        
        return int(chance_of_admit[0])
                 
if __name__ == '__main__':
    app.run(port=8080, debug=True)



