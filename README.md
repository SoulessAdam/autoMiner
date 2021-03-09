# autoMemer
Automated script/program for sending s.mine, made in 2 minutes with minimal effort and no concern for efficiency or a tidy code base. Written in Python.

## Instructions for use: 
### Intercepting a good post request:
* Using a tool like Fiddler, Burp or general network debugging tools your browser may have included, intercept a successful POST request method spawned from sending a message.
* Extract the necessary info and add it to the python script. The main info you will need is:
  * Your authentication token for sending messages e.g. authorization: {Token here} in your POST headers.
  * The request url, used to specify which channel messages are sent to e.g. https://discord.com/api/v8/channels/####################/messages
* Fill in the necessary information in the script and run

### General use:
* Use this tool whenever necessairy, you may run multiple instances all with different auth tokens allowing you to bot on many accounts at once, however, the spamming of the Discord API will not only cause flags but will result in a pretty quick rate limit. 
* It is advised you obtain the following items before use:
  * A pickaxe, preferrably a better one that basic so you don't have to keep buying them. Keep in mind that as you get picks with higher durability, the $/hit increases, meaning profit is lower. 
  * Field Rations
  * Some form of gear, this one is important for long term usage, feel free to spend extra on this one. 

* To stop the script use the Keyboard Interrupt shortcut, ``Control``+``C`` to stop, or close the Python window.

![image](https://user-images.githubusercontent.com/58148487/110537188-444d9500-811a-11eb-9e55-45e66f6b01d3.png)
![image](https://user-images.githubusercontent.com/58148487/110537212-4a437600-811a-11eb-9592-38d0fc01d275.png)

###### By using this tool you aknowledge that you are at risk of punishment from the Sandra Bot Team and/or Discord. I am not responisble for any losses or punishment you recieve, it is your choice to use this tool and your responsibility to keep use of said tool covert, unsuspicious and unknown to those you do not trust, in order to avoid bans. 
