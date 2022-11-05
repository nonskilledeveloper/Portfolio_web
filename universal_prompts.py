neofetch = ""
pwd_path = ""

def pwd_function(enteprisename, prompt_path):
    global pwd_path
    pwd_path = f"""
<pre>
/Users/{enteprisename}{prompt_path}
</pre>
"""

def neofetch_function(enterprisename):
    global neofetch

    neofetch = f"""
<pre>

                <label style="color: #32FF00;"> {enterprisename}</label><label style="color: white;">@</label><label style="color: #FF0000;">root</label>
                <label style="color: white;"> -----------------</label>
                 <label style="color: yellow;">OS:</label><label style="color: white;"> TacOS arm128</label>
<label style="color: white;">┈┈┈┈╭╯╭╯╭╯┈┈┈┈┈</label>  <label style="color: yellow;">Host:</label><label style="color: white;"> SuperServer</label>
<label style="color: white;">┈┈┈╱▔▔▔▔▔╲▔╲┈┈┈</label>  <label style="color: yellow;">Kernel:</label><label style="color: white;"> 42.12.0</label>
<label style="color: white;">┈┈╱┈╭╮┈╭╮┈╲╮╲┈┈</label>  <label style="color: yellow;">Uptime:</label><label style="color: white;"> 3 months, 21 days</label>
<label style="color: white;">┈┈▏┈▂▂▂▂▂┈▕╮▕┈┈</label>  <label style="color: yellow;">Packages:</label><label style="color: white;"> 1,234 (Brew)</label>
<label style="color: white;">┈┈▏┈╲▂▂▂╱┈▕╮▕┈┈</label>  <label style="color: yellow;">Shell:</label><label style="color: white;"> zsh 98.8.2</label>
<label style="color: white;">┈┈╲▂▂▂▂▂▂▂▂╲╱┈┈</label>  <label style="color: yellow;">Terminal:</label><label style="color: white;"> 0dayTerm</label>
                 <label style="color: yellow;">CPU:</label><label style="color: white;"> AMX AtomicThread 4040X</label>
                 <label style="color: yellow;">GPU:</label><label style="color: white;"><strong> Strong_Nuclear_Force</strong> 6180</label>
</pre>

"""

mkdir = """
I also want to make things together 🌵
"""

help = """
<pre>

startx  -   Loads a graphical interface

ls      -   Lists files and directories

cd      -   cd command will move you through 
            every directory inside our system, 
            use this command followed by the 
            directory you want to go in, Ex: 
            'cd games'

color   -   Use this command followed by a
            color, you can write colors with 
            HEX format 
            Ex: 'color #FF0000', 
            RGB format 
            Ex: 'color rgb(255,000,000)'
            or RGBA format 
            Ex: 'color rgba(255,000,000,0.5)'

            Also, you can write some color names
            directly Ex: 'color red'

sh      -   Use this command followed by a
            binary file, you are allowed to
            run some programs, Ex:
            'sh welcome.sh'

neofetch  - Displays information about your 
            operating system, software and 
            hardware in an aesthetic and 
            visually pleasing way

cat     -  Use this command followed by a file
           to show its text content, Ex:
           'cat welcome.sh'

help    -  Use this command followed by a number
           to show you the next page of commands
           Ex: 'help 2'
</pre>"""

help_2 = """
<pre>
md      -   Use this command followed by a 
            MarkDown file to interpret a 
            MarkDown document

pwd     -   Shows the current path

head    -   Shows the first 10 lines of a
            file

tail    -   Shows the last 10 lines of a
            file
</pre>"""

mv_command = """
<pre>
Let's move the world 🌎
</pre>"""

touch_command = """
<pre>
If you are reading this, 
it's because you touched my heart ❤️
</pre>"""

rm_command = """
<pre>
Sorry my friend, what is done is done, 
let's improve what it comes 👾
</pre>"""
