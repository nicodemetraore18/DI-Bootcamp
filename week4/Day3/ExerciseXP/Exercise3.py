
#Zara

brand={
"name": "Zara", 
"creation_date": 1975 ,
"creator_name":"Amancio Ortega Gaona",
"type_of_clothes": ["men", "women", "children", "home" ],
"international_competitors": ["Gap", "H&M", "Benetton" ],
"number_stores": 7000 ,
"major_color": {
    "France": "blue", 
    "Spain": "red", 
    "US": ["pink", "green"]}
}

brand["number_stores"]=2;
print("Zara's products are destinied to anyone men,women,children");
brand["country_creation"]="Spain";
if "international_competitors" in brand:
   brand["international_competitors"].append("Desigual");
print( brand["international_competitors"]);
print( brand["number_stores"]);
del brand["creation_date"];
print( brand["international_competitors"][len(brand["international_competitors"])-1]);
print(brand["major_color"]["US"])
print(len(brand))
for key in brand:
    print(key);

more_on_zara={
"creation_date": 1975 ,
"number_stores": 10000

}
brand.update(more_on_zara);
print(brand["number_stores"]);

