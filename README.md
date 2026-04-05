**MAIN CHANGES**<br />
1- This code works using Gemini rather than ChatGPT <br />
2- reset_qdrant.py Class for resetting the data set in QDrant if you change sensitive data in the main code <br />
3- WhatVersionYourAPIRun.py shows you all the versions your API key can run <br /> 

**How to run Method #1**<br />
1- Download Qdrant or a similar platform<br />
2- Enter the streamlit_app.py and run the following code inside the terminal "uv run streamlit run .\streamlit_app.py"<br />
3- Open a new terminal and run the following code "npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery"<br />
4- Put your files inside the browser and ask the chatbot<br />
**Additional Steps**<br />
In case you want to see the code and the problems written, enter http://localhost:8288/ inside any browser of your choice it will show the activities. You can check any task you want

**How to run Method #2**<br />
1- Download Qdrant or a similar platform<br />
2- Enter the main.py and run the following code inside the terminal "uv run uvicorn main: app"<br />
3- Open a new terminal and run the following code "npx inngest-cli@latest dev -u http://127.0.0.1:8000/api/inngest --no-discovery"<br />
4- Go to the browser of your choice and enter http://localhost:8288/ <br />
5- Go to manage on your left and choose apps. You will see a function choice InngestPDF and enter your PDF path inside" data:"your PDF path" " make sure you use double forward dash // not only one <br />
6- Invoke, then do the same for InngestQuery, but in this one, you have to enter your question inside" "question: "your question" " then press invoke <br />
7- Go to the app and see the activity and choose the one you want to see the result<br />
