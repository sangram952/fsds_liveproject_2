from flask import Flask
from housing.logger import logging

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    logging.info("we are testing logging module")
    return "final testing on 19/6 CICD pipeline setup competed"
  
if __name__=="__main__":
    app.run(debug=True)
