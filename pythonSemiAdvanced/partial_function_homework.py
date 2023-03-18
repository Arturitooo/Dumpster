import requests 
import os
import functools

 
def save_url_file(url, dir, file,msg):
       
    print(msg.format(file))
    
    r = requests.get(url, stream = True) 
    file_path = os.path.join(dir, file)
      
    with open(file_path, "wb") as f: 
        f.write(r.content)

msg = "Please wait - the file {} will be downloaded"
 
save_url_file_fixed_direction = functools.partial(save_url_file, dir=r'C:\Users\Art\Documents\GitHub\learning\pythonSemiAdvanced\files_operations_with_ifs', msg = 'Please wait')

url = 'http://mobilo24.eu/spis'
file = 'spis.html'
#save_url_file(url, dir, file,msg)
save_url_file_fixed_direction(url = url, file=file)
 
url = 'https://www.mobilo24.eu/wp-content/uploads/2015/11/Mobilo_logo_kolko_512-565b1626v1_site_icon.png'
file = 'logo.png'
#save_url_file(url, dir, file,msg)
save_url_file_fixed_direction(url = url, file=file)

