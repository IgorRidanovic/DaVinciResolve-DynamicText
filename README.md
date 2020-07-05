This is a proof of concept for DaVinci Resolve external dynamic title generation.

DaVinci Resolve V15 allows Fusion macros to be used on the edit page as title templates.
The macros are structured as plain text. It is trivial to substitue text payload strings
with arbitrary text.

The app has two buttons. One generates a date/time stamp at the time the button is pressed.
The other button retrieves Bundesliga RSS news (German football league) and formats the
headlines as a bottom of the screen crawl.

It is necessary to click each button once before launching Resolve for the first time.
Resolve loads the list or templates into the memory only once at start time. Once the
templates are loaded we can click the buttons to refresh the templates. The text contents
of the templates dropped on the timeline are frozen.

Video exmample: https://www.youtube.com/watch?v=w9l1IFbcxno
