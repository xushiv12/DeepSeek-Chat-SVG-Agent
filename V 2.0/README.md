# IMG plus

A tiny AI pixel-art image generator powered by DeepSeek chat model.

## What it does

This project lets a user type a prompt, sends that prompt to a DeepSeek reasoner model, asks the model to return a **10×10 pixel code**, and then renders the result as a colored image in the browser.

Instead of using a normal image model, this project uses a **text model** to generate structured pixel data.

## How it works

The system works like this:

1. The user enters a prompt.
2. The backend sends the prompt to the DeepSeek model.
3. The model must answer inside a special format:

```text
(::0000011111 0000011111 0000011111 ...::)
```
install:pip install flask openai
