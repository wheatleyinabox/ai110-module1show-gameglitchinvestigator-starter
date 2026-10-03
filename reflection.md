# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

It was fine, just very buggy, the only thing that seem to work reliably was when you had a correct guess and you were out of attempts. Everything else wasn't working or totally unreliable.
- List at least two concrete bugs you noticed at the start  
   (for example: "the hints were backwards").

The attempts weren't be displayed correctly, nor were they going down as expected after looking at the debugging bit. The next was the hint messages were totally wrong. It was suggesting in the wrong direction and it didn't account for the upper and lower limits of the secret range.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                         | Expected Behavior                                   | Actual Behavior                                | Console Output / Error                               |
| ----------------------------- | --------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------- |
| Make an attempt               | Attempt count decreases by 1                        | Attempt didn’t decrease at all nor did history | Nothing was updated in internal logic, phantom click |
| Entering 85 when secret is 55 | Hint message says “Go Lower”                        | Hint messages says “Go Higher”                 | 85 > 55, I should be told to lower my number         |
| Set mode to Easy              | Range changes from 100 to 20. Attempts update to 5 | Range remains the same. Attempts update to 4  | Doesn’t update range and attempts properly           |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

Claude Code in terminal 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

It noticed the attempts weren't displaying or working properly while working on the check_guess function. It didn't provide the solution or an edit (since I told it not to do that) but it did see it was a problem.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.

Like I said before it was detecting other bugs I had listed but I wasn't asking for those to be looked at.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I went through and reran the app to test it that way. If it worked, it worked!
- Describe at least one test you ran (manual or using pytest)  
   and what it showed you about your code.

I did some manual testing with the higher and lower and I noticed that the history of the game wasn't being reset on top of rerunning the game not letting me enter attempts. So it give me another thing to look at!
- Did AI help you design or understand any tests? How?

Yeah, I had it walk me through everything it did. It would explain the problem and suggest what should be fixed and then I went in to review before letting it change anything. I was also having an issue running them and it helped me! (I was running the wrong command lol)

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

Reruns are basically jumping to the top of your code and running it all again. Until another rerun statement is in the stack then it'll go it again! Everything is recalculated and redefined. Using sessions state basically lets you use a dictionary to maintain a variable through reruns so they don't get reset.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

I like using Git, I'm pretty comfortable in it and it's super valuable.
- What is one thing you would do differently next time you work with AI on a coding task?

Personally, I don't like running my AI within my codebase. I like to be able to control how much it sees and what it does. So if I can find a way for it to REALLY not access anything unless I ask it to would be nice!
- In one or two sentences, describe how this project changed the way you think about AI generated code.

In terms of the code itself, nothing has really changed. I know to review and keep a level of distance with AI code. So if any issues arise, I can see what's up. I also liked how it wrote the tests, the verbose syntax makes sense to me so yeah sometimes AI code has good suggestions and sometimes it doesn't. And that's why he review!