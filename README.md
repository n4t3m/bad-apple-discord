# How2Use

The way this project works:

- Start off with the bad apple video. 
- Convert that to frames using ``frames.py``. After running this, you should have a ``./frames/`` folder with a couple thousand pictures.
- Next, convert each frame to an ascii image using ''.py''. It will output a json fike.
- Place your Discord Bot token in the ``bot.py`` file on the bottom line.
- Run this script, invite the bot to a server you're in, and use the command ``!run`` to start.
- If you want to make something similar to the video of the final product, you will need to speed up the video ``54.8x``. This should place it more or less perfectly. I used ffmpeg for this step because my goto video editor cannot speed anything up more than 50x.