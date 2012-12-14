import subprocess

host = [ "google.fr","perdu.com"]
box_list = { '100' : 'wanadoo static', '101': 'wanadoo dynamic', '102': 'neuf', '103': 'wanadoo duo', '104' : 'nerim', '105' : 'ovh1', '106' : 'ovh2', '107' : 'free' } 

online = []
offline = []
nom_box = []
box_online = []
box_offline = []

for box in box_list:
    #{
    print " "
    print "Test de la box : "  + box_list[box]
    nom_box.append(box_list[box])
    
    for hostname in host:
        #{
        ping = subprocess.Popen(["ping","-s", box , "-c", "1", hostname], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
              
        if ping.wait() == 0:            
            print "     " + hostname + " is Connected."
            online.append(hostname)
                
        else : 
            offline.append(nom_box)
            print "    " +hostname + " is down."   
            
        
        #}
            #print "    end of tests"
    #}
    
    if len(online) > 0  :
        print "Enable"
        box_online.append(nom_box)
    
    else :
        print "Disable"
        box_offline.append(nom_box)
    print nom_box
    nom_box = []
    
    online = []

print " "    
print "Liste des box online : " + str(box_online)

print "Liste des box offline : " + str(box_offline)
