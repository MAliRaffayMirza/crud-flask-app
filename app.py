from flask import Flask,request,session,redirect
import os
app=Flask(__name__)
app.secret_key = "9z!u#XyE1q93D@f8pL"

@app.route("/")
def home():
    return'''
<!DOCTYPE html>
<html>
<head>
    <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">

    <style>
        h1 {
            font-family: 'Lobster';
            color:#0e0482;
        }
    </style>
</head>
<body bgcolor="#03f8fc">


<table align="right"><tr>



	<td><form action="/login"><input style="width:100px; height:26px; background-color:white; border:2px solid blue; border-radius:8px; font-weight:bold;" type="submit" value="Log In"></form></td>


	<td><form action="/signup"><input style="width:100px; height:26px; background-color:white; border:2px solid blue; border-radius:8px; font-weight:bold;" type="submit" value="Sign Up"></form></td>



</tr></table><br>



    <h1 align="center">Welcome to CRUD Project</h1>
    <center><div style="border-radius:16px; border: 3px dashed blue; padding: 10px; width: 70%; background-color: white; text-align: center;"><marquee style="font-family: calibri; font-size: 18px; width: 100%;">You can manage your everyday tasks and office routines using this simple tool!</marquee></div></center>

    <br />
    <br />
    <br />

<table width="100%" height="40%" border="0px">
  <tr>
    <td width="50%" align="center">
      <div style="border: 3px solid blue; border-radius: 9%; height: 100%; background-color: white; padding: 10px; width: 60%; box-sizing: border-box;">
        <center><h1>What may you do?</h1></center>
        <p style="font-family:calibri; font-size: 19px; font-weight: bold;" align="center">
          You can do the following things using this tool.
        </p>
        <ol style="font-family:calibri; font-size: 18px;">
          <li>Create Task list</li>
          <li>Read Tasks from list</li>
          <li>Update Tasks from list</li>
          <li>Delete Tasks from list</li>
        </ol>
      </div>
    </td>

    <td width="50%" align="center">
      <div style="border: 3px solid blue; border-radius: 9%; height: 100%; background-color: white; padding: 10px; width: 60%; box-sizing: border-box;">
        <center><h1>Features of this Tool</h1></center>
        <p style="font-family:calibri; font-size: 19px; font-weight: bold;" align="center">
          You can do the following things using this tool.
        </p>
        <ol style="font-family:calibri; font-size: 18px;">
          <li>Create Task list</li>
          <li>Read Tasks from list</li>
          <li>Update Tasks from list</li>
          <li>Delete Tasks from list</li>
        </ol>
</div></td></tr></table>

<table style="position: absolute; left: 0px; bottom: -30%; height: 50px; width: 100%; border: 4px dashed #7f0587; background-color: white; font-family: calibri; font-weight: bold; text-align: center;"><tr align="center"><td align="center">This is a project I worked on myself to enhance my skills and be eligible for WerkStudent jobs.</td></tr></table>

</body>
</html>

'''



def errorpage(errortype):
    return """<body bgcolor="#00f7ff">
    <center><br>
    <h1 style="font-family: lobster; color: #05038c;">Sign Up</h1>

    <div style="width: 50%; border: 0.5px solid #ff8645; border-radius: 10px; background-color: #f5dacb; min-height:30px; text-align:center; padding-top:10px; text-align: center;">"""+errortype+"""</div><br>
    
    <form method="POST" action="/signup">
        <table width="50%" border="0">
            <tr>
                <td style="border: none;"><input name="username" placeholder="Username" style="width: 100%; height: 40px; padding: 10px; border:3px solid royalblue; border-radius: 10px;"></td>
                <td style="border: none;"><input name="password" placeholder="Password" type="password" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
            </tr>
        </table>

<br>

                <table width="50%" border="0">
            <tr>
                <td><input name="email" placeholder="Email" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
            </tr>
        </table>


<br>


        <table width="50%" border="0">
            <tr>
                <td><input name="secq" placeholder="Security Question" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
                <td><input name="seca" placeholder="Security Answer" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
            </tr>
        </table>
<br>

                <table width="50%" border="0">
            <tr>
                <td><input name="phone" placeholder="Phone Number" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
            </tr>
        </table>
        <br>
<input type="submit" style="width: 50%; border-radius: 10px; height: 40px; border:3px solid royalblue; background-color: orange; color: white; font-family: calibri; font-size: 18px; font-weight: bold;">

    </form>
    </center>
</body>"""




