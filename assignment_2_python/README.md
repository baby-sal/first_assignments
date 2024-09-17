# . ݁₊ ⊹ . ݁˖ . ݁Studio Ghibli Character Generator and Movie Recommendation . ݁₊ ⊹ . ݁˖ . ݁

## Welcome! Have you ever wondered what Ghibli character you resemble?

This app asks the user questions about their hair and eye color
and finds a character in the Ghibli universe who looks like them.

After the doppelganger is (or isn't...) revealed, the user can input a character
name to find out what film they are in and some information about the film. 

I used the Ghibli API to access information about the characters and the films.
The app sends a request to the API to form responses in the form of lists with the characters who match the user's hair colour and eye colour.
Secondly, the app will respond the URL relating to the character and loop through the list of films on the film endpoint
If there is a match found, then the app will print the film's details.
There is no set up required for the API

I imported the time function to make the user have to wait for the result, increasing their suspense.

Enjoy!

### How I'd like to improve:
- Recursion - if there is no match then being able to repeat that input again
- Be able to connect related colours of hair and eyes, so that there are more matches (some of the colour names are too specific)
- Make a response that is relevant to the Rotten Tomatoes score, e.g if bad, ask to suggest another.
- Files only append a new film title / doppelganger if the value is unique. 

⠀⠀⠀⠀⠀⠀⠀⠀⣴⠛⢆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡶⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡟⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⣰⡟⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡇⠀⡘⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣦⠀⠗⠒⠒⠒⠒⠒⠒⠼⢿⠀⡖⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⡟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠠⠤⣀⣠⣾⣿⠀⠸⠃⠀⠀⠀⢤⣤⠄⠀⢀⠲⠆⠀⠈⢄⡀⠠⠀⠀⠀⠀
⠀⠒⠒⠂⠰⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠈⠬⣦⠤⠤⠤⠀⠀
⠀⠀⠒⠒⣾⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢉⡉⠁⠀⠀
⠀⠀⣠⣾⣿⣿⡿⠃⣀⡤⠤⠒⠒⠒⠂⠀⠀⠐⠆⢀⡀⠀⠀⠀⠀⠀⠑⠄⠀⠀
⠀⣼⣿⣿⣿⡿⠃⣉⣀⡀⠀⠀⢀⣤⣶⣤⡀⠀⠀⠀⣀⣉⠑⠦⡀⠀⠀⠈⠢⡀
⠘⠛⠛⠛⠛⠀⠚⠋⠉⠙⠀⠀⠉⠉⠀⠈⠙⠀⠐⠛⠉⠙⠃⠀⠘⠂⠐⠀⠀⠃