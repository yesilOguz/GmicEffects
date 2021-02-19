import gmic
import PIL.Image


class GmicEffects:  
    def help():
        return """When using an effect, you must give the path to its file. For example GmicEffects.poster_hope('mypath/myphoto.png'). If you want an array with all effects, GmicEffects.effects(). Remember, this library gives you a pillow object."""

    def effects():
        effects = ["old_photo", "stained_glass", "poster_hope", "polygon", "sketch", "lifiny", "paloraid", "cubism",
                   "vector_paint", "cartoon", "poster", "pencil", "paint", "edge_fire", "boxfitting",
                   "color_abstraction", "freaky_details", "gogh", "polloc", "klee", "picasso", "blur", "bokeh", "shine",
                   "diamond"]

        return effects

    def old_photo(dosyaYol):
        gmic_images = []

        effect = '{} old_photo'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def stained_glass(dosyaYol):
        gmic_images = []

        effect = '{} stained_glass 20%,1 cut 0,20'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def poster_hope(dosyaYol):
        gmic_images = []

        effect = '{} poster_hope'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def polygon(dosyaYol):
        gmic_images = []

        effect = '{} polygonize 100,10 +fill "I!=J(1) || I!=J(0,1)?[0,0,0]:I"'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def sketch(dosyaYol):
        gmic_images = []

        effect = '{} +sketchbw 1 reverse blur[-1] 3 blend[-2,-1] overlay'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def lifiny(dosyaYol):
        gmic_images = []

        effect = '{} linify 60'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def paloraid(dosyaYol):
        gmic_images = []

        effect = '{} to_rgba polaroid 5,30 rotate 20 drop_shadow , drgba'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def cubism(dosyaYol):
        gmic_images = []

        effect = '{} cubism'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def vector_paint(dosyaYol):
        gmic_images = []

        effect = '{} fx_vector_painting 9.37,0'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def cartoon(dosyaYol):
        gmic_images = []

        effect = '{} cartoon 3,50,10,0.25,3,16'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def poster(dosyaYol):
        gmic_images = []

        effect = '{} fx_posterize 150,30,1,6,0,0,1,0'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def pencil(dosyaYol):
        gmic_images = []

        effect = '{} fx_feltpen 300,50,1,0.1,20,5,0'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def paint(dosyaYol):
        gmic_images = []

        effect = '{} fx_painting 5,2.5,1.5,50,1,0'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def edge_fire(dosyaYol):
        gmic_images = []

        effect = '{} fire_edges 0.7,0.25,0.5,25,20'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def boxfitting(dosyaYol):
        gmic_images = []

        effect = '{} boxfitting'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def color_abstraction(dosyaYol):
        gmic_images = []

        effect = '{} fx_color_abstraction 1,10,0.2,0'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def freaky_details(dosyaYol):
        gmic_images = []

        effect = '{} fx_freaky_details 2,10,1,11,0,32,0'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def gogh(dosyaYol):
        gmic_images = []

        effect = '{} _fx_stylize starrynight +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,10,2,1.85,0'.format(
            dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def polloc(dosyaYol):
        gmic_images = []

        effect = '{} _fx_stylize convergence +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,50,2,1.85,0'.format(
            dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def klee(dosyaYol):
        gmic_images = []

        effect = '{} _fx_stylize redwaistcoat +fx_stylize 1,4,0,0,0.67,3.17,3,0.5,0.06,3,3,0,0.7,5,0,2,0,5,5,7,1,30,0,2.05,1.85,0'.format(
            dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def picasso(dosyaYol):
        gmic_images = []

        effect = '{} _fx_stylize reservoirhortadeebro +fx_stylize 1,6,0,0,0.5,2,3,0.5,0.1,3,3,0,0.7,1,0,1,0,5,5,7,1,30,10,2,1.85,0'.format(
            dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def blur(dosyaYol):
        gmic_images = []

        effect = '{} blur_x 30'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def bokeh(dosyaYol):
        gmic_images = []

        effect = '{} fx_bokeh 3,8,0,30,8,4,0.3,0.2,210,210,80,160,0.7,30,20,20,1,2,170,130,20,110,0.15,0'.format(
            dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def shine(dosyaYol):
        gmic_images = []

        effect = '{} +b 0.5% lightrays. , n. 0,255 blend add,0.9'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic

    def diamond(dosyaYol):
        gmic_images = []

        effect = '{} repeat 3 smooth 40,0,1,1,2 done blur xy,5 rodilius'.format(dosyaYol)
        gmic.run(effect, gmic_images)

        sayi = len(gmic_images) - 2

        PIL_image_from_gmic = gmic_images[sayi].to_PIL()

        return PIL_image_from_gmic


