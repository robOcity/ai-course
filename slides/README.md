# Creating reveal.js slide decks from a Jupyter notebook using `nbconvert`

## Generating slidedecks

Reveal.js is a Javascript framework for creating slide presentations in HTML.  Visit [Reveal.js - The HTML Presentation Framework] for an impressive demonstration of its capabilities.  

Get started by creating a you will need to create a directory for your slide shows.  To use it you will need to download a copy from the [Reveal.js github page](https://github.com/hakimel/reveal.js/), and of course `git clone https://github.com/hakimel/reveal.js/` works too.  Your new reveal.js folder should be a subdirectory of you slideshow folder.  It is easy to do, just follow these steps at the command line.  __I suggest NOT making reveal.js submodule since it complicates your git workflows.  The slide show folder does not need to be in the repository.  If it isn't, you can copy your slidedeck/notebook in and out of it, and check them in when you are done making changes.  Notebooks are hard to track in git anyway, so this approach works better than it may sound.__

```bash
mkdir my_slideshows
cd my_slideshows
git clone https://github.com/hakimel/reveal.js/
```

Generating reveal.js presentations from Jupyter notebooks is also easy using the `nbconvert` utility.  It is included with [Anaconda Python](https://www.anaconda.com/).  Check that it is installed by running `conda list | grep nbconvert`.  Directions on how to use `nbconvert` can be found [here](https://ipython.org/ipython-doc/3/notebook/nbconvert.html) and see the `--to slides` and `--output-dir='dest_dir'` options.  Follow these steps to generate a reveal.js slide deck from a Jupyter notebook.

```bash
jupyter nbconvert --to slides --output-dir='.' path-to-slides/my_slides.ipynb
```

Finally, just open your newly created HTML file in your browser and revel in your geekiness.

## Getting images to display

If you added images to your notebook using markdown `[description](filename)` you were gravely disappointed with you slidedeck because the images did not appear.  The solution is to use python code rather than markdown for display.  Here the code you need to include.

'''python
from IPython.display import Image
Image(filename)
'''

## Creating web pages

Generating webpages are also easy _and_ your images appear too!  If you output your webpage to different directory than where your notebooks are stored, then you will need to copy the images folder into the same relative position so that the images files can be successfully loaded.

```bash
jupyter nbconvert --to html --output-dir='.' path-to-slides/my_slides.ipynb
```

## Making PDFs

Generating PDF documents works too. To generate PDF, I found that you had to be in the same folder as your notebook file when you run `jupyter nbconvert`. 

```bash
jupyter nbconvert --to pdf --output-dir='.' path-to-slides/my_slides.ipynb
```

