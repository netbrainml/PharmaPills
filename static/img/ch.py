import os 
  
# Function to rename multiple files 
i = 0
      
for filename in os.listdir("test"): 
    dst ="test" + str(i) + ".jpg"
    src ='test/'+ filename 
    dst ='test/'+ dst 
      
    # rename() function will 
    # rename all the files 
    os.rename(src, dst) 
    i += 1