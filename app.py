from flask import Flask,jsonify,request,render_template
from convert import Numerical
import pickle

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check',methods = ['GET','POST'])
def check():
    if request.method=='POST':
        print('tes1')
        name = request.form.get('name')
        gen = request.form.get('gender')
        mar = request.form.get('married')
        dep = request.form.get('dependents')
        ed = request.form.get('education')
        sf = request.form.get('self-employed')
        apin = request.form.get('applicant-income')
        coapin = request.form.get('coapplicant-income')
        lam = request.form.get('loan-amount')
        lterm = request.form.get('loan-term')
        crhist = request.form.get('credit-history')
        prarea = request.form.get('property-area')
        print(name,gen,mar,dep,ed,sf,apin,coapin,lam,lterm,crhist,prarea)
        nt = Numerical()
        genn = nt.converted('Gender',gen)
        marn = nt.converted('Married',mar)
        depn = int(dep)
        edn = nt.converted('Education',ed)
        sfn = nt.converted('Self_Employed',sf)
        if crhist=='Yes':
            crn = 1
        else:
            crn = 0
        prarean = nt.converted('Property_Area',prarea)
        print(nt,genn,marn,depn,edn,sfn,crn,prarean)
        with open('model.pickle','rb') as abc:
            mlmodel = pickle.load(abc)
        pred = mlmodel.predict([[genn,marn,depn,edn,sfn,apin,coapin,lam,lterm,crn,prarean]]) 
        if pred[0]==1:
            status = 'Loan Approved'
        else:
            status='Loan Rejected'

        print(pred)
        return render_template('message.html',status=status)
    else:
        return render_template('check.html')
if __name__== '__main__':
    app.run(host='0.0.0.0',port=5050)