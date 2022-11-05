pp_ls = """
<pre>
<label style="color:#FFFF00";>python.md</label>                    <label style="color:#FFFF00";></label>
</pre>"""

head_pythonmd = """
<pre>
# These are my projects written in Python

Python is personally the programming language where
I feel much more comfortable to work with, but I'm
open to work with other languages in which I have a
little of experience.

Following i'll post a list of python projects that I
have developed by myself, certainly these are not so
many projects, but as i am constantly thinking how to
</pre>"""

tail_pythonmd = """
<pre>
# This website

Yes, as i mentioned previously in the README.md, this
website is built with Python, i used the framework
Flask, which is the framework where i have more
experience with.

### GitHub Link -> [Portfolio]({{portf_url}}})

I hope you enjoy it 🌵
</pre>"""

cat_pythonmd = """
<pre>
# These are my projects written in Python

Python is personally the programming language where
I feel much more comfortable to work with, but I'm
open to work with other languages in which I have a
little of experience.

Following i'll post a list of python projects that I
have developed by myself, certainly these are not so
many projects, but as i am constantly thinking how to
solve my own issues or other's issues with 
programming, this list surely will grow soon 

-------

# JobBank_Finder 

## What it does?

This is a Web Scraper specially designed to find job
offers from the canadian website 
[Job Bank](https://jobbank.gc.ca/)
that matches with specific criterias that are not 
possible to configure in the own website, at least 
up today.

### GitHub Link -> [JobBank_Finder](github.com/)

Also, this software ranks the job offers, and
generates a file with the results found that 
is very easy to read.

![](assets/16675304997229.jpg)

For example, I'm going to check the job offers 
avalaible today, which have a positive LMIA
(Approved), that do not requires high education,
that do not require previous experience...  
Until now, all these criterias are possible
to configure in the website, yes, but here it 
comes the interesting part:

We are going to point higher those offers that
adds a link to their website, and that has an
official email

Why? 

Because these offers are most likely possible to
be oficial, real offers. It's known that there are
too many scams on this website, and scammers 
commonly are lazy, they won't complicate themselves
buying a website, and if they do it, probably this 
website will not be so well built, or it will be very
generic, anyway, we'll have another thing to analyze
before sending our curriculum, or any other kind of
information.

![](assets/16675314895783.jpg)

So, the software starts analyzing every job offer
in the website by itself, in the console it give 
us a small summary about what this software is
finding, the section "Stars Rank" is the important
part, since it will rank higher as it matches with
our criterias, and these criterias are completely 
customizable by code (For the moment) and in the 
running time (I'll be working on it).

![](assets/16675319232825.jpg)

Finally as we can see, we get a folder, with the
date of today, which contains all the information
found. 

Let's open it... 

![](assets/16675320324870.jpg)

Inside we have an HTML file

![](assets/16675321433976.jpg)

And here we have... 

Certainly today we were not so lucky, because the 
maximun punctuation getted it was 0.5 in the 
Stars Rank (This rank works from 0 to 5 points),
but i've had much better days, in fact, with this 
software I'm looking for a job for my father, and we 
have already got a call for an interview 

(Wish us luck) 🌵

## Legallity 

Neither the users agreements, the "robots.txt" 
section of the website or the canadian laws forbides
to scrap in this website

## It worths it?

I'm completely sure that it worths to use it, since
it can analyze, maybe hundred of offers per minute
and rank them, a thing that for a human, it would be 
absolutely impossible to do 

---
# OCR_Scanner

This software i wrote it for a friend, he asked me
to wrote this since he constantly received such kind
of lists with the purpose to send them a message, and
he was very tired of writing  down these numbers 
manually in his smartphone, this was a very
repetitive task, and he asked me if i was able to 
authomatize it

### GitHub link -> [OCR_Scanner](github.com/)

## How to use it

We need a capture with phone numbers and usernames,
like the following example:

![](assets/16675456834447.jpg)

This is petty similar to the one my friend was used
to see. 

Now, we have to save this capture in the same folder
as our OCR_Scanner, and the capture must to be named
with the numbers starting from "1.png" 
(It also supports jpg images)

We would have something very similar to this

![](assets/16675459486870.jpg)

Now, we execute the OCR_Scanner from the terminal of
our operating system

![](assets/16675460180043.jpg)

It will analyze all the captures that you add to the
folder, in a few seconds, in this case i only used
one capture, but you can add even hundreds

At the final, you have to do an "Enter" into the 
terminal, and you will get a csv document similar
to this one

![](assets/16675461656445.jpg)

![](assets/16675462755669.jpg)

As it is a CSV file, it's possible to import these
contacts to the telephone, some telephones can read
contacts from a CSV file, others need to install an
extra application, but it is completely possible,
and it saves time when you need to write contacts 
this way for any reason 

---

# Real time chat

This is a very basic web chat in real time, it was
made with Python and Flask as a framework, honestly 
it's too basic and it was possible to improve it a 
lot, or make it another way, but here we go

### Github link -> [Chat](github.com/)

## How to use it

![](assets/16675372103500.jpg)

These are the documents of the project, 
let's run it...

![](assets/16675372700352.jpg)

And now, see te result

![](assets/16675373252656.jpg)

And we type a message now

![](assets/16675374443742.jpg)

We can join us with another tab

![](assets/16675375089506.jpg)

Nothing so complex, but it works 😄

---

# Password_Generator

This is also a not so complex program, it is very
common to code something like this on the Internet,
in this case, i wrote it as a part of this website, 
because i use it to generate the 'sessions' password 
of flask

As this is a short code, i think it's possible to
share here directly:

```
from random import randint

# <Random secret key:>
passchars = ['a','b','c','d','e','f','g','h','i',
'j','k','l','m','n','ñ','o','p','q','r','s','t',
'u','v','w','x','y','z'] # 27 chars

passchars_uppers = []
for x in range(len(passchars)):
    passchars_uppers.append(passchars[x].upper())

passnumbers = ['0','1','2','3','4','5','6','7','8',
'9']

passchars_unusuals = ['#','!',' ','$','/','(',')',
'=','&','%','°','|','{','}','*','[',']','.','_',
'-',',',';','<','>','¡','¿','?','+'] # 28 chars

pass_order = {
1:passchars,
2:passnumbers,
3:passchars_uppers,
4:passchars_unusuals}

rndscrt_key = ""

for x in range(256):
    temp_char = pass_order[randint(1,4)]
    temp_char = str(temp_char[randint(1, 
    len(temp_char)-1)])
    rndscrt_key = rndscrt_key + temp_char
# </Random secret key>
```

It generates a very strong 256 characters password, 
i'm aware that is completely possible to improve it, 
for example, playing with the seeds of the randint
library

---

# This website

Yes, as i mentioned previously in the README.md,this
website is built with Python, i used the framework
Flask, which is the framework where i have more
experience with.

### GitHub Link -> [Portfolio]({{portf_url}}})

I hope you enjoy it 🌵
</pre>"""