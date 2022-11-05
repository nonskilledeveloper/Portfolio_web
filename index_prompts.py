welcome_message = ""

def welcome_function(enterprisename):
    global welcome_message
    i = 25 - len(enterprisename)
    for a in range(i):
        enterprisename = enterprisename+" "

    welcome_message = f"""
<pre>
#################################################
#                                               #
#     Nice to see you, {enterprisename}#
#                                               #
#################################################

 Some commands:
            
  startx  -  Starts a graphical interface (Developing)
  ls      -  List of files and directories
  cd      -  Move to an specific directory
  msg     -  Give me a feedback :D (Developing)
  help    -  Show more commands
</pre>"""


cat_welcome = """
<pre>
spaces=18-${#USER}
username=$USER

for spaces
do
username=username+" "
done

Printf "
#################################################
#                                               #
#     Nice to see you, %s       #
#                                               #
#################################################

 Some commands:
            
  startx  -  Starts a graphical interface (Developing)
  ls      -  List of files and directories
  cd      -  Move to an specific directory
  msg     -  Give me a feedback :D (Developing)
  help    -  Show more commands

" $username

</pre>"""



ls = """<pre>
<label style="color:#0000EF";>programming</label>                        <label style="color:#0000EF";>games</label>
<label style="color:#0000EF";>web_projects</label>                       <label style="color:#0000EF";>certs</label>
<label style="color:#0000EF";>courses</label>                          <label style="color:#0000EF";>hobbies</label>
<label style="color:#00FF00";>welcome.sh</label>                     <label style="color: yellow";>README.md</label>
</pre>"""



head_welcome = """
<pre>
spaces=18-${#USER}
username=$USER

for spaces
do
username=username+" "
done

Printf "
#################################################
</pre>"""

tail_welcome = """
<pre>

    Some commands:

    startx  -  Starts a graphical interface (Developing)
    ls      -  List of files and directories
    cd      -  Move to an specific directory
    msg     -  Give me a feedback :D (Developing)
    help    -  Show more commands and info

" $username
</pre>"""

cat_readme = """
<pre>
# My portfolio

Hello [enterprise_name]! 

I'm Carlos and this is my portfolio, if everything 
is running as it's supposed to, you should be 
receiving this website from a RaspBerry Pi server 
in my house 😄

![IMG_3075](assets/IMG_3075.jpeg)

Is it not great? 
Well, I've always liked these things

If this is not the case, because we are having a 
storm, or because someone accidentally spilled a 
drop of antimatter over it, then you will receive 
the website from a mirrroring server.

In any case you will know it in the following label:

`Home-Server: [homeserver_status]`

For this, I had to configure not only the operating
system and software in the RaspBerry, but also my
home network to share these resources to the public.

Languages, tools and other knowledge needed for this
project:

* Python
* HTML
* CSS
* JavaScript
* Svelte Framework (Still working with it)
* Linux
* Networks
* A weird humor sense

I learned most of these knowledges since my childhood, 
you can read a little more about my history in the 
"About me" section of my website, or typing the 
command "whoami"
</pre>"""

head_readme = """
<pre>
# My portfolio

Hello [Company Name]! 

I'm Carlos and this is my portfolio, if everything is
running as it's supposed to, you should be receiving
this website from a RaspBerry Pi server in my house
😄

![IMG_3075](assets/IMG_3075.jpeg)
</pre>"""

tail_readme = """
<pre>
* JavaScript
* Svelte Framework (Still working with it)
* Linux
* Networks
* A weird humor sense

I learned most of these knowledges since my childhood, 
you can read a little more about my history in the 
"About me" section of my website, or typing the 
command "whoami"
</pre>"""