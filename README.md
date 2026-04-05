# RAG_Local_File_Intrepter <br />
This project was derived from Tim Ruscica techwithtim. The main changes that I have made are the following <br />
1- The AI agent uses Gemini rather than Chat GPT<br />
2- Inngest_Inspection.py, which will inspect all available modules within Inngest to be used<br />
3- reset_qdrant.py, as the name suggests, it will reset the data set inside qdrant because sometimes it needs a manual reset once you change the inner code<br />
4- WhatVersionYourAPIRun.py, this will show what modules you can use regarding your API key<br /> 

**How to run Method #1**<br />
1- First, you have to download Qdrant or a similar platform<br />
2- Go inside streamlit_app.py  <br />
3- Go to the terminal while making sure Qdrant is running in the background<br />
4- Enter this code "uv run streamlit run .\streamlit_app.py"       <br />
5- Enter this command to see the background activity, which is npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery    <br />           
7- In runs, you can see each activity and any error if available <br />
**How to run Method #2**<br />
1- First, you have to download Qdrant or a similar platform<br />
2- Go inside main.py <br />
3- Go to the terminal while making sure Qdrant is running in the background<br />
4- Enter this code "uv run uvicorn main:app"   <br />    
5- Enter this second command "npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery" to see the data load <br />              
6- Go to any browser of your choice and enter http://localhost:8288/ <br />
7- On your left, look at Mangea and choose apps under it<br />
8- You will see "see functions."<br />
9- First choice InngestPDF and put the path of your PDF file " "data": "Yourfile path" " Note you have to put double // or it will not count the single /, then invoke <br />
11- Second choice InngestQuery and put your question" "question: "Your question" " then invoke <br />
12- To see the results, go to Runs and click on your desired event<br />
