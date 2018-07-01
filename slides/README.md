#  Creating reveal.js slide decks from a Jupyter notebook using `nbconvert`

Reveal.js is a Javascript framework for creating slide decks in HTML.  Visit [Reveal.js - The HTML Presentation Framework] for an impressive demonstration of its capabilities.  First, you will need to create a directory for your slide shows.  It needs to have reveal.js as a subdirectory.  It is easy to do, just follow these steps at the command line.

```bash
mkdir my_slideshows
cd my_slideshows
git clone https://github.com/hakimel/reveal.js/
```

Generating reveal.js presentations from Jupyter notebooks is also easy using the `nbconvert` utility.  It is included with the [Anaconda Python](https://www.anaconda.com/).  You can check to that it is installed by running `conda list | grep nbconvert`.  Directions on how to use `nbconvert` can be found [here](https://ipython.org/ipython-doc/3/notebook/nbconvert.html) and see the `--to slides` and `--output-dir='dest_dir'` options.  Follow these steps to generate a reveal.js slide deck from a Jupyter notebook.

```bash
jupyter nbconvert --to slides --output-dir='.' path-to-slides/my_slides.ipynb
```

Finally, just open your newly created HTML file in your browser and revel in your geekiness.
