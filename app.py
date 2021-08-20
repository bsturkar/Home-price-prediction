from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import json
import numpy as np
import sklearn
#from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('bang.pkl', 'rb'))
with open('columns.json','r') as f:
    col= json.load(f)
x=col
#GET means you are retriving something from anather file i.e. here from index file 
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

        
# standard_to = StandardScaler()
#GET means you are adding something 
@app.route("/predict", methods=['POST'])
def predict():    
    location =str(request.form['location']) 
    total_sqft = int(request.form['total_sqft'])
    bath=int(request.form['bath'])
    bhk=int(request.form['bhk']) 
    # # loc_index = np.where(x.columns==location)[0][0]
    # # # m = np.zeros(len(x.columns)) 
    # loc_index=3 
    # # #m = np.zeros(243)
    # x=['total_sqft','bath','bhk','1st Block Jayanagar',
    #    '1st Phase JP Nagar', '2nd Phase Judicial Layout',
    #    '2nd Stage Nagarbhavi', '5th Block Hbr Layout',
    #    '5th Phase JP Nagar', '6th Phase JP Nagar', '7th Phase JP Nagar',
    #    '8th Phase JP Nagar', '9th Phase JP Nagar', 'AECS Layout',
    #    'Abbigere', 'Akshaya Nagar', 'Ambalipura', 'Ambedkar Nagar',
    #    'Amruthahalli', 'Anandapura', 'Ananth Nagar', 'Anekal',
    #    'Anjanapura', 'Ardendale', 'Arekere', 'Attibele', 'BEML Layout',
    #    'BTM 2nd Stage', 'BTM Layout', 'Babusapalaya', 'Badavala Nagar',
    #    'Balagere', 'Banashankari', 'Banashankari Stage II',
    #    'Banashankari Stage III', 'Banashankari Stage V',
    #    'Banashankari Stage VI', 'Banaswadi', 'Banjara Layout',
    #    'Bannerghatta', 'Bannerghatta Road', 'Basavangudi',
    #    'Basaveshwara Nagar', 'Battarahalli', 'Begur', 'Begur Road',
    #    'Bellandur', 'Benson Town', 'Bharathi Nagar', 'Bhoganhalli',
    #    'Billekahalli', 'Binny Pete', 'Bisuvanahalli', 'Bommanahalli',
    #    'Bommasandra', 'Bommasandra Industrial Area', 'Bommenahalli',
    #    'Brookefield', 'Budigere', 'CV Raman Nagar', 'Chamrajpet',
    #    'Chandapura', 'Channasandra', 'Chikka Tirupathi', 'Chikkabanavar',
    #    'Chikkalasandra', 'Choodasandra', 'Cooke Town', 'Cox Town',
    #    'Cunningham Road', 'Dasanapura', 'Dasarahalli', 'Devanahalli',
    #    'Devarachikkanahalli', 'Dodda Nekkundi', 'Doddaballapur',
    #    'Doddakallasandra', 'Doddathoguru', 'Domlur', 'Dommasandra',
    #    'EPIP Zone', 'Electronic City', 'Electronic City Phase II',
    #    'Electronics City Phase 1', 'Frazer Town', 'GM Palaya',
    #    'Garudachar Palya', 'Giri Nagar', 'Gollarapalya Hosahalli',
    #    'Gottigere', 'Green Glen Layout', 'Gubbalala', 'Gunjur',
    #    'HAL 2nd Stage', 'HBR Layout', 'HRBR Layout', 'HSR Layout',
    #    'Haralur Road', 'Harlur', 'Hebbal', 'Hebbal Kempapura',
    #    'Hegde Nagar', 'Hennur', 'Hennur Road', 'Hoodi', 'Horamavu Agara',
    #    'Horamavu Banaswadi', 'Hormavu', 'Hosa Road', 'Hosakerehalli',
    #    'Hoskote', 'Hosur Road', 'Hulimavu', 'ISRO Layout', 'ITPL',
    #    'Iblur Village', 'Indira Nagar', 'JP Nagar', 'Jakkur', 'Jalahalli',
    #    'Jalahalli East', 'Jigani', 'Judicial Layout', 'KR Puram',
    #    'Kadubeesanahalli', 'Kadugodi', 'Kaggadasapura', 'Kaggalipura',
    #    'Kaikondrahalli', 'Kalena Agrahara', 'Kalyan nagar', 'Kambipura',
    #    'Kammanahalli', 'Kammasandra', 'Kanakapura', 'Kanakpura Road',
    #    'Kannamangala', 'Karuna Nagar', 'Kasavanhalli', 'Kasturi Nagar',
    #    'Kathriguppe', 'Kaval Byrasandra', 'Kenchenahalli', 'Kengeri',
    #    'Kengeri Satellite Town', 'Kereguddadahalli', 'Kodichikkanahalli',
    #    'Kodigehaali', 'Kodigehalli', 'Kodihalli', 'Kogilu', 'Konanakunte',
    #    'Koramangala', 'Kothannur', 'Kothanur', 'Kudlu', 'Kudlu Gate',
    #    'Kumaraswami Layout', 'Kundalahalli', 'LB Shastri Nagar',
    #    'Laggere', 'Lakshminarayana Pura', 'Lingadheeranahalli',
    #    'Magadi Road', 'Mahadevpura', 'Mahalakshmi Layout', 'Mallasandra',
    #    'Malleshpalya', 'Malleshwaram', 'Marathahalli', 'Margondanahalli',
    #    'Marsur', 'Mico Layout', 'Munnekollal', 'Murugeshpalya',
    #    'Mysore Road', 'NGR Layout', 'NRI Layout', 'Nagarbhavi',
    #    'Nagasandra', 'Nagavara', 'Nagavarapalya', 'Narayanapura',
    #    'Neeladri Nagar', 'Nehru Nagar', 'OMBR Layout', 'Old Airport Road',
    #    'Old Madras Road', 'Padmanabhanagar', 'Pai Layout', 'Panathur',
    #    'Parappana Agrahara', 'Pattandur Agrahara', 'Poorna Pragna Layout',
    #    'Prithvi Layout', 'R.T. Nagar', 'Rachenahalli',
    #    'Raja Rajeshwari Nagar', 'Rajaji Nagar', 'Rajiv Nagar',
    #    'Ramagondanahalli', 'Ramamurthy Nagar', 'Rayasandra',
    #    'Sahakara Nagar', 'Sanjay nagar', 'Sarakki Nagar', 'Sarjapur',
    #    'Sarjapur  Road', 'Sarjapura - Attibele Road',
    #    'Sector 2 HSR Layout', 'Sector 7 HSR Layout', 'Seegehalli',
    #    'Shampura', 'Shivaji Nagar', 'Singasandra', 'Somasundara Palya',
    #    'Sompura', 'Sonnenahalli', 'Subramanyapura', 'Sultan Palaya',
    #    'TC Palaya', 'Talaghattapura', 'Thanisandra', 'Thigalarapalya',
    #    'Thubarahalli', 'Tindlu', 'Tumkur Road', 'Ulsoor', 'Uttarahalli',
    #    'Varthur', 'Varthur Road', 'Vasanthapura', 'Vidyaranyapura',
    #    'Vijayanagar', 'Vishveshwarya Layout', 'Vishwapriya Layout',
    #    'Vittasandra', 'Whitefield', 'Yelachenahalli', 'Yelahanka',
    #    'Yelahanka New Town', 'Yelenahalli', 'Yeshwanthpur']
    c=0
    for i in range(2,243):
        if x[i]==location:
           c=i
    #loc_index = np.where(x==location)[0][0]
    m = np.zeros(len(x))
    
    # m = np.zeros(243)
    m[0] = total_sqft
    m[1] = bath
    m[2] = bhk
    m[c] = 1
   

    prediction=model.predict([m])[0]
    output=prediction


    return render_template('index.html',prediction_text="home price in lakhs= {}".format(output))

if __name__=="__main__":
    app.run(debug=True)