@app.route("/login")
def login():
    return'''
    <body bgcolor=#bbff3d>
</br></br></br><center>

<h1>Please enter Log In details below:</h1></br>
<form method="POST" action="/loggedin">
    <b></b> <input name="username" placeholder="Enter Username" style="width:50%; height:40px; font-size:16px; border-width:2px; border-color:#000000; background-color:#cffdff; border-radius:14px; padding:8px;"></br></br>
    <b></b> <input name="password" type="password" placeholder="Enter Password" style="width:50%; height:40px; font-size:16px; border-width:2px; border-color:#000000; background-color:#cffdff; border-radius:14px; padding:8px;"></br></br>
    <input type="submit" value="Log In" style="background-color:#ffff00; font-family:bahnschrift; font-size:16px; font-weight:bold; border-width:1px; height:35px; width:50%; border-radius:40px; color:#220080;"></br>
</form>

</center></body>
'''

@app.route("/loggedin", methods=["POST"])
def loggedin():
    username = request.form.get("username")
    password = request.form.get("password")
    session["username"] = username
    session["password"] = password
    return redirect("/dashboard")

@app.route("/dashboard", methods=["GET","POST"])

def process_login():
    #Login functioning here... if else...
    username=session.get("username")
    password=session.get("password")
    with open("details.txt", "r") as file:
        multilines=file.readlines()
    for singleline in multilines:
        line=singleline.strip().split(",")
        if line[0]==username and line[1] == password:
            session["username"]= username
            session["password"]= password
            if len(line)>2:
                htmlpage="""<html><head><style>body {background-color: #f5ed05;} h1 {font-family: Lobster, cursive; color: #9c000d;}</style><link href=https://fonts.googleapis.com/css2?family=Lobster&display=swap rel=stylesheet></head><body><center><br><h1>Your List Items are listed below</h1><br><table style="border: 0px dashed purple; margin:0px; background-color: white; min-width: 100%; border-radius: 10px;"><tr><td width="30%">
<form style="margin: 0; padding: 0;" action="/additem"><input type="submit" value="Add New Item" style="border:2px dashed blue; border-radius: 12px; width: 100%; height: 30px; background-color: white; font-family: calibri; font-weight: bolder; font-size: 15px;"></input></form></td>
<td width="30%"><form style="margin: 0; padding: 0;" action="/update"><input type="submit" value="Update Item" style="border:2px dashed blue; border-radius: 12px; width: 100%; height: 30px; background-color: white; font-family: calibri; font-weight: bolder; font-size: 15px;"></input></form></td>
<td width="30%"><form style="margin: 0; padding: 0;" action="/delete"><input type="submit" value="Delete Item" style="border:2px dashed blue; border-radius: 12px; width: 100%; height: 30px; background-color: white; font-family: calibri; font-weight: bolder; font-size: 15px;"></input></form></td>
<td width="10%"><form style="margin: 0; padding: 0;" action="/logout"><input type="submit" value="Log Out" style="border:2px dashed blue; border-radius: 12px; width: 100%; height: 30px; background-color: red; color:white; font-family: calibri; font-weight: bolder; font-size: 15px;"></input></form></td>
</tr></table><br><table style="border: 3px dashed purple; background-color: white; padding-top: 10px; padding-bottom: 10px; padding-left: 10px; padding-right: 10px; min-height: 60%; min-width: 30%; border-radius: 20%;"><tr><td><ol>"""
                for items in line[6:]:
                    htmlpage=htmlpage+"<li>"+items.upper()+"</li>"
                htmlpage=htmlpage+"""</td></tr></table>



</center></body>"""
                return htmlpage
            else:
                return'''<h1>Sorry, You don't have any item on your list!</h1>'''
    
    return redirect("/login")

