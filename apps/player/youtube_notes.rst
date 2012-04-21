##
# autohide
# Values: 0, 1, and 2 (default). This parameter indicates whether the video controls will automatically hide after a video begins playing. The default behavior is for the video progress bar to fade out while the player controls (play button, volume control, etc.) remain visible.
# If this parameter is set to 0, the video progress bar and the video player controls will be visible throughout the video.
# If this parameter is set to 1, then the video progress bar and the player controls will slide out of view a couple of seconds after the video starts playing. They will only reappear if the user moves her mouse over the video player or presses a key on her keyboard.

##
# autoplay
# Values: 0 or 1. Default is 0. Sets whether or not the initial video will autoplay when the player loads.
# border
# Values: 0 or 1. Default is 0. Setting to 1 enables a border around the entire video player. The border's primary color can be set via the color1 parameter, and a secondary color can be set by the color2 parameter.
# cc_load_policy
# Values: 1. Default is based on user preference. Setting to 1 will cause closed captions to be shown by default, even if the user has turned captions off.
# color1, color2
# Values: Any RGB value in hexadecimal format. color1 is the primary border color, and color2 is the video control bar background color and secondary border color.
# controls
# Values: 0 or 1. Default is 1. This parameter indicates whether the video player controls will display. If this parameter is set to 0, then the player controls will not display, causing the player to look like the chromeless player.
# disablekb
# Values: 0 or 1. Default is 0. Setting to 1 will disable the player keyboard controls. Keyboard controls are as follows: 
#      Spacebar: Play / Pause 
#      Arrow Left: Jump back 10% in the current video 
#      Arrow Right: Jump ahead 10% in the current video 
#      Arrow Up: Volume up 
#      Arrow Down: Volume Down
# egm
# Values: 0 or 1. Default is 0. Setting to 1 enables the "Enhanced Genie Menu". This behavior causes the genie menu (if present) to appear when the user's mouse enters the video display area, as opposed to only appearing when the menu button is pressed.
# 
# Note: This parameter is not supported in the AS3 embedded player.
# enablejsapi
# Values: 0 or 1. Default is 0. Setting this to 1 will enable the Javascript API. For more information on the Javascript API and how to use it, see the JavaScript API documentation.
