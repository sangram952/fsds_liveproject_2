from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "final testing on 19/6 CICD pipeline setup competed"
  
if __name__=="__main__":
    app.run(debug=True)