@app.route("/signup", methods=["GET","POST"])
def signuphtml():
    
    return '''

<body bgcolor="#00f7ff">
	<center><br>
	<h1 style="font-family: lobster; color: #05038c;">Sign Up</h1><br>
	<form method="POST" action="/signups">
		<table width="50%" border="0">
			<tr>
				<td style="border: none;"><input name="username" placeholder="Username" style="width: 100%; height: 40px; padding: 10px; border:3px solid royalblue; border-radius: 10px;"></td>
				<td style="border: none;"><input name="password" placeholder="Password" type="password" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
			</tr>
		</table>

<br>

				<table width="50%" border="0">
			<tr>
				<td><input name="email" placeholder="Email" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
			</tr>
		</table>


<br>


		<table width="50%" border="0">
			<tr>
				<td><input name="secq" placeholder="Security Question" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
				<td><input name="seca" placeholder="Security Answer" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
			</tr>
		</table>
<br>

				<table width="50%" border="0">
			<tr>
				<td><input name="phone" placeholder="Phone Number" style="width: 100%; border-radius: 10px; height: 40px; border:3px solid royalblue; padding: 10px;"></td>
			</tr>
		</table>
		<br>
<input type="submit" style="width: 50%; border-radius: 10px; height: 40px; border:3px solid royalblue; background-color: orange; color: white; font-family: calibri; font-size: 18px; font-weight: bold;">

	</form>
	</center>
</body>

'''
@app.route("/signups", methods=["POST"])
def signupprocess():
    symbolex = "!@#$%^&*():;',.<>/?|`~+-="
    symbol = "!@#$%^&*()_-:;',.<>/?|`~+-="
    username=request.form.get("username")
    password=request.form.get("password")
    email=request.form.get("email")
    secq=request.form.get("secq")
    seca=request.form.get("seca")
    phone=request.form.get("phone")
    
    
    
    
    with open("details.txt", "r") as file:
        many_lines = file.readlines()
    for single_line in many_lines:
        existing_user = single_line.strip().split(",")[0]
        existing_email =  single_line.strip().split(",")[2]
        existing_phone =  single_line.strip().split(",")[5]
        if existing_user == username :
            return errorpage("Sorry Username is Already Existed!")
        elif existing_email == email:
            return errorpage("Sorry Email is Already Existed!")
            
        elif existing_phone == phone:
            return errorpage("Sorry Phone Record Already Existed!")
            
    if sum(char in symbolex for char in username) == 0 and len(username) >= 5 and sum (char in password for char in symbol)>=3 and len(password)>= 10:
        with open("details.txt", "a") as fileg:
            fileg.write(username+","+password+","+email+","+secq+","+seca+","+phone+"\n")
        return errorpage("You're successfully signed up!")
    elif sum(char in symbolex for char in username) == 0 and len(username) >= 5:
        return errorpage("Use a stronger Password!")
    elif sum (char in password for char in symbol)>=3 and len(password)>= 10:
        return errorpage("Sorry your Username contains a special character!")
    else:
        return errorpage("Both the username and password are incorrect, choose something else!")
    
@app.route("/additem", methods=["GET"])
def additem():
    return'''

<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<!-- Add Lobster font from Google Fonts -->
	<link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
	<style>
		h1 {
			font-family: 'Lobster', cursive;
		}
	</style>
</head>
<body bgcolor="#f5ed05">
	<br>
	<h1 style="color: #8a061e;" align="center">Enter a new item to your list!</h1>
	<br><br>
	<form method="POST" action="/additems" align="center">
		<input name="item" placeholder="Add ITEM" style="width:50%; min-height: 30px; padding-top: 0px; padding-bottom: 0px; padding-left: 15px; padding-right: 15px; font-size: 16px; font-family: arial; border: 2px solid #45068a; border-radius: 10px;">
		<input type="submit" value="ADD ITEM" style="width:25%; min-height: 30px; font-size: 16px; font-family: arial; background-color: white; border: 2px dashed blue; font-weight: bold; border-radius: 10px;">
	</form>
</body>
</html>




'''
    
    
    
@app.route("/additems", methods=["POST"])
def additems():
    item = request.form.get("item")
    username = session.get("username")
    password = session.get("password")

    updated_lines = []  # Store updated user records

    with open("details.txt", "r") as file:
        multilines = file.readlines()

    for singleline in multilines:
        line = singleline.strip().split(",")

        # If user matched, add the new item
        if username == line[0] and password == line[1] and item!="":
            line.append(item)  # Add the new item to user's list

        updated_line = ",".join(line)+"\n"  # Rebuild line
        updated_lines.append(updated_line)
    with open("details.txt", "w") as file:
        file.writelines(updated_lines)

    with open("details.txt", "r") as file:
        multilines=file.readlines()
    for singleline in multilines:
        line=singleline.strip().split(",")
        if line[0]==username and line[1] == password:
            session["username"]= username
            session["password"]= password
            if len(line)>2:
                htmlpage="<html><head><style>body {background-color: #f5ed05;} h1 {font-family: Lobster, cursive; color: #9c000d;} table {border: 3px dashed purple; background-color: white; padding: 30px; min-height: 60%; min-width: 30%; border-radius: 20%;}</style><link href=https://fonts.googleapis.com/css2?family=Lobster&display=swap rel=stylesheet></head><body><center><br><h1>Your List Items are listed below</h1><br><table><tr><td><ol>"
                for items in line[6:]:
                    htmlpage=htmlpage+"<li>"+items.upper()+"</li>"
                htmlpage=htmlpage+"""</td></tr><tr><td><form action="/additem"><input type="submit" value="Add New Item" style="border:2px dashed blue; border-radius: 12px; width: 100%; min-height: 30px; background-color: white; font-family: calibri; font-weight: bolder; font-size: 15px;"></input></form></td></tr></table></center></body>"""
                return redirect("/dashboard")
            else:
                return'''<h1>Sorry, You don't have any item on your list!</h1>'''
    
    return '''<h1>Sorry, You don't have any account.</h1>'''

