from transformers import pipeline

summarizer=pipeline("summarization")

summing=summarizer("""let's talk about the strategy

  friends this strategy, mostly those who are trading options might have heard

and even there is a dedicated video related to this strategy in our channel and was reached to many

you may have seen that video and I suggest keeping your mind as a blank paper

either the thing we told or someone else, do not keep any rules that this is the same strategy

if I'm telling you to keep my own videos aside means that I'm trying to explain this in a different way

 not as in the theory of what to sell and wait but the reality related to this strategy

if you want to really earn money, with experience for years of following a strategy

what we have to observe and what we have to understand related to this strategy

I'll take step by step so don't keep your mind predetermined the only you can understand

this strategy name is Short Strangle. If you divide this name, Short, Strangle

Short means selling, Strangle in option strategy means from the present trading price

 after moving to a particular distance which is our wish and selecting a CE & PE

So if we short it,  it is a Short Strangle or if we buy, it is a Long Strangle but the strategy we are following is

Short Strangle. Moving a distance from the present trading price, the distance we have to go

and how to select it, I'll speak later but let's go to a particular distance and sell CE & PE

for example, present nifty is trading at 14500, we select 14000PE by going below 500

and select 50,000CE by going 500 points above and sell them both. This is Short Strangle

I told you this for you to understand, this is only 10% n the entire strategy but

but if you see this theoretically  or in any videos you'll see that this is the entire strategy

if the profit comes simply by selling through moving a distance many might have earned in the market till now

but never take this strategy lightly. again and again, I'm telling in all the strategies

if you want to follow only 1 strategy I'll tell only Short Strangle

so the logic of this Short Strangle is if the trader thinks that the market is in the range-bound

then Short Strangle is employed. The real logic for this strategy is the market will be in a range

that it will move in the particular range.""")

print(summing)
