from flask import Flask, render_template, request, session, redirect
import universal_prompts, index_prompts, courses_prompts, programming_prompts, certs_prompts, passgen, requests

app = Flask(__name__)

app.secret_key = passgen.rndscrt_key

@app.route("/<enterprise_name>", methods=['GET', 'POST'])
def index(enterprise_name):
    universal_command = False
    prompt_path = ''
    print("Hubo un ingreso de: "+ enterprise_name) 
    
    request_data = "None"
    
    # <Process the name of the enterprise> in required sections
    index_prompts.welcome_function(enterprise_name)
    universal_prompts.neofetch_function(enterprise_name)
    universal_prompts.pwd_function(enterprise_name, prompt_path)
    # </Process the name of the enterprise> in required sections
    
    universal_prompts_dic = {
    "pwd":universal_prompts.pwd_path,
    "neofetch":universal_prompts.neofetch,
    "help":universal_prompts.help,
    "help 2":universal_prompts.help_2
    }

    prompt_dictionary = {
    "sh ./welcome.sh":index_prompts.welcome_message,
    "sh welcome.sh":index_prompts.welcome_message,
    "./welcome.sh":index_prompts.welcome_message,
    "sh ./welcome.sh":index_prompts.welcome_message,
    "./*.sh":index_prompts.welcome_message,
    "sh ./*.sh":index_prompts.welcome_message,
    "sh *.sh":index_prompts.welcome_message,

    "cat welcome.sh":index_prompts.cat_welcome,
    "cat *.sh":index_prompts.cat_welcome,
    "cat *.*":index_prompts.cat_welcome,

    "ls":index_prompts.ls,
    "head welcome.sh": index_prompts.head_welcome,
    "tail welcome.sh": index_prompts.tail_welcome,
    "cat readme.md": index_prompts.cat_readme,
    "cat *.md": index_prompts.cat_readme,
    "head readme.md": index_prompts.head_readme,
    "head *.md": index_prompts.head_readme,
    "tail readme.md": index_prompts.tail_readme,
    "tail *.md": index_prompts.tail_readme
    } # Import the dictionary of commands for the index

    prompt_color = "white" # Set default value for prompt color

    if 'prompt_color' in session:

        prompt_color = session['prompt_color'] # If there are cookies, set the value of these cookies as prompt color

    else:

        prompt_color = prompt_color
    
    bash_prompt_response = prompt_dictionary["./welcome.sh"] # default message
    
    if request.method == 'POST':

        request_data = request.form.get('command') # If there is a post method, save the post as a command in 'request_data'
        request_data = str(request_data).lower()
    
    try:
        bash_prompt_response = universal_prompts_dic[request_data]
        universal_command = True
    except:

        pass

    try:

        bash_prompt_response = prompt_dictionary[request_data] # Try to find the posted command inside the command dictionary

    except:

        
        if request_data.startswith("color ") and len(request_data) > 5:
            prompt_color = str(request_data.split(" ")[1])
            session['prompt_color'] = prompt_color
        
        elif len(request_data) > 3 and request_data.startswith("sh ") or request_data.startswith("./") or request_data.startswith("sh ./"):
            bash_prompt_response = request_data+': No such file'
        
        elif request_data.startswith("cd ") and request_data != 'cd courses' and request_data != 'cd ..' and request_data != 'cd programming' and request_data != 'cd certs' and request_data != 'cd hobbies':
            bash_prompt_response = request_data+': No such directory'
        
        elif request_data.startswith("mkdir ") or request_data == "mkdir":
            bash_prompt_response = universal_prompts.mkdir
        
        elif request_data.startswith("mv ") or request_data == "mv":
            bash_prompt_response = universal_prompts.mv_command
        
        elif request_data.startswith("rm ") or request_data == "rm":
            bash_prompt_response = universal_prompts.rm_command
        
        elif request_data.startswith("touch ") or request_data == "touch":
            bash_prompt_response = universal_prompts.touch_command

        else:
            if request_data == "None":
                pass
            elif request_data == "clear":
                bash_prompt_response=''
            elif request_data == "md readme.md" or request_data == "md *.md":
                return redirect('/'+enterprise_name+'/README.md', code=302)

            elif request_data == "cd courses":
                return redirect('/'+enterprise_name+'/courses', code=302)
            
            elif request_data == "cd programming":
                return redirect('/'+enterprise_name+'/programming',code=302)
            
            elif request_data == "cd certs":
                return redirect('/'+enterprise_name+'/certs',code=302)
            
            elif request_data == "cd hobbies":
                return redirect('/'+enterprise_name+'/hobbies',code=302)
            
            elif request_data == "cd .." or request_data == "cd..":
                bash_prompt_response = "Hey! Where are you going? There are six folders and a lot of fun here 😄"
            
            elif request_data == "startx" or request_data.startswith("startx "):
                bash_prompt_response = "Ups, this command still under a developing process 👷🏾‍♂️"
            else:
                if universal_command == True:
                    universal_command = False
                else:
                    bash_prompt_response= 'zsh: command not found: '+str(request_data)


    return render_template("console_shell.html",enterprise_name=enterprise_name, bash_prompt_response=bash_prompt_response, prompt_color=prompt_color, prompt_path=prompt_path)

