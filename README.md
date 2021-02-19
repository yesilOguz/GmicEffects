# GmicEffects

### INSTALLATION:
###### python 3.x
`pip3 install GmicEffects`
###### python 2.x
`pip install GmicEffects`

### USAGE:

##### for help:

    from GmicEffects import GmicEffects as ge
    import PIL.Image
    
    ge.help()#for help
    
##### for effects list:

    from GmicEffects import GmicEffects as ge
    import PIL.Image
    
    ge.effects()#for effects list

##### for example:

    from GmicEffects import GmicEffects as ge
    import PIL.Image
    
    oldPhoto = ge.old_photo("myphoto.png")#old photo effect
    
    # oldPhoto is pillow object
    
    oldPhoto.save("editedPhoto.png")#saved with pillow
