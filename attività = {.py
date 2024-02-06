
attività = {
 "Lunedi" : ["lezione di italiano", "studio matematica","allenamento di basket" ],
 "Martedi" : ["lezione di italiano", "studio matematica","allenamento di basket" ],
 "Mercoledi" : ["lezione di italiano", "studio matematica","allenamento di basket" ],
 "Giovedi" : ["lezione di italiano", "studio matematica","allenamento di basket" ], 
 "Venerdi" : ["lezione di italiano", "studio matematica","allenamento di basket" ], 
 "sabato" : ["lezione di italiano", "studio matematica","allenamento di basket" ], 
"domenica" : ["lezione di italiano", "studio matematica","allenamento di basket" ],
  
 }
for i in attività.items():
  
  print (i)
   

attività["sabato"] = ["sbronza con gli amici"] 

for i in attività.items():
    
    print(i)