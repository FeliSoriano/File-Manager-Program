# File-Manager-Program
This is a Program I created as my final project of Udemy's Complete Python Bootcamp course. I could still use a lot of work, so I'm going to use it to learn how to use GitHub as well.


I download a ton of files, specially since the pandemic started, and they don't always come ordered how I'd like them to. Just as an example, I recently downloaded all the files from a Data Science on-line course on Udemy. If you are familiar with the platform courses, you'll know that a course is usually devided in sections, each composed by a couple of videos and maybe some excercises. In this particular case, each video had a corresponding folder. In each folder there was the file they used on their video presentatio. But there where a couple of problems, to say the least. I'll name the first two that come to mind:
 
 - The folder's names where unrecognizable
 - If the same file was used in two videos, you get the file twice (one file was atually repeated 11 times)

Now, this may not seem as much of a problem. But similar things appear when teachers send me dozens of classes, unorganized. Or when I download manga or anime and the name of the first episode of Odd Taxi looks like _0wehabsa2adfajon.1_ (An Etherum adress might be easier to read). Sudennly, I look at my folders, and they are a complete mess, that makes one waste time looking for files that should be easiy accesible. 

Now one could solve pretty much all of these problems with simple for loop in a few lines of code. The problem with that approach is that python doesn't necessarily reads the files or directories in the same order you see them on your screen. As of now, I have failed to find a satisfying solution to this, particularly annoyng, issue.[^1] You can't sort the files if you don't know (or they don't have) how the naming is formated.
[^1]: According to the os module [documentation](https://docs.python.org/3/library/os.html#os.listdir) the order is arbitrary.

My program tries to find solutions to these kind of problems. I'm currently on "version 3" of the program, although I'm not sure that's how I should be calling each update.

The first version focused on single-file handling. It allowed to move, rename or delete a single file or folder, you also needed to provide the full path of the file/directory you wanted to work with.

Version 2 got read of the need to type a full path. The program would find the file/directory you wanted to work with for you, all you needed was it's name. This function, called _find()_ still has a lot of problems that I'll be trying to solve in the near future, as stated bellow.

The third version added mass-file managing options. This is the version I have been using, but it still have **A LOT** of problems. I'll list some of them here.


1. It's unreadable and unorganized (even I have some trouble reading it).
2. Even though I added a couple of fail-safes, user errors can break it (i.e you mistakingly enter a path when the code thought it was getting a file-name).
3. It may not be able to find the file you are looking for. (this can be solved if the user gives a "_better_" path, but this shouldn't be neccesary).
4. Doesn't work on files with spaces in them (ie. My First Repositorie)
5. It's definetly not user-friendly. 

As I said at the beggining, I'm new to this whole GitHub thing, and as I, hopefully, just showed you, I also have a _horribly written kind-of-working_ code. My hopes are to drastiaclly improve my program, while also learning how this tool works. I realize that I haven't included any information on how the code works in here, I'll work on that soon.

This are the steps I'm going to take going foward. 

1st, I'm going to rewrite the hole thing, adding comments, making a separate file for the functions, etc.

2nd, I'll either add on this README or make a new text file explaining the thinking that went into all the code written so far, struggles I had and ideas on how to imporve.

3rd, I'm going to work in improving the _find()_ function. I'm gonna be honest, I took it from StackOverflow, and modified it a little. The plan is to re-write to make it better fit my use-case. 

4th would probably be error handling.

Those four steps will probably keep me occupied for the time being. All help is appreciated. You can contact me at my email felysoryano@gmail.com or on twitter @FeliSorianoE.

Thanks for taking interest in my project.

PD: I'm not a native english speaker, so I'm sorry for any mistakes I might have made. 