@app.route("/<enterprise_name>/README.md", methods=['GET'])
def index_readme(enterprise_name):
    homeserver_status = ""
    try:
        homeserver_status = requests.get('https://www.superserver.com/')
        if homeserver_status != "":
            homeserver_status = 'ON'
    except:
        homeserver_status = 'OFF'

    return render_template("root_readme.html",enterprise_name=enterprise_name, homeserver_status=homeserver_status)

@app.route("/<enterprise_name>/courses/microsoft+p.md", methods=['GET'])
def microsoftp_readme(enterprise_name):

    return render_template("microsoft+p.html", enterprise_name=enterprise_name)

@app.route("/<enterprise_name>/courses/google+p.md", methods=['GET'])
def googlep_readme(enterprise_name):

    return render_template("google+p.html", enterprise_name=enterprise_name)

@app.route("/<enterprise_name>/courses", methods=['GET', 'POST'])
def courses_shell(enterprise_name):
    bash_prompt_response = ""
    prompt_path = '/courses'
    request_data = "None"
    universal_command = False

    # <Process the name of the enterprise> in required sections
    universal_prompts.neofetch_function(enterprise_name)
    universal_prompts.pwd_function(enterprise_name, prompt_path)
    # </Process the name of the enterprise> in required sections

    prompt_color = "white"

    if 'prompt_color' in session:

        prompt_color = session['prompt_color']

    else:

        prompt_color = prompt_color

    # <Import dictionaries>
    prompt_dictionary = {
    "ls":courses_prompts.ls_courses,

    "cat platzi.md": courses_prompts.cat_platzimd,
    "head platzi.md": courses_prompts.head_platzimd,
    "tail platzi.md": courses_prompts.tail_platzimd,

    "cat google+p.md": courses_prompts.cat_googlepmd,
    "head google+p.md": courses_prompts.head_googlepmd,
    "tail google+p.md": courses_prompts. tail_googlepmd,

    "cat microsoft+p.md": courses_prompts.cat_microsoftp,
    "head microsoft+p.md": courses_prompts.head_microsoftp,
    "tail microsoft+p.md": courses_prompts.tail_microsoftp
    }

    universal_prompts_dic = {
    "pwd":universal_prompts.pwd_path,
    "neofetch":universal_prompts.neofetch,
    "help":universal_prompts.help,
    "help 2":universal_prompts.help_2
    }
    # </Import dictionares>

    prompt_color = "white"

    if 'prompt_color' in session:
        prompt_color = session['prompt_color']
    
    else:

        prompt_color = prompt_color
    
    if request.method == 'POST':

        request_data = request.form.get('command') # If there is a post method, save the post as a command in 'request_data'
        request_data = str(request_data).lower()
    
    try:
        bash_prompt_response = universal_prompts_dic[request_data]
        universal_command = True
    except:

        pass

    try:

        bash_prompt_response = prompt_dictionary[request_data]

    except:
        if request_data.startswith("color ") and len(request_data) > 5:
            prompt_color = str(request_data.split(" ")[1])
            session['prompt_color'] = prompt_color
        
        elif len(request_data) > 3 and request_data.startswith("sh ") or request_data.startswith("./") or request_data.startswith("sh ./"):
            bash_prompt_response = request_data+': No such file'
        
        elif request_data.startswith("cd ") and request_data != 'cd ..':
            bash_prompt_response = request_data+': No such directory'
        
        elif request_data.startswith("mkdir ") or request_data == "mkdir":
            bash_prompt_response = universal_prompts.mkdir
        
        elif request_data.startswith("mv ") or request_data == "mv":
            bash_prompt_response = universal_prompts.mv_command
        
        elif request_data.startswith("rm ") or request_data == "rm":
            bash_prompt_response = universal_prompts.rm_command
        
        elif request_data.startswith("touch ") or request_data == "touch":
            bash_prompt_response = universal_prompts.touch_command

        else:
            if request_data == "None":
                pass
            elif request_data == "clear":
                bash_prompt_response=''
            elif request_data == "md platzi.md":
                return redirect('/'+enterprise_name+'/courses/platzi.md', code=302)
            
            elif request_data == "md microsoft+p.md":
                return redirect('/'+enterprise_name+'/courses/microsoft+p.md',code=302)
            
            elif request_data == "md google+p.md":
                return redirect('/'+enterprise_name+'/courses/google+p.md',code=302)

            elif request_data == "cd .." or request_data == "cd..":
                return redirect('/'+enterprise_name, code=302)

            elif request_data == "md *.md":
                bash_prompt_response = "I'm sure nobody would be able to read so many things at the same time 🤔"
            
            elif request_data == "startx" or request_data.startswith("startx "):
                bash_prompt_response = "Ups, this command still under a developing process 👷🏾‍♂️"

            else:
                if universal_command == True:
                    universal_command = False
                else:
                    bash_prompt_response= 'zsh: command not found: '+str(request_data)

    return render_template("console_shell.html",enterprise_name=enterprise_name, prompt_color=prompt_color, request_data=request_data, prompt_path=prompt_path,bash_prompt_response=bash_prompt_response)

