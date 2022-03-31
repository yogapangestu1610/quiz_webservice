from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

@app.route("/cekHasil", methods=["POST"])
def cekHasil():
    berat = float(request.form['berat'])
    tinggi = float(request.form['tinggi'])
    
    bmi = berat/(tinggi/100)**2
    
    if bmi < 18.5 :
        keterangan = 'kurus'
    elif bmi > 18.5 and bmi < 25 :
        keterangan = 'normal'
    elif bmi > 25 and bmi < 40 :
        keterangan = 'berlebih'
    else : 
        keterangan =  'bahaya'
        
    hasil = {'keterangan': keterangan, 'bmi':bmi}
    return jsonify(hasil)

if __name__== '__main__':
    app.run(debug = True, port=5000)
    