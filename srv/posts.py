import json
import markdown
import markdown_katex

# Set up a markdown converter with necessary extensions.
md = markdown.Markdown(extensions=['markdown_katex', 'fenced_code', 'codehilite'])


# Get list of posts and metadata from posts.json
with open('content/posts.json') as f:
    allposts = json.load(f)


# Get Post:
# Returns a string of the html for a given post
def getpost(name):
    # Read the file into a string
    # The file should be at content/name/name.md
    with open('content/{}/{}.md'.format(name, name)) as f:
        srctxt = f.read()

    return md.convert(srctxt)