@app.route("/<enterprise_name>/courses/platzi.md", methods=['GET'])
def courses_readme(enterprise_name):
    return render_template("platzi_courses.html", enterprise_name=enterprise_name)

@app.route("/<enterprise_name>/programming/python.md", methods=['GET'])
def python_programming(enterprise_name):
    return render_template("python_projects.html", enterprise_name=enterprise_name)

@app.route("/<enterprise_name>/programming", methods=['GET', 'POST'])
def programming_projects(enterprise_name):
    bash_prompt_response = ""
    prompt_path = '/programming'
    request_data = "None"
    universal_command = False

    # <Process the name of the enterprise> in required sections
    universal_prompts.neofetch_function(enterprise_name)
    universal_prompts.pwd_function(enterprise_name, prompt_path)
    # </Process the name of the enterprise> in required sections

    prompt_color = "white"

    if 'prompt_color' in session:

        prompt_color = session['prompt_color']

    else:

        prompt_color = prompt_color

    # <Import dictionaries>
    prompt_dictionary = {
    "ls": programming_prompts.pp_ls,
    "head python.md": programming_prompts.head_pythonmd,
    "head *.md": programming_prompts.head_pythonmd,
    "tail python.md": programming_prompts.tail_pythonmd,
    "tail *.md": programming_prompts.tail_pythonmd,
    "cat python.md": programming_prompts.cat_pythonmd,
    "cat *.md": programming_prompts.cat_pythonmd

    }

    universal_prompts_dic = {
    "pwd":universal_prompts.pwd_path,
    "neofetch":universal_prompts.neofetch,
    "help":universal_prompts.help,
    "help 2":universal_prompts.help_2
    }
    # </Import dictionares>

    prompt_color = "white"

    if 'prompt_color' in session:
        prompt_color = session['prompt_color']
    
    else:

        prompt_color = prompt_color
    
    if request.method == 'POST':

        request_data = request.form.get('command') # If there is a post method, save the post as a command in 'request_data'
        request_data = str(request_data).lower()
    
    try:
        bash_prompt_response = universal_prompts_dic[request_data]
        universal_command = True
    except:

        pass

    try:

        bash_prompt_response = prompt_dictionary[request_data]

    except:
        if request_data.startswith("color ") and len(request_data) > 5:
            prompt_color = str(request_data.split(" ")[1])
            session['prompt_color'] = prompt_color
        
        elif len(request_data) > 3 and request_data.startswith("sh ") or request_data.startswith("./") or request_data.startswith("sh ./"):
            bash_prompt_response = request_data+': No such file'
        
        elif request_data.startswith("cd ") and request_data != 'cd ..':
            bash_prompt_response = request_data+': No such directory'
        
        elif request_data.startswith("mkdir ") or request_data == "mkdir":
            bash_prompt_response = universal_prompts.mkdir
        
        elif request_data.startswith("mv ") or request_data == "mv":
            bash_prompt_response = universal_prompts.mv_command
        
        elif request_data.startswith("rm ") or request_data == "rm":
            bash_prompt_response = universal_prompts.rm_command
        
        elif request_data.startswith("touch ") or request_data == "touch":
            bash_prompt_response = universal_prompts.touch_command

        else:
            if request_data == "None":
                pass
            elif request_data == "clear":
                bash_prompt_response=''
            elif request_data == "md python.md":
                return redirect('/'+enterprise_name+'/programming/python.md', code=302)

            elif request_data == "cd .." or request_data == "cd..":
                return redirect('/'+enterprise_name, code=302)

            elif request_data == "md *.md":
                return redirect('/'+enterprise_name+'/programming/python.md', code=302)
            
            elif request_data == "startx" or request_data.startswith("startx "):
                bash_prompt_response = "Ups, this command still under a developing process 👷🏾‍♂️"

            else:
                if universal_command == True:
                    universal_command = False
                else:
                    bash_prompt_response= 'zsh: command not found: '+str(request_data)

    return render_template("console_shell.html",enterprise_name=enterprise_name, prompt_color=prompt_color, request_data=request_data, prompt_path=prompt_path,bash_prompt_response=bash_prompt_response)

