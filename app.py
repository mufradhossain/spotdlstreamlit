import os
from zipfile import ZipFile
import streamlit as st
import base64

def main():
    st.write("Spotify Downloader")
    url=st.text_input("Enter URL here")
    if st.button("Submit URL"):

        os.system("spotdl "+url)        
        dir_path = os.path.dirname(os.path.realpath(__file__)) 
        try:
            os.remove('music.zip')
        except:
            pass
        zipObj = ZipFile('music.zip', 'w')
        for root, dirs, files in os.walk(dir_path): 
            for file in files:  
                if file.endswith('.mp3'): 
                    
                    zipObj.write(root+"/"+str(file))
                    os.remove(root+"/"+str(file))
        zipObj.close()
        with open("music.zip", "rb") as f:
            bytes = f.read()
            b64 = base64.b64encode(bytes).decode()
            href = f'<a href="data:file/zip;base64,{b64}" download=\'music.zip\'>Download ZIP</a>'
            st.markdown(href, unsafe_allow_html=True)
if __name__ == "__main__":
    main()