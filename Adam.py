import sys;
import json;
import requests;
import csv;

#Written by Adam Rizk
#adamrizk9@gmail.com

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://search.unbxd.io/fb853e3332f2645fac9d71dc63e09ec1/demo-unbxd700181503576558/search?&q=*&rows=10&start=0");
numProducts = int(response.json()['response']['numberOfProducts']);
prodlist = response.json()['response']['products'];
json_object = json.dumps(prodlist, indent = 4)
i=0;
numProducts=3;
product = (prodlist[i]);
listKeys = list(product.keys())
MlistKeys = set(listKeys);
for i in range(0,numProducts):       #We loop over al the products one by one
    product = prodlist[i];
    listKeys = list(product.keys())
    MlistKeys.update(set(listKeys));
    for n in listKeys:               #We iterate over all the JSON objects in the product
        if type(product[n]) is list:         #checking if datattype is an array
            print(n);
            uniqueList = list(set(product[n]));   #Removing Duplicate Values from List
            uniqueString = ','.join(map(str,uniqueList))   #Converting array to commea seperated uniqueString
            product[n] = uniqueString;         #Replacing JSON array with the processed string

#After the abovr nested loop, we have converted all arrays to strings and removed duplicate values
jprint(prodlist[0]);  #Printing the first data after processing


#csv_file="Unbxd-2021-interns-Test-Adam-Rizk"
#try:
#    with open(csv_file,'w') as csvfile:
#        writer = csv.DictWriter(csvfile, fieldnames=list(MlistKeys));
#        writer.writeheader()
#        for data in prodlist:
#                writer.writerow(data);
#except IOError:
#    print("I/O error");
