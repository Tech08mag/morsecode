letters_to_morse = {
  "a":".-",
  "b":"-...",
  "c":"-.-.",
  "d":"-..",
  "e": ".",
  "f":"..-.",
  "g":"--.",
  "h":"....",
  "i":"..",
  "j":".---",
  "k":"-.-",
  "l":".-..",
  "m":"--",
  "n":"-.",
  "o":"---",
  "p":".--.",
  "q":"--.-",
  "r":".-.",
  "s":"...",
  "t":"-",
  "u":"..-",
  "v":"...-",
  "w":".--",
  "x": "-..-",
  "y":"-.--",
  "z":"--..",
  "0":"-----",
  "1":".----",
  "2":"..---",
  "3":"...--",
  "4":"....-",
  "5":".....",
  "6":"-....",
  "7":"--...",
  "8":"---..",
  "9":"----.",
  " ":" "
}

morse_to_letters = {
  ".-":"a",
  "-...":"b",
  "-.-.":"c",
  "-..":"d",
  ".":"e",
  "..-.":"f",
  "--.":"g",
  "....":"h",
  "..":"i",
  ".---":"j",
  "-.-":"k",
  ".-..":"l",
  "--":"m",
  "-.":"n",
  "---":"o",
  ".--.":"p",
  "--.-":"q",
  ".-.":"r",
  "...":"s",
  "-":"t",
  "..-":"u",
  "...-":"v",
  ".--":"w",
  "-..-":"x",
  "-.--":"y",
  "--..":"z",
  "-----":"0",
  ".----":"1",
  "..---":"2",
  "...--":"3",
  "....-":"4",
  ".....":"5",
  "-....":"6",
  "--...":"7",
  "---..":"8",
  "----.":"9",
  " ":" "
}
morsetext = []
dot = "."
minus = "-"
def get_user_input():
  text = input("Gebe deinen Text ein: ").lower()
  return text

def letters_to_morse(text):
  for n in text:
    if n in letters_to_morse.keys():
        morsetext.append(letters_to_morse[n])


def morse_to_letters(text):
  for s in text:
    if s in morse_to_letters.keys():
        morsetext.append(morse_to_letters[s])

def system_out():
  for m in morsetext:
    print(m, end=" ")
  print()
  morsetext.clear()


while True:
  text = get_user_input()
  if dot in text or minus in text:
    morse_to_letters(text)
  else:
    letters_to_morse(text)
  system_out()