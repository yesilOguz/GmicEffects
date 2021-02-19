# GmicEffects

### INSTALLATION:
###### python 3.x
`pip3 install GmicEffects`
###### python 2.x
`pip install GmicEffects`

### USAGE:

##### for help:

    from GimpEffects import GimpEffects as ge
    import pillow
    
    ge.help()#for help
    
##### for effects list:

    from GimpEffects import GimpEffects as ge
    import pillow
    
    ge.effects()#for effects list

##### for example:

    from GimpEffects import GimpEffects as ge
    import pillow
    
    oldPhoto = ge.old_photo("myphoto.png")#old photo effect
    
    # oldPhoto is pillow object
    
    oldPhoto.save("editedPhoto.png")#saved with pillow