@app.route("/<enterprise_name>/certs", methods=['GET','POST'])
def certs(enterprise_name):
    bash_prompt_response = ""
    prompt_path = '/certs'
    request_data = "None"
    universal_command = False

    # <Process the name of the enterprise> in required sections
    universal_prompts.neofetch_function(enterprise_name)
    universal_prompts.pwd_function(enterprise_name, prompt_path)
    # </Process the name of the enterprise> in required sections

    prompt_color = "white"

    if 'prompt_color' in session:

        prompt_color = session['prompt_color']

    else:

        prompt_color = prompt_color

    # <Import dictionaries>
    prompt_dictionary = {
    "ls": certs_prompts.ls_certs
    }

    universal_prompts_dic = {
    "pwd":universal_prompts.pwd_path,
    "neofetch":universal_prompts.neofetch,
    "help":universal_prompts.help,
    "help 2":universal_prompts.help_2
    }
    # </Import dictionares>

    prompt_color = "white"

    if 'prompt_color' in session:
        prompt_color = session['prompt_color']
    
    else:

        prompt_color = prompt_color
    
    if request.method == 'POST':

        request_data = request.form.get('command') # If there is a post method, save the post as a command in 'request_data'
        request_data = str(request_data).lower()
    
    try:
        bash_prompt_response = universal_prompts_dic[request_data]
        universal_command = True
    except:

        pass

    try:

        bash_prompt_response = prompt_dictionary[request_data]

    except:
        if request_data.startswith("color ") and len(request_data) > 5:
            prompt_color = str(request_data.split(" ")[1])
            session['prompt_color'] = prompt_color
        
        elif len(request_data) > 3 and request_data.startswith("sh ") or request_data.startswith("./") or request_data.startswith("sh ./"):
            bash_prompt_response = request_data+': No such file'
        
        elif request_data.startswith("cd ") and request_data != 'cd ..':
            bash_prompt_response = request_data+': No such directory'
        
        elif request_data.startswith("mkdir ") or request_data == "mkdir":
            bash_prompt_response = universal_prompts.mkdir
        
        elif request_data.startswith("mv ") or request_data == "mv":
            bash_prompt_response = universal_prompts.mv_command
        
        elif request_data.startswith("rm ") or request_data == "rm":
            bash_prompt_response = universal_prompts.rm_command
        
        elif request_data.startswith("touch ") or request_data == "touch":
            bash_prompt_response = universal_prompts.touch_command

        else:
            if request_data == "None":
                pass
            elif request_data == "clear":
                bash_prompt_response=''

            elif request_data == "cd .." or request_data == "cd..":
                return redirect('/'+enterprise_name, code=302)
            
            elif request_data == "startx" or request_data.startswith("startx "):
                bash_prompt_response = "Ups, this command still under a developing process 👷🏾‍♂️"

            else:
                if universal_command == True:
                    universal_command = False
                else:
                    bash_prompt_response= 'zsh: command not found: '+str(request_data)

    return render_template("console_shell.html",enterprise_name=enterprise_name, prompt_color=prompt_color, request_data=request_data, prompt_path=prompt_path,bash_prompt_response=bash_prompt_response)

