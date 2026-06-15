A pretty simple discord bot, it has only a few functions. 
In order to use the bot, you need to download discord.py(it's an API, which the bot uses).

First things first, in order to connect the code to the bot itself. You do that by swapping the "Your bot token" text in line 88 for your actual token. Next, you need to swap the "Your guild ID" text for the ID of the guild you want to use the bot in (I haven't tested it in multiple servers yet).

The current functions of the bot are:

1. It shows every message sent in the guild(along with who wrote them) in the terminal.
2. If someone reacts to a message with an emote, the bot will print out a text saying "(username) reacted to a message" (you need to uncomment lines 29 and 30 for this to work).

Now, unto the slash commands. Those are the commands you use by typing "/" + the command name. Discord should tell you what commands you can use. Right now, there are the following commands:

1. The /hello commands, which just prints out the text "Hello there!".
2. The /print command, which allows you to type in a text, which the bot will then print out.
3. The /embed command, it's basically an embed test, but it shows you different functions embeds have, so you can customize it however you want.
4. The /check_info command, which displays various information about the user which uses it, in a form of an embed. The information it dispays are:the username, the profile picture, the main(top) role, the date on which the user joined the server, the creation date of the account, all of the user's roles and the date when the command was issued.
5. The /button command, which is a test of the buttons. It displays 3 buttons, for now only one of them works. It has a "Click me" text written on it and makes the bot print out "(username) clicked me.".
