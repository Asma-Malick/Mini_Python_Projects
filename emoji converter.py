def emoji_converter(message):
  word=message.split(" ")
  emoji={
    ":)": "😊",
    ":(": "🙁",
    ":D": "😁",
    ":P": "😜",
    ":O": "😮",
    "B)": "😎",
    ";)": "😉",
    ":/": "😕",
    ":|": "😐",
    ">:(": "😡",
    
  }
  output=""
  for i in word:
    output+=emoji.get(i,i) +" "
  return output

message=input(">")
print(emoji_converter(message))
