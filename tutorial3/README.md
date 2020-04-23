# Tutorial 3

## Some Backgorund 

Were really cooking now! We're finally venturing beyond where we went together in class. In this tutorial I hope to show some of the nifty features readily avilable to you in python (and Google Colab) when you import some pretty great and light weight libraries. 

Here were going to look at:
* scikit-image 
* pyproj 
* folium 
* scikit lean 


### But - lets build on what weve done!

Lets use our little script from tutorial 2 to grab a landsat image to play with!

Were going to avoid the relatively short list of steps for [setting up a python package](https://packaging.python.org/tutorials/packaging-projects/) in our little git repo just to keep things simple for us. If we did this we could do fancy things like <code>%pip install git+https://github.com/NSCC-COGS/GDAA2030.git</code> and <code>import GDAA2030</code>>and things..., but I digress! We're instead going to continue using our little <i>hacky</i> method of importing functions from our repo. 