def htmlg(item, i):
    return f"""
        <tr style="border:none; height:40px;">
            <td style="width: 40%; border:none; height:30px; padding-left:10px;">{item}</td>
            <td style="width:60%; border:none;">
                <form method="POST" action="/lists">
                    <input style="width:70%; height:30px; border:2px dashed red; padding-left:7px; padding-right:7px; border-radius:10px;" placeholder="Enter Item" name='{i}'>
                    <input style="width:25%; height:30px; border:2px dashed blue; background-color:white; border-radius:10px;" type="submit" value="Update Item">
                </form>
            </td>
        </tr>
    """

@app.route("/update", methods=["GET"])
def htmlpage():
    username = session.get("username")
    password = session.get("password")
    i = 0
    response = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Update Items</title>
    </head>
    <body bgcolor="#f5ed05">
        <center>
        <h1 style="text-align:center;">Update List Items</h1><br>
        <table border="2" width="70%" style="background-color:white; border:2px solid black; border-radius:20px;">
    """

    with open("details.txt", "r") as file:
        multilines = file.readlines()
    for singleline in multilines:
        line = singleline.strip().split(",")
        if username == line[0] and password == line[1]:
            for item in line[6:]:  # Start at index 6 (after phone number)
                response += htmlg(item, i)
                i += 1

    response += """
        </table>
        <br><form action="/dashboard"><input type="submit" value="Return to Dashboard" style="border:2px dashed blue; border-radius: 12px; width: 25%; min-height: 30px; background-color: white; font-family: calibri; font-weight: bolder; font-size: 15px;"></input></form>
        </center>
    </body>
    </html>
    """
    return response

@app.route("/lists", methods=["POST"])
def listupdate():
    username = session.get("username")
    password = session.get("password")

    with open("details.txt", "r") as file:
        multilines = file.readlines()

    newlines = []
    for singleline in multilines:
        line = singleline.strip().split(",")

        if username == line[0].strip() and password == line[1].strip():
            for i in range(len(line)):  # Only update list items (skip first 6 fields)
                new_val = request.form.get(str(i-6))
                if new_val and new_val.strip() != "":
                    line[i] = new_val.title().strip()
            newlines.append(",".join(line) + "\n")
        else:
            newlines.append(singleline)

    with open("details.txt", "w") as file:
        file.writelines(newlines)

    return htmlpage()




@app.route("/delete", methods=["GET"])
def delete():
    username=session.get("username")
    password=session.get("password")
    html="""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body bgcolor="#f5ed05">

<h1 style="font-family:Calibri; font-size:30px; color:#b52d00;" align="center">Delete List Items</h1><br>

<center><table style="min-width: 70%; height: 50px; padding-bottom:10px; padding-top:5px; padding-left:10px; padding-right:10px; background-color:white; border: 2px dashed #b00404; border-radius: 20px;"><tr><td width="70%">"""
    with open("details.txt", "r") as file:
        multilines=file.readlines()
    for singleline in multilines:
        line = singleline.strip().split(",")
        if line[0]==username and line[1]==password:
            i=0
            for item in line[6:]:
                html=html+"""<tr><td width="70%" style="font-family:arial;">""" +item+"""</td><td width="30%"><form method="POST" action="/deleted"><input type="submit" value="Delete Item" name="""+str(i)+""" style="width:100%; height: 40px; border: 2px solid darkblue; border-radius: 10px; background-color: white;"></form></td></tr>"""
                i=i+1
            html=html+"""</table></center></body></html>"""
    return html
                
                

@app.route("/deleted", methods=["POST"])
def deleted():
    lists = []
    username = session.get("username")
    password = session.get("password")
    
    with open("details.txt", "r") as file:
        multilines = file.readlines()

    for singleline in multilines:
        line = singleline.strip().split(",")
        
        if line[0] == username and line[1] == password:
            temp_line = line[:]  # make a copy to modify
            for i in range(len(line)):
                deleteitem = request.form.get(str(i))  # request.form keys are str
                if deleteitem != "":
                    u = i + 6
                    if u < len(temp_line):
                        temp_line.pop(u)
                        break  # minimal fix: prevent multiple shifting deletions
            lists.append(",".join(temp_line) + "\n")
        else:
            lists.append(singleline)

    with open("details.txt", "w") as file:
        file.writelines(lists)

    return redirect("/dashboard")


@app.route("/logout",methods=["GET","POST"])
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