@app.route("/<enterprise_name>/hobbies", methods=['GET','POST'])
def hobbies(enterprise_name):
    bash_prompt_response = ""
    prompt_path = '/hobbies'
    request_data = "None"
    universal_command = False

    # <Process the name of the enterprise> in required sections
    universal_prompts.neofetch_function(enterprise_name)
    universal_prompts.pwd_function(enterprise_name, prompt_path)
    # </Process the name of the enterprise> in required sections

    prompt_color = "white"

    if 'prompt_color' in session:

        prompt_color = session['prompt_color']

    else:

        prompt_color = prompt_color

    # <Import dictionaries>
    prompt_dictionary = {
    
    }

    universal_prompts_dic = {
    "pwd":universal_prompts.pwd_path,
    "neofetch":universal_prompts.neofetch,
    "help":universal_prompts.help,
    "help 2":universal_prompts.help_2
    }
    # </Import dictionares>

    prompt_color = "white"

    if 'prompt_color' in session:
        prompt_color = session['prompt_color']
    
    else:

        prompt_color = prompt_color
    
    if request.method == 'POST':

        request_data = request.form.get('command') # If there is a post method, save the post as a command in 'request_data'
        request_data = str(request_data).lower()
    
    try:
        bash_prompt_response = universal_prompts_dic[request_data]
        universal_command = True
    except:

        pass

    try:

        bash_prompt_response = prompt_dictionary[request_data]

    except:
        if request_data.startswith("color ") and len(request_data) > 5:
            prompt_color = str(request_data.split(" ")[1])
            session['prompt_color'] = prompt_color
        
        elif len(request_data) > 3 and request_data.startswith("sh ") or request_data.startswith("./") or request_data.startswith("sh ./"):
            bash_prompt_response = request_data+': No such file'
        
        elif request_data.startswith("cd ") and request_data != 'cd ..':
            bash_prompt_response = request_data+': No such directory'
        
        elif request_data.startswith("mkdir ") or request_data == "mkdir":
            bash_prompt_response = universal_prompts.mkdir
        
        elif request_data.startswith("mv ") or request_data == "mv":
            bash_prompt_response = universal_prompts.mv_command
        
        elif request_data.startswith("rm ") or request_data == "rm":
            bash_prompt_response = universal_prompts.rm_command
        
        elif request_data.startswith("touch ") or request_data == "touch":
            bash_prompt_response = universal_prompts.touch_command

        else:
            if request_data == "None":
                pass
            elif request_data == "clear":
                bash_prompt_response=''

            elif request_data == "cd .." or request_data == "cd..":
                return redirect('/'+enterprise_name, code=302)
            else:
                if universal_command == True:
                    universal_command = False
                else:
                    bash_prompt_response= 'zsh: command not found: '+str(request_data)

    return render_template("console_shell.html",enterprise_name=enterprise_name, prompt_color=prompt_color, request_data=request_data, prompt_path=prompt_path,bash_prompt_response=bash_prompt_response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